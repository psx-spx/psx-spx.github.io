#!/usr/bin/env python3
"""Draw how interrupt requests reach the CPU.

    python3 tools/diagrams/interrupts.py

Writes docs/ps1/system/diagrams/interrupt-chain.svg. The SVG is committed,
nothing runs this at build time. Boxes and wires follow tools/diagrams/cdrom.py;
a note is (x, y, text) in the dimmer text colour.
"""
import os

FONT = 'font-family="monospace"'
INK = '#222'
DIM = '#555'
GREEN = '#1a7f37'
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'ps1', 'system',
                   'diagrams')


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def render(path, label, boxes, wires, notes, W, H):
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
        for i, line in enumerate(text.split('\n') if text else []):
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
    for x, y, text in notes:
        o.append(f'<text x="{x}" y="{y}" {FONT} font-size="11" text-anchor="middle" '
                 f'fill="{DIM}">{esc(text)}</text>')
    o.append('</svg>')
    with open(os.path.join(OUT, path), 'w') as f:
        f.write('\n'.join(o) + '\n')
    print(path, W, H)


def chain():
    boxes = [
        (20, 20, 180, 120, 'IRQ sources', 'VBLANK, GPU, CDROM,', 'DMA, TMR0-2,',
         'controller/memcard,', 'SIO, SPU,', 'lightpen/PIO'),
        (250, 40, 140, 70, 'I_STAT', '1F801070h', 'edge latch'),
        (440, 40, 140, 70, 'AND I_MASK', '1F801074h', 'per device'),
        (630, 40, 120, 70, 'OR', '11 bits -> 1'),
        (800, 40, 180, 70, 'CAUSE IP10', 'hardware line 0', 'no latch'),
        (800, 200, 180, 60, 'AND SR.IM10', 'master gate'),
        (20, 200, 180, 60, 'CAUSE IP8-9', 'software, R/W'),
        (250, 200, 140, 60, 'AND SR.IM8-9'),
        (560, 200, 140, 60, 'OR'),
        (560, 320, 140, 60, 'AND SR.IEc'),
        (800, 320, 180, 60, 'Exception', 'ExcCode 0, INT'),
    ]
    wires = [
        ([(200, 75), (250, 75)], '>', '', 0, 0),
        ([(390, 75), (440, 75)], '>', '', 0, 0),
        ([(580, 75), (630, 75)], '>', '', 0, 0),
        ([(750, 75), (800, 75)], '>', '', 0, 0),
        ([(890, 110), (890, 200)], '>', '', 0, 0),
        ([(800, 230), (700, 230)], '>', '', 0, 0),
        ([(200, 230), (250, 230)], '>', '', 0, 0),
        ([(390, 230), (560, 230)], '>', '', 0, 0),
        ([(630, 260), (630, 320)], '>', '', 0, 0),
        ([(700, 350), (800, 350)], '>', '', 0, 0),
    ]
    notes = [
        (770, 145, 'IP11-15 (lines 1-5):'),
        (770, 159, 'not connected, read 0'),
        (315, 75 + 50, 'write 0 to acknowledge'),
    ]
    render('interrupt-chain.svg', 'Interrupt requests from I_STAT to the CPU exception',
           boxes, wires, notes, 1000, 400)


os.makedirs(OUT, exist_ok=True)
chain()
