#!/usr/bin/env python3
"""Move docs/ into the nested layout, split the big pages along their H2s,
and generate the old-URL redirect map.

Content is moved, never edited: the only text changes are the link targets
(re-pointed at wherever the target heading now lives), a split page's H2
becoming its new file's H1, and a title line on each grouped part.

    python3 tools/restructure/restructure.py OLD_SITE MKDOCS

OLD_SITE is a build of the tree before the move (the heading ids are read from
the rendered HTML, so the map uses exactly the anchors readers have pasted).
MKDOCS is the mkdocs binary to build the new tree with. Run from the repo root
on a clean checkout of the old layout.
"""
import json
import os
import re
import subprocess
import sys

# Pages that move whole. Anchors are unchanged, so their stubs pass the
# fragment through.
MOVES = {
    'arcadecabinets.md': 'arcade/arcadecabinets.md',
    'psxdevboardchipsets.md': 'dtl/psxdevboardchipsets.md',
    'psxdevboardprotocol.md': 'dtl/psxdevboardprotocol.md',
    'cdromdrive.md': 'ps1/cdr/cdromdrive.md',
    'cdromformat.md': 'ps1/cdr/cdromformat.md',
    'cdromvideocdsvcd.md': 'ps1/cdr/cdromvideocdsvcd.md',
    'cdrominternalinfoonpsxcdromcontroller.md': 'ps1/cdr/cdrominternalinfoonpsxcdromcontroller.md',
    'cpuspecifications.md': 'ps1/cpu/cpuspecifications.md',
    'geometrytransformationenginegte.md': 'ps1/cpu/gte/geometrytransformationenginegte.md',
    'gtepipelinetimings.md': 'ps1/cpu/gte/gtepipelinetimings.md',
    'macroblockdecodermdec.md': 'ps1/cpu/mdec/macroblockdecodermdec.md',
    'hardwarenumbers.md': 'ps1/hardwarenumbers.md',
    'memorymap.md': 'ps1/system/memorymap.md',
    'iomap.md': 'ps1/system/iomap.md',
    'interrupts.md': 'ps1/system/interrupts.md',
    'dmachannels.md': 'ps1/system/dmachannels.md',
    'timers.md': 'ps1/system/timers.md',
    'memorycontrol.md': 'ps1/system/memorycontrol.md',
    'partialwordwrites.md': 'ps1/system/partialwordwrites.md',
    'unpredictablethings.md': 'ps1/system/unpredictablethings.md',
    'cheatdevices.md': 'ps1/pio/cheatdevices.md',
    'expansionportpio.md': 'ps1/pio/expansionportpio.md',
    'pocketstation.md': 'ps1/sio/pocketstation.md',
    'serialinterfacessio.md': 'ps1/sio/serialinterfacessio.md',
    'soundprocessingunitspu.md': 'ps1/spu/soundprocessingunitspu.md',
    'controller-pinout.jpg': 'ps1/sio/controller-pinout.jpg',
}

# Pages that stay where they are. The 573 page moves to arcade/konami/573/
# together with its split, once that cut is agreed.
STAYS = ('index.md', 'aboutcredits.md', 'konamisystem573.md')

# Pages that split. Everything before the first H2 (the title and the page's
# own link list) becomes the folder's index.md.
#   'each': one file per H2, the H2 promoted to the file's H1.
#   groups: a run of consecutive H2s per file, starting at the first H2 whose
#           title starts with the given prefix, under a new H1 title.
SPLITS = {
    'graphicsprocessingunitgpu.md': ('ps1/gpu', 'each', 'GPU '),
    'kernelbios.md': ('ps1/kernelbios', 'each', 'BIOS '),
    'pinouts.md': ('ps1/pinouts', 'each', 'Pinouts - '),
    'controllersandmemorycards.md': ('ps1/sio/controllersandmemorycards', 'each', ''),
    'cdromfileformats.md': ('ps1/cdr/cdromfileformats', [
        ('executables', 'Executables and Debug Files', 'CDROM File Playstation EXE'),
        ('graphics', 'Textures, 2D and 3D Graphics', 'CDROM File Video Texture Image TIM'),
        ('streaming', 'Video Streaming and BS Compression', 'CDROM File Video STR Streaming'),
        ('audio', 'Audio', 'CDROM File Audio Single Samples'),
        ('archives', 'Archives', 'CDROM File Archives with Filename'),
        ('compression', 'Compression', 'CDROM File Compression'),
        ('diskimages', 'Disk Images', 'CDROM Disk Images CCD'),
    ], None),
}

