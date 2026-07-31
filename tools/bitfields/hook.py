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
    return os.path.basename(src_path)[:-3]


def on_config(config):
    """Write the SVGs before mkdocs collects the file tree."""
    docs_dir = config['docs_dir']
    out_dir = os.path.join(docs_dir, SUBDIR)
    os.makedirs(out_dir, exist_ok=True)

    keep, count = set(), 0
    for fn in sorted(os.listdir(docs_dir)):
        if not fn.endswith('.md'):
            continue
        page = fn[:-3]
        text = open(os.path.join(docs_dir, fn), encoding='utf-8').read()
        for _line, name, _heading, fields, width in extract.blocks_for(page, text):
            svg = render.render(extract.fill_gaps(fields, width), width)
            with open(os.path.join(out_dir, name + '.svg'), 'w', encoding='utf-8') as f:
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
    if os.path.dirname(page.file.src_path):
        return markdown                     # only top-level pages carry registers

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
        lines.insert(line, f'![{alt} - bit layout]({SUBDIR}/{diagram}.svg)')
    return '\n'.join(lines)
