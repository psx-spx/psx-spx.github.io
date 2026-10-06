#!/usr/bin/env python3
"""Draw the CD-ROM subsystem block diagrams.

    python3 tools/diagrams/cdrom.py

Writes docs/ps1/cdr/diagrams/*.svg. The SVGs are committed, nothing runs this
at build time. A box is (x, y, w, h, title, subtitle lines...). A wire is
(points, style, label, label x, label y[, anchor]): the points are joined in
order, style is '>' for an arrow at the last point, '<>' for arrows at both
ends and '-' for none.
"""
import os

FONT = 'font-family="monospace"'
INK = '#222'
GREEN = '#1a7f37'
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'ps1', 'cdr',
                   'diagrams')


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render(path, label, boxes, wires, W, H):
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" style="max-width:100%;background-color:white" '
         f'role="img" aria-label="{esc(label)}">',
         '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
         'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" '
         f'fill="{GREEN}"/></marker></defs>']
    for pts, style, text, lx, ly, *anchor in wires:
        marks = {'>': ' marker-end="url(#a)"',
                 '<>': ' marker-start="url(#a)" marker-end="url(#a)"', '-': ''}[style]
        o.append('<polyline fill="none" points="' + ' '.join(f'{x},{y}' for x, y in pts) +
                 f'" stroke="{GREEN}" stroke-width="2"{marks}/>')
        for i, line in enumerate(text.split('\n')):
            o.append(f'<text x="{lx}" y="{ly + i * 14}" {FONT} font-size="11" '
                     f'text-anchor="{anchor[0] if anchor else "middle"}" '
                     f'fill="#444">{esc(line)}</text>')
    for x, y, w, h, title, *sub in boxes:
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" '
                 f'fill="#f6f8fa" stroke="{INK}" stroke-width="1.5"/>')
        o.append(f'<text x="{x + w / 2}" y="{y + 18}" {FONT} font-size="13" '
                 f'font-weight="bold" text-anchor="middle" fill="{INK}">{esc(title)}</text>')
        for i, line in enumerate(sub):
            o.append(f'<text x="{x + w / 2}" y="{y + 34 + i * 14}" {FONT} font-size="11" '
                     f'text-anchor="middle" fill="#444">{esc(line)}</text>')
    o.append('</svg>')
    with open(os.path.join(OUT, path), 'w') as f:
        f.write('\n'.join(o) + '\n')
    print(path, W, H)


def separate():
    boxes = [
        (20, 30, 150, 80, 'CPU', 'CXD8606Q'),
        (320, 30, 190, 80, 'Decoder', 'CXD1815Q', 'sector buffer, ECC,', 'XA-ADPCM, volume'),
        (640, 40, 130, 60, 'Sector SRAM', '32Kx8'),
        (20, 230, 150, 60, 'SPU', 'CXD2925Q'),
        (320, 230, 190, 70, 'Mechacon', 'MC68HC05', 'firmware in ROM'),
        (640, 230, 130, 70, 'DSP', 'CXD2545Q', 'EFM, C1/C2, SubQ'),
        (840, 240, 130, 50, 'Motor driver', 'BA6392FP'),
        (640, 400, 130, 50, 'RF amplifier', 'CXA1791N'),
    ]
    wires = [
        ([(170, 50), (320, 50)], '<>', 'host bus', 245, 44),
        ([(320, 70), (170, 70)], '>', 'IRQ2', 245, 64),
        ([(320, 95), (245, 95), (245, 260), (170, 260)], '>', 'CD audio (I2S)', 252, 210,
         'start'),
        ([(510, 70), (640, 70)], '<>', 'sectors', 575, 64),
        ([(415, 110), (415, 230)], '<>', 'register bus,\nXINT', 408, 166, 'end'),
        ([(680, 230), (680, 170), (480, 170), (480, 110)], '>', 'data, C2 flags', 580, 164),
        ([(510, 255), (640, 255)], '>', 'commands', 575, 249),
        ([(640, 280), (510, 280)], '>', 'SubQ', 575, 296),
        ([(770, 265), (840, 265)], '>', 'servo', 805, 259),
        ([(705, 400), (705, 300)], '>', 'RF', 712, 354, 'start'),
        ([(415, 300), (415, 425), (640, 425)], '>', 'laser on', 527, 419),
    ]
    render('cdrom-separate.svg', 'CD subsystem with separate chips (PU-18)', boxes, wires,
           990, 470)


def combined():
    boxes = [
        (20, 30, 150, 80, 'CPU'),
        (320, 30, 230, 100, 'Combo chip', 'CXD2938Q / CXD2941R', 'decoder + DSP + SPU',
         'internal links unknown'),
        (680, 50, 130, 50, 'Sector SRAM'),
        (320, 240, 230, 60, 'Mechacon', 'MC68HC05'),
    ]
    wires = [
        ([(170, 50), (320, 50)], '<>', 'host bus', 245, 44),
        ([(320, 70), (170, 70)], '>', 'IRQ2', 245, 64),
        ([(550, 75), (680, 75)], '<>', 'sectors', 615, 69),
        ([(435, 130), (435, 240)], '<>', 'register bus,\ncommands, SubQ', 442, 182, 'start'),
    ]
    render('cdrom-combined.svg', 'CD subsystem with a combined chip (SCPH-7500 and later)',
           boxes, wires, 830, 320)


os.makedirs(OUT, exist_ok=True)
separate()
combined()