# The nav, in the old reading order grouped into sections. A split page's
# entry expands to its index plus its parts.
NAV = [
    'index.md',
    {'PlayStation': [
        {'System': ['memorymap.md', 'iomap.md', 'interrupts.md', 'dmachannels.md', 'timers.md',
                    'memorycontrol.md', 'partialwordwrites.md', 'unpredictablethings.md']},
        {'CPU': ['cpuspecifications.md', 'geometrytransformationenginegte.md',
                 'gtepipelinetimings.md', 'macroblockdecodermdec.md']},
        {'GPU': 'graphicsprocessingunitgpu.md'},
        'soundprocessingunitspu.md',
        {'CD-ROM': ['cdromdrive.md', 'cdromformat.md', {'CDROM File Formats': 'cdromfileformats.md'},
                    'cdromvideocdsvcd.md', 'cdrominternalinfoonpsxcdromcontroller.md']},
        {'Serial Ports (SIO)': [{'Controllers and Memory Cards': 'controllersandmemorycards.md'},
                                'pocketstation.md', 'serialinterfacessio.md']},
        {'Expansion Port (PIO)': ['expansionportpio.md', 'cheatdevices.md']},
        {'Kernel (BIOS)': 'kernelbios.md'},
        {'Pinouts': 'pinouts.md'},
        'hardwarenumbers.md',
    ]},
    {'Arcade': ['arcadecabinets.md', 'konamisystem573.md']},
    {'Dev Boards': ['psxdevboardchipsets.md', 'psxdevboardprotocol.md']},
    'aboutcredits.md',
]

DOCS = 'docs'
FENCE = re.compile(r'^\s*```')
H2 = re.compile(r'^##\s+(.*?)\s*$')
LINK = re.compile(r'(\]\()([^)\s]+)((?:\s+"[^"]*")?\))')
SELF = re.compile(r'^https?://psx-spx\.consoledev\.net/([^/#]+)/(?:#(.*))?$')


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def h2_positions(lines):
    out, fenced = [], False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and (m := H2.match(line)):
            out.append((i, m.group(1)))
    return out


def plan_split(old, spec):
    """[(newfile, lines, added_title_or_None)] in reading order."""
    folder, mode, prefix = spec
    lines = open(os.path.join(DOCS, old), encoding='utf-8').read().split('\n')
    heads = h2_positions(lines)
    parts = []
    if mode == 'each':
        cuts = [(i, t) for i, t in heads]
        parts.append((f'{folder}/index.md', lines[:cuts[0][0]], None))
        names = set()
        for n, (i, title) in enumerate(cuts):
            end = cuts[n + 1][0] if n + 1 < len(cuts) else len(lines)
            name = slugify(title[len(prefix):] if prefix and title.startswith(prefix) else title)
            assert name and name not in names, (old, title)
            names.add(name)
            body = lines[i:end]
            body[0] = body[0][1:]               # '##   X' -> '#   X'
            parts.append((f'{folder}/{name}.md', body, None))
    else:
        starts = []
        for slug, title, first in mode:
            hit = [i for i, t in heads if t.startswith(first)]
            assert hit, (old, first)
            starts.append((hit[0], slug, title))
        assert starts == sorted(starts), old
        parts.append((f'{folder}/index.md', lines[:starts[0][0]], None))
        for n, (i, slug, title) in enumerate(starts):
            end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
            parts.append((f'{folder}/{slug}.md', [f'#   {title}', ''] + lines[i:end], title))
    # content check: undo the promotions and titles, and it is the page again
    flat = []
    for n, (_f, body, added) in enumerate(parts):
        if added:
            flat += body[2:]
        elif mode == 'each' and n:
            flat += ['#' + body[0]] + body[1:]
        else:
            flat += body
    assert flat == lines, f'{old}: split does not reassemble'
    return parts


def apply():
    origin, defaults, splitfiles = {}, {}, {}
    for old, new in MOVES.items():
        os.makedirs(os.path.dirname(os.path.join(DOCS, new)), exist_ok=True)
        subprocess.run(['git', 'mv', os.path.join(DOCS, old), os.path.join(DOCS, new)], check=True)
        if old.endswith('.md'):
            origin[new] = old
            defaults[old] = new
            splitfiles[old] = [(new, False)]
    for old, spec in SPLITS.items():
        parts = plan_split(old, spec)
        subprocess.run(['git', 'rm', '-q', os.path.join(DOCS, old)], check=True)
        splitfiles[old] = []
        for new, body, added in parts:
            path = os.path.join(DOCS, new)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(body).rstrip('\n') + '\n')
            origin[new] = old
            splitfiles[old].append((new, bool(added)))
        defaults[old] = parts[0][0]
    return origin, defaults, splitfiles


def url(md):
    d, b = os.path.split(md[:-3])
    return (d + '/' if d else '') if b == 'index' else md[:-3] + '/'


HEAD = re.compile(r'<h([1-6]) id="([^"]+)"[^>]*>(.*?)</h\1>', re.S)


