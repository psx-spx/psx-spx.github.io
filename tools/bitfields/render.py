#!/usr/bin/env python3
"""Draw a register bit-layout as plain SVG.

Written by hand rather than through mermaid, because the diagram is rectangles
on a linear grid with rotated labels, and going through a headless browser to
place them would put node and chromium in the deploy path for no gain.

Conventions, all deliberate:
  - bit 0 on the RIGHT, the way hardware documentation draws it
  - field names rotated 90 degrees, so a 1-bit field can still carry a real name
  - don't-care runs drawn narrow, with the bit numbers still marking the true
    extent, the way a datasheet draws a break
  - every colour and transform is a presentation attribute and there is no
    stylesheet, so WeasyPrint renders it in the PDF exactly as a browser does
"""
import re

FILLER = re.compile(r'^(garbage|not used|unused|unknown|reserved|zero|n/?a)\b', re.I)

TARGET_PX = 770         # nominal full-width register
MAX_FILLER_BITS = 3     # widest a don't-care run is ever drawn
MAX_LABEL = 44          # characters that fit vertically in MAX_ROW
MAX_ROW = 320
MIN_ROW = 90
GAP = 5                 # gap between adjacent field boxes
NUM_H = 15              # height of the bit-number strip
FONT = ('"Trebuchet MS", Verdana, Arial, Helvetica, sans-serif')
LABEL_PX = 12
NUM_PX = 10
FILL = '#efefef'
STROKE = 'black'


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def shorten(lab):
    """The full text is in the block right below the diagram."""
    if len(lab) <= MAX_LABEL:
        return lab
    cut = lab[:MAX_LABEL - 3]
    if ' ' in cut[30:]:
        cut = cut[:cut.rindex(' ')]
    return cut.rstrip(' .,:-') + '...'


def is_filler(lab):
    return not lab.strip() or bool(FILLER.match(lab.strip()))


def render(fields, width):
    """fields: sorted [(lo, hi, label)] covering 0..width-1. Returns SVG text."""
    labels = [shorten(l) for _, _, l in fields]
    longest = max((len(l) for l in labels), default=0)
    row_h = max(MIN_ROW, min(MAX_ROW, int(longest * 6.6) + 26))
    pitch = max(10, round(TARGET_PX / width))

    # how many columns each field is actually drawn as
    drawn = [min(hi - lo + 1, MAX_FILLER_BITS) if is_filler(lab) else hi - lo + 1
             for lo, hi, lab in fields]
    total = sum(drawn)
    svg_w = total * pitch + 1
    svg_h = NUM_H + row_h + 1

    # lay out right to left so bit 0 lands on the right edge
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" '
           f'height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}" '
           f'style="max-width: 100%; background-color: white;" '
           f'role="img" aria-label="register bit layout">']

    cursor = svg_w - 1                       # right edge, walking leftwards
    for (lo, hi, _raw), lab, cols in zip(fields, labels, drawn):
        w = cols * pitch - GAP
        x = cursor - cols * pitch + GAP
        cx, cy = x + w / 2, NUM_H + row_h / 2

        out.append(f'<rect x="{x:g}" y="{NUM_H}" width="{w:g}" height="{row_h}" '
                   f'fill="{FILL}" stroke="{STROKE}" stroke-width="1"/>')
        if lab.strip():
            out.append(
                f'<text x="{cx:g}" y="{cy:g}" font-family={FONT!r} '
                f'font-size="{LABEL_PX}" fill="black" text-anchor="middle" '
                f'dominant-baseline="middle" '
                f'transform="rotate(-90,{cx:g},{cy:g})">{esc(lab)}</text>')

        # bit numbers: high bit at the box's left edge, low bit at its right
        ny = NUM_H - 3
        out.append(f'<text x="{x:g}" y="{ny}" font-family={FONT!r} '
                   f'font-size="{NUM_PX}" fill="black" '
                   f'text-anchor="start">{hi}</text>')
        if hi != lo:
            out.append(f'<text x="{x + w:g}" y="{ny}" font-family={FONT!r} '
                       f'font-size="{NUM_PX}" fill="black" '
                       f'text-anchor="end">{lo}</text>')
        cursor -= cols * pitch

    out.append('</svg>')
    return '\n'.join(out) + '\n'
