"""MkDocs hook: inline SVG figures so they follow the light/dark palette.

An image line on its own, ![alt](some/figure.svg), pointing at an SVG inside
docs/ is replaced by the SVG itself in a <div class="psx-figure">. Every colour
in the figure is then restyled from the theme's palette, keyed on the colour
it was drawn with, so a figure only has to be drawn in the palette below:

    #222 / black        text, box outlines       -> foreground
    #444 / #555         secondary text           -> foreground, light
    #888                tertiary text            -> foreground, lighter
    #ccc / #ddd         grid lines, shaded areas -> foreground, lightest
    #f6f8fa / #efefef / white   box fills        -> code background
    #1a7f37             signals and wires        -> --psx-fig-signal

Each themed element gets a class naming its role (pf-fill-fg, pf-stroke-signal,
...), and docs/css/extra.css colours those classes inside @media screen. The
original fill/stroke attributes stay in place, so the PDF, which is rendered
for print, keeps the colours the figure was drawn with. A colour not in the
table is left alone and reported in the build log.

Wired up in mkdocs.yml after the bitfield hook, which inserts image lines of
its own:

    hooks:
      - tools/bitfields/hook.py
      - tools/figures/hook.py
"""
import os
import re

MARKER = '</div><!-- psx-figure -->'

THEME = {
    '#222': 'fg',
    'black': 'fg',
    '#000': 'fg',
    '#444': 'light',
    '#555': 'light',
    '#888': 'lighter',
    '#ccc': 'lightest',
    '#ddd': 'lightest',
    '#f6f8fa': 'bg',
    '#efefef': 'bg',
    'white': 'bg',
    '#fff': 'bg',
    '#1a7f37': 'signal',
}

IMAGE = re.compile(r'^!\[(.*)\]\(([^)\s]+\.svg)\)\s*$')    # alt text may hold ]
TAG = re.compile(r'<([a-zA-Z]+)\b([^<>]*?)(/?)>')
PAINT = re.compile(r'\b(fill|stroke)="([^"]*)"')
ID = re.compile(r'\bid="([^"]+)"')


def _esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def _theme(svg, prefix, alt, unknown):
    # Inlined figures share one document: namespace their ids.
    for old in set(ID.findall(svg)):
        svg = svg.replace(f'id="{old}"', f'id="{prefix}-{old}"')
        svg = svg.replace(f'url(#{old})', f'url(#{prefix}-{old})')
        svg = svg.replace(f'href="#{old}"', f'href="#{prefix}-{old}"')

    def tag(m):
        name, attrs, close = m.groups()
        if name == 'svg':
            attrs = re.sub(r'\s*style="[^"]*"', '', attrs)
            if alt and 'aria-label=' not in attrs:
                attrs += f' aria-label="{_esc(alt)}"'
            return f'<svg{attrs}{close}>'
        roles = []
        for prop, colour in PAINT.findall(attrs):
            key = colour.strip().lower()
            if key in ('none', 'transparent') or key.startswith('url('):
                continue
            if key in THEME:
                roles.append(f'pf-{prop}-{THEME[key]}')
            else:
                unknown.add(colour)
        if roles and 'class=' not in attrs:
            attrs += f' class="{" ".join(roles)}"'
        return f'<{name}{attrs}{close}>'

    return TAG.sub(tag, svg)


def on_page_markdown(markdown, page, config, files):
    docs = config['docs_dir']
    here = os.path.dirname(page.file.src_path)
    lines, out, n, fence = markdown.split('\n'), [], 0, None
    for line in lines:
        # an image line inside a fenced block is an example, not a figure
        f = re.match(r'\s*(`{3,}|~{3,})', line)
        if f and (fence is None or f.group(1).startswith(fence)):
            fence = None if fence else f.group(1)[:3]
        m = fence is None and IMAGE.match(line)
        path = m and os.path.normpath(os.path.join(docs, here, m.group(2)))
        if not m or '://' in m.group(2) or not path.startswith(docs + os.sep) \
                or not os.path.isfile(path):
            out.append(line)
            continue
        n += 1
        unknown = set()
        name = os.path.splitext(os.path.basename(path))[0]
        svg = open(path, encoding='utf-8').read()
        svg = re.sub(r'<\?xml[^>]*\?>\s*', '', svg).strip()
        svg = _theme(svg, f'fig{n}-{re.sub(r"[^A-Za-z0-9-]", "-", name)}',
                     m.group(1), unknown)
        if unknown:
            print(f'WARNING -  Figure {m.group(2)} on {page.file.src_path}: colours '
                  f'not in the theme table, left as drawn: {", ".join(sorted(unknown))}')
        # No blank line after MARKER: the bitfield hook looks at the line just
        # above its table to stay idempotent across with-pdf's second pass.
        out += ['', '<div class="psx-figure">', svg, MARKER]
    return '\n'.join(out)
