#!/usr/bin/env python3
"""Export the block diagrams in ps1-blocks.drawio to SVG.

    DRAWIO=/path/to/drawio python3 tools/diagrams/drawio.py

Needs the draw.io desktop app (the AppImage works headless under xvfb-run,
which this script uses when $DISPLAY is unset). Each page of the .drawio file
becomes one SVG, written where PAGES says. The SVGs are committed, nothing runs
this at build time.

draw.io writes labels as HTML inside <foreignObject>, which WeasyPrint cannot
draw; with --theme light it also writes a plain <text> fallback, which is kept
and the HTML dropped. The diagrams are drawn in black on white, and the colours
are mapped onto the palette tools/figures/hook.py themes: boxes get the shaded
fill, wires and arrowheads the signal colour, dashed outlines the light grey.
"""
import os
import re
import shutil
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, '..', '..', 'docs')
SOURCE = os.path.join(HERE, 'ps1-blocks.drawio')

# page name in the .drawio file -> output path under docs/
PAGES = {
    'cpu-soc': 'ps1/cpu/diagrams/cpu-soc.svg',
    'gpu-v0': 'ps1/gpu/diagrams/gpu-v0.svg',
    'gpu-v2': 'ps1/gpu/diagrams/gpu-v2.svg',
    'mdec': 'ps1/cpu/mdec/diagrams/mdec.svg',
    'spu': 'ps1/spu/diagrams/spu.svg',
    'cdrom': 'ps1/cdr/diagrams/cdrom-blocks.svg',
}

INK, NOTE, DIM, FILL, SIGNAL = '#222', '#444', '#888', '#f6f8fa', '#1a7f37'


def pages(path):
    return re.findall(r'<diagram\b[^>]*\bname="([^"]*)"', open(path).read())


def export(drawio, src, index, out):
    cmd = [drawio, '--no-sandbox', '--disable-gpu', '-x', '-f', 'svg', '--theme', 'light',
           '--embed-svg-fonts', 'false', '-p', str(index), '-o', out, src]
    if not os.environ.get('DISPLAY'):
        cmd = ['xvfb-run', '-a'] + cmd
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def element(m):
    name, attrs, close = m.groups()
    attrs = re.sub(r'\s+(style|pointer-events|id|data-cell-id)="[^"]*"', '', attrs)
    fill = re.search(r'\bfill="([^"]*)"', attrs)
    fill = fill and fill.group(1).lower()
    dashed = 'stroke-dasharray' in attrs

    def paint(prop, colour):
        nonlocal attrs
        # an unpainted side (a label with no border) stays unpainted
        attrs = re.sub(rf'\b{prop}="(?!none")[^"]*"', f'{prop}="{colour}"', attrs)

    if name == 'text':
        paint('fill', INK)
    elif name in ('rect', 'ellipse'):
        paint('stroke', DIM if dashed else INK)
        if fill == '#ffffff' and 'stroke="none"' in attrs:
            paint('fill', 'none')                          # a bare label's background
        elif fill == '#ffffff':
            paint('fill', FILL)
        elif fill == '#000000':
            paint('fill', INK)                             # the dots in an ellipsis
    elif name == 'path':
        if fill in (None, 'none'):
            paint('stroke', DIM if dashed else SIGNAL)     # a wire, or a dashed outline
        elif fill == '#000000':
            paint('fill', SIGNAL)                          # an arrowhead
            paint('stroke', SIGNAL)
        elif fill == '#ffffff':
            paint('fill', FILL)
            paint('stroke', INK)
    return f'<{name}{attrs}{close}>'


def convert(svg, label):
    svg = re.sub(r'<\?xml[^>]*\?>\s*|<!DOCTYPE[^>]*>\s*', '', svg)
    svg = re.sub(r'<style[^>]*>.*?</style>', '', svg, flags=re.S)
    # keep the <text> fallback of every label, drop the HTML
    svg = re.sub(r'<switch><foreignObject\b.*?</foreignObject>(.*?)</switch>', r'\1', svg,
                 flags=re.S)
    # and the "Text is not SVG" notice draw.io appends for viewers without HTML
    svg = re.sub(r'<switch><g requiredFeatures="[^"]*"/><a\b.*?</a></switch>', '', svg,
                 flags=re.S)
    svg = re.sub(r'<svg\b[^>]*>', lambda m: re.sub(
        r'\s+(style|id|xmlns:xlink|version)="[^"]*"', '', m.group(0)).replace(
        '>', f' role="img" aria-label="{label}">', 1), svg, count=1)
    svg = re.sub(r'<(?!svg\b)([a-zA-Z]+)\b([^<>]*?)(/?)>', element, svg)
    svg = re.sub(r'<g>\s*</g>', '', svg)
    if 'foreignObject' in svg:
        raise SystemExit('a label had no <text> fallback')
    return svg.strip() + '\n'


def main():
    drawio = os.environ.get('DRAWIO') or shutil.which('drawio')
    if not drawio:
        raise SystemExit('set DRAWIO to the draw.io desktop binary')
    names = pages(SOURCE)
    # RAW_DIR keeps draw.io's own exports and reuses them, which saves the slow
    # step when only the conversion below has changed.
    keep = os.environ.get('RAW_DIR')
    with tempfile.TemporaryDirectory() as tmp:
        for name, rel in PAGES.items():
            if name not in names:
                raise SystemExit(f'page {name!r} is not in {SOURCE}')
            raw = os.path.join(keep or tmp, name + '.svg')
            if not (keep and os.path.exists(raw)):
                export(drawio, SOURCE, names.index(name) + 1, raw)     # pages count from 1
            out = os.path.join(DOCS, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            with open(out, 'w') as f:
                f.write(convert(open(raw).read(), f'{name} block diagram'))
            print(rel)
    for name in names:
        if name not in PAGES:
            print(f'not exported (no entry in PAGES): {name}')


if __name__ == '__main__':
    main()
