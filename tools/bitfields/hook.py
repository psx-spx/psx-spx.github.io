"""MkDocs hook: draw a bit-layout diagram above each register table.

Everything is generated at build time from the tables themselves, so there is
nothing committed to go stale and nothing to remember to regenerate. Pure
Python - no node, no browser - so the deploy action needs no extra machinery.

Wired up in mkdocs.yml as:

    hooks:
      - tools/bitfields/hook.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import extract          # noqa: E402
import render           # noqa: E402

SUBDIR = 'diagrams'


def _page_name(src_path):
    # 'ps1/gpu/timings.md' -> 'ps1-gpu-timings', unique across the tree
    return src_path.replace(os.sep, '/')[:-3].replace('/', '-')


def _pages(docs_dir):
    for root, dirs, files in os.walk(docs_dir):
        dirs[:] = sorted(d for d in dirs if d != SUBDIR)
        for fn in sorted(files):
            if fn.endswith('.md'):
                path = os.path.join(root, fn)
                yield _page_name(os.path.relpath(path, docs_dir)), path


def on_config(config):
    """Write the SVGs before mkdocs collects the file tree."""
    docs_dir = config['docs_dir']
    out_dir = os.path.join(docs_dir, SUBDIR)
    os.makedirs(out_dir, exist_ok=True)

    keep, count = set(), 0
    for page, path in _pages(docs_dir):
        text = open(path, encoding='utf-8').read()
        for _line, name, _heading, fields, width in extract.blocks_for(page, text):
            svg = render.render(extract.fill_gaps(fields, width), width)
            out = os.path.join(out_dir, name + '.svg')
            try:
                same = open(out, encoding='utf-8').read() == svg
            except OSError:
                same = False
            if not same:
                with open(out, 'w', encoding='utf-8') as f:
                    f.write(svg)
            keep.add(name + '.svg')
            count += 1

    for fn in os.listdir(out_dir):          # a block that no longer converts
        if fn.endswith('.svg') and fn not in keep:
            os.remove(os.path.join(out_dir, fn))

    print(f'INFO    -  Bitfield diagrams: generated {count}')
    return config


def on_page_markdown(markdown, page, config, files):
    name = _page_name(page.file.src_path)
    up = '../' * page.file.src_path.replace(os.sep, '/').count('/')
    inserts = list(extract.blocks_for(name, markdown))
    if not inserts:
        return markdown

    lines = markdown.split('\n')
    for line, diagram, heading, _fields, _width in reversed(inserts):
        # with-pdf runs the page through the markdown pipeline a second time, so
        # this has to be idempotent: inserting again would shift every following
        # fence and land the second copy inside a code block.
        if line and lines[line - 1].startswith('!['):
            continue
        alt = heading.lstrip('#').strip() or 'bit layout'
        lines.insert(line, f'![{alt} - bit layout]({up}{SUBDIR}/{diagram}.svg)')
    return '\n'.join(lines)
