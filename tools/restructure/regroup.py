#!/usr/bin/env python3
"""Split one page into a folder of pages by picking heading sections, in any
order, and regenerate its redirect entries.

restructure.py only cuts a page into contiguous runs of H2s. This takes a
list of heading paths per new page, so a subsection can move to a different
page than its parent. Every line of the old page must land on exactly one new
page, and every heading must come out with the same text, or it refuses.

    python3 tools/restructure/regroup.py OLD_SITE MKDOCS

Run from the repo root on a clean checkout with the old page in place.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from restructure import DOCS, FENCE, LINK, SELF, build, headings, url  # noqa: E402

OLD = 'konamisystem573.md'
FOLDER = 'arcade/konami/573'

# (file, [selectors]). ('T', path) takes a heading's whole section, ('H', path)
# only the heading and its text up to its first subheading. A path element
# matches the one child heading that contains it.
PAGES = [
    ('index.md', [('H', ()), ('T', ('Differences vs. PS1',)), ('T', ('Credits, sources and links',))]),
    ('registers.md', [
        ('H', ('Register map',)),
        ('T', ('Register map', 'IDE registers')),
        ('T', ('Register map', 'RTC registers')),
        ('H', ('Register map', 'Other registers')),
        ('T', ('Register map', 'Other registers', '0x1f500000')),
        ('T', ('Register map', 'Other registers', '0x1f560000')),
        ('T', ('Register map', 'Other registers', '0x1f5c0000')),
        ('T', ('Register map', 'Other registers', '0x1f6a0000')),
    ]),
    ('builtin-io.md', [
        ('T', ('Register map', 'Konami ASIC registers')),
        ('T', ('Register map', 'Other registers', '0x1f520000')),
        ('T', ('Register map', 'Other registers', '0x1f600000')),
        ('T', ('Register map', 'Other registers', '0x1f680000')),
        ('T', ('JVS interface',)),
    ]),
    ('expansion-io.md', [('T', ('I/O boards',))]),
    ('security-cartridges.md', [('T', ('Security cartridges',))]),
    ('external-modules.md', [('T', ('External modules',))]),
    ('bios.md', [('T', ('BIOS',)), ('T', ('Bootleg mod boards',))]),
    ('drives.md', [('T', ('Notes', 'Known working replacement drives'))]),
    ('games.md', [
        ('T', ('Game-specific information',)),
        ('H', ('Notes',)),
        ('T', ('Notes', 'Hard-to-install games')),
        ('T', ('Notes', 'Homebrew guidelines')),
        ('T', ('Notes', 'Missing support for PAL mode')),
        ('T', ('Notes', 'Flash chips and PCMCIA cards')),
        ('T', ('Notes', 'Known working replacement PCMCIA cards')),
        ('T', ('Notes', 'Bemani launcher error and status codes')),
    ]),
    ('pinouts.md', [('T', ('Pinouts',))]),
]

NAV = [
    ('Konami System 573', 'index.md'), ('Register Map', 'registers.md'),
    ('Built-in I/O and JVS', 'builtin-io.md'), ('Expansion I/O Boards', 'expansion-io.md'),
    ('Security Cartridges', 'security-cartridges.md'), ('External Modules', 'external-modules.md'),
    ('BIOS and Bootleg Mod Boards', 'bios.md'), ('CD/DVD Drives', 'drives.md'),
    ('Games and Notes', 'games.md'), ('Pinouts', 'pinouts.md'),
]


class Node:
    def __init__(self, level, title, start):
        self.level, self.title, self.start = level, title, start
        self.children, self.end, self.body_end = [], None, None


def tree(lines):
    root = Node(0, '', 0)
    stack, fenced = [root], False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if fenced or not line.startswith('#'):
            continue
        level = len(line) - len(line.lstrip('#'))
        if level == 1:
            continue                        # the page title belongs to the root
        while stack[-1].level >= level:
            stack.pop().end = i
        node = Node(level, line.lstrip('#').strip(), i)
        stack[-1].children.append(node)
        stack.append(node)
    for n in stack:
        n.end = len(lines)

    def body(n):
        n.body_end = n.children[0].start if n.children else n.end
        for c in n.children:
            body(c)
    body(root)
    return root


def find(root, path):
    n = root
    for part in path:
        hit = [c for c in n.children if part in c.title]
        assert len(hit) == 1, (path, part, [c.title for c in n.children])
        n = hit[0]
    return n


def heading_lines(lines):
    out, fenced = [], False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and line.startswith('#'):
            out.append(i)
    return out


def main():
    old_site, mkdocs = sys.argv[1:3]
    lines = open(os.path.join(DOCS, OLD), encoding='utf-8').read().split('\n')
    root = tree(lines)

    owner = [None] * len(lines)
    pages = {}
    for fn, sels in PAGES:
        idx = []
        for kind, path in sels:
            n = find(root, path)
            rng = range(n.start, n.body_end if kind == 'H' else n.end)
            for i in rng:
                assert owner[i] is None, (fn, path, i, owner[i])
                owner[i] = fn
            idx += rng
        pages[fn] = idx
    missing = [i + 1 for i, o in enumerate(owner) if o is None]
    assert not missing, f'lines on no page: {missing[:20]}'

    # write the pages, remembering where each line came from
    origin = {}
    subprocess.run(['git', 'rm', '-q', os.path.join(DOCS, OLD)], check=True)
    for fn, idx in pages.items():
        new = f'{FOLDER}/{fn}'
        path = os.path.join(DOCS, new)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        body = [lines[i] for i in idx]
        while body and not body[-1].strip():
            body.pop()
        open(path, 'w', encoding='utf-8').write('\n'.join(body) + '\n')
        origin[new] = idx

    cfg = open('mkdocs.yml', encoding='utf-8').read()
    entry = f'  - {OLD}\n'
    assert cfg.count(entry) == 1, 'nav entry for the old page not found'
    section = '  - Konami System 573:\n' + ''.join(
        f'    - {t}: {FOLDER}/{f}\n' for t, f in NAV)
    open('mkdocs.yml', 'w', encoding='utf-8').write(cfg.replace(entry, section))

    new_site = old_site.rstrip('/') + '-573'
    build(mkdocs, new_site)

    # old heading ordinal -> (new page, new id), checked on the heading text
    old_heads = headings(old_site, OLD)
    old_lines = heading_lines(lines)
    assert len(old_heads) == len(old_lines), (len(old_heads), len(old_lines))
    by_line = dict(zip(old_lines, old_heads))
    ids = {}
    for new, idx in origin.items():
        body = open(os.path.join(DOCS, new), encoding='utf-8').read().split('\n')
        new_heads = headings(new_site, new)
        src = [idx[j] for j in heading_lines(body)]
        assert len(src) == len(new_heads), (new, len(src), len(new_heads))
        for j, (nid, text) in zip(src, new_heads):
            oid, otext = by_line[j]
            assert otext == text, (new, otext, text)
            ids[oid] = (new, nid)
    assert len(ids) == len(old_heads)

    table = {'': url(f'{FOLDER}/index.md')}
    table.update({oid: url(new) + '#' + nid for oid, (new, nid) in ids.items()})
    mp = os.path.join('tools', 'redirects', 'map.json')
    m = json.load(open(mp, encoding='utf-8'))
    assert OLD[:-3] not in m
    m[OLD[:-3]] = table
    with open(mp, 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=1, sort_keys=True)
        f.write('\n')

    # re-point links: from the new pages (moved two folders down) and into
    # them from everywhere else
    def rewrite(path, base_old):
        text = open(path, encoding='utf-8').read().split('\n')
        here = os.path.dirname(os.path.relpath(path, DOCS))
        fenced, changed = False, 0

        def fix(mt):
            nonlocal changed
            t = mt.group(2)
            s = SELF.match(t)
            if s and s.group(1) + '.md' == OLD:
                anchor = s.group(2) or ''
                new, nid = ids[anchor] if anchor else (f'{FOLDER}/index.md', '')
                changed += 1
                return mt.group(1) + 'https://psx-spx.consoledev.net/' + url(new) + (
                    '#' + nid if nid else '') + mt.group(3)
            if ':' in t.split('/')[0]:
                return mt.group(0)
            ours = here.startswith(FOLDER)
            p, _, anchor = t.partition('#')
            if p:
                target = os.path.normpath(os.path.join(base_old, p))
            elif ours:
                target = OLD
            else:
                return mt.group(0)
            if target == OLD:
                new, nid = ids[anchor] if anchor else (f'{FOLDER}/index.md', '')
            elif ours:
                new, nid = target, anchor
            else:
                return mt.group(0)
            rel = os.path.relpath(new, here or '.')
            if new == os.path.relpath(path, DOCS):
                rel = ''
            changed += 1
            return mt.group(1) + rel + ('#' + nid if nid else '') + mt.group(3)

        for n, line in enumerate(text):
            if FENCE.match(line):
                fenced = not fenced
            elif not fenced:
                text[n] = LINK.sub(fix, line)
        open(path, 'w', encoding='utf-8').write('\n'.join(text))
        return changed

    total = 0
    for dirpath, _dirs, files in os.walk(DOCS):
        for fn in files:
            if fn.endswith('.md'):
                path = os.path.join(dirpath, fn)
                rel = os.path.relpath(path, DOCS)
                base = '' if rel.startswith(FOLDER) else os.path.dirname(rel)
                total += rewrite(path, base)
    print(f'{len(pages)} pages, {len(ids)} anchors mapped, {total} links re-pointed')


if __name__ == '__main__':
    main()