def headings(site, md):
    html = open(os.path.join(site, url(md), 'index.html'), encoding='utf-8').read()
    art = html[html.index('<article'):html.index('</article>')]
    return [(i, re.sub(r'<[^>]+>|¶', '', t).strip()) for _l, i, t in HEAD.findall(art)]


def build(mkdocs, site):
    r = subprocess.run([mkdocs, 'build', '-q', '-d', site], capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    return r.stdout + r.stderr


def idmap(old_site, new_site, splitfiles):
    ids, redirects = {}, {}
    for old, files in splitfiles.items():
        before = headings(old_site, old)
        after = []
        for new, added in files:
            h = headings(new_site, new)
            after += [(new, i, t) for i, t in (h[1:] if added else h)]
        assert [t for _i, t in before] == [t for _n, _i, t in after], f'{old}: headings differ'
        m = {'': url(files[0][0])}
        for (oid, _t), (new, nid, _t2) in zip(before, after):
            ids[(old, oid)] = (new, nid)
            if len(files) > 1 or oid != nid:
                m[oid] = url(new) + '#' + nid
        redirects[old[:-3]] = m
    return ids, redirects


def rewrite(origin, defaults, ids):
    misses = []
    for new, old in origin.items():
        path = os.path.join(DOCS, new)
        lines = open(path, encoding='utf-8').read().split('\n')
        here = os.path.dirname(new)
        fenced = False

        def fix(m):
            t = m.group(2)
            s = SELF.match(t)
            if s:
                page, anchor = s.group(1) + '.md', s.group(2) or ''
                if page not in defaults:
                    return m.group(0)
                tgt, aid = ids.get((page, anchor), (defaults[page], anchor)) if anchor else (defaults[page], '')
                return m.group(1) + 'https://psx-spx.consoledev.net/' + url(tgt) + (
                    '#' + aid if aid else '') + m.group(3)
            if re.match(r'^[a-z]+:', t):
                return m.group(0)
            p, _, anchor = t.partition('#')
            page = os.path.normpath(os.path.join(os.path.dirname(old), p)) if p else old
            if page.endswith('.md'):
                if page not in defaults:
                    return m.group(0)
                if anchor:
                    if (page, anchor) not in ids:
                        misses.append(f'{new}: {t}')
                    tgt, aid = ids.get((page, anchor), (defaults[page], anchor))
                else:
                    tgt, aid = defaults[page], ''
            elif page in MOVES:
                tgt, aid = MOVES[page], anchor
            else:
                return m.group(0)
            rel = '' if tgt == new else os.path.relpath(tgt, here or '.')
            return m.group(1) + rel + ('#' + aid if aid else '') + m.group(3)

        for n, line in enumerate(lines):
            if FENCE.match(line):
                fenced = not fenced
            elif not fenced:
                lines[n] = LINK.sub(fix, line)
        with open(path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    return misses


def nav_yaml(splitfiles, defaults):
    out = []

    def entry(item, ind):
        pad = '  ' * ind
        if isinstance(item, str):
            files = splitfiles.get(item)
            if files and len(files) > 1:
                out.append(f'{pad}- {files[0][0]}')     # unreachable: splits sit under a titled dict
            else:
                out.append(f'{pad}- {defaults.get(item, item)}')
            return
        (title, body), = item.items()
        out.append(f'{pad}- {title}:')
        if isinstance(body, str):
            for new, _a in splitfiles[body]:
                out.append(f'{pad}  - {new}')
        else:
            for sub in body:
                entry(sub, ind + 1)

    for item in NAV:
        entry(item, 0)
    return '\n'.join(out) + '\n'


def main():
    old_site, mkdocs = sys.argv[1:3]
    origin, defaults, splitfiles = apply()
    for fn in STAYS:
        origin[fn] = fn
        defaults[fn] = fn
    cfg = open('mkdocs.yml', encoding='utf-8').read()
    cfg = cfg[:cfg.index('\nnav:\n')] + '\nnav:\n' + nav_yaml(splitfiles, defaults)
    open('mkdocs.yml', 'w', encoding='utf-8').write(cfg)
    new_site = old_site.rstrip('/') + '-new'
    build(mkdocs, new_site)
    moved = {k: v for k, v in splitfiles.items() if k not in ('index.md', 'aboutcredits.md')}
    ids, redirects = idmap(old_site, new_site, moved)
    for fn in STAYS:
        ids.update({(fn, i): (fn, i) for i, _t in headings(old_site, fn)})
    misses = rewrite(origin, defaults, ids)
    out = os.path.join('tools', 'redirects', 'map.json')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(redirects, f, indent=1, sort_keys=True)
        f.write('\n')
    print(f'{len(origin)} pages, {len(ids)} anchors mapped, {len(misses)} links to anchors '
          f'that did not exist before the move:')
    for m in misses:
        print('  ' + m)


if __name__ == '__main__':
    main()
