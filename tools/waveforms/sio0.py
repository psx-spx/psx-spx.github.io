#!/usr/bin/env python3
"""Draw the controller/memory card signal diagrams.

    python3 tools/waveforms/sio0.py

Writes docs/ps1/sio/controllersandmemorycards/waveforms/*.svg. The SVGs are
committed, nothing runs this at build time. Times are in arbitrary units.

A signal is a list of (time, state[, label]) change points. States: '1' and
'0' are logic levels, 'z' is high impedance, 'x' is don't care and 'd' is a
labelled value on a data line.
"""
import os

CW, RH, LW, TOP, T = 8, 34, 54, 10, 3
FONT = 'font-family="monospace" font-size="12"'
GREEN = '#1a7f37'
OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'ps1', 'sio',
                   'controllersandmemorycards', 'waveforms')


def segments(changes, start, end):
    seg = []
    for i, c in enumerate(changes):
        t1 = changes[i + 1][0] if i + 1 < len(changes) else end
        if t1 > start:
            seg.append((max(c[0], start), t1, c[1], c[2] if len(c) > 2 else ''))
    return seg


def bits(t, byte, period, n=8):
    return [(t + i * period, str((byte >> i) & 1)) for i in range(n)]


def digits(t, byte, period, n=8):
    return [(t + (i + 0.5) * period, str((byte >> i) & 1)) for i in range(n)]


def merge(changes):
    out = []
    for c in sorted(changes, key=lambda c: c[0]):
        if out and out[-1][1] == c[1] and c[1] in '01z':
            continue
        out.append(c)
    return out


def render(path, label, sigs, start, end, grid=()):
    W = LW + int((end - start) * CW) + 10
    H = TOP + len(sigs) * RH + 4
    x = lambda t: LW + (t - start) * CW
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
         f'viewBox="0 0 {W} {H}" style="max-width:100%;background-color:white" '
         f'role="img" aria-label="{label}">']
    for t in grid:
        o.append(f'<line x1="{x(t)}" y1="{TOP - 4}" x2="{x(t)}" y2="{H - 2}" '
                 f'stroke="#ddd" stroke-width="1"/>')
    for r, sig in enumerate(sigs):
        name, changes = sig[:2]
        notes = sig[2] if len(sig) > 2 else ()
        y0 = TOP + r * RH
        hi, lo = y0 + 6, y0 + RH - 8
        mid = (hi + lo) / 2
        lvl = {'1': hi, '0': lo, 'z': mid}
        o.append(f'<text x="4" y="{mid + 4}" {FONT} fill="black">{name}</text>')
        for t, txt in notes:
            o.append(f'<text x="{x(t)}" y="{mid + 4}" {FONT} text-anchor="middle" '
                     f'fill="#555">{txt}</text>')
        seg = segments(merge(changes), start, end)
        for i, (t0, t1, st, lab) in enumerate(seg):
            xa, xb = x(t0), x(t1)
            prev = seg[i - 1][2] if i else None
            nxt = seg[i + 1][2] if i + 1 < len(seg) else None
            if st in lvl:
                y = lvl[st]
                dash = ' stroke-dasharray="4 3"' if st == 'z' else ''
                o.append(f'<line x1="{xa}" y1="{y}" x2="{xb}" y2="{y}" '
                         f'stroke="{GREEN}" stroke-width="2"{dash}/>')
                if prev in lvl and lvl[prev] != y:
                    o.append(f'<line x1="{xa}" y1="{lvl[prev]}" x2="{xa}" y2="{y}" '
                             f'stroke="{GREEN}" stroke-width="2"/>')
                continue
            ly = lvl.get(prev, mid)
            ry = lvl.get(nxt, mid)
            pts = [(xa, ly), (xa + T, hi), (xb - T, hi), (xb, ry), (xb - T, lo), (xa + T, lo)]
            fill = '#ccc' if st == 'x' else 'white'
            o.append(f'<polygon fill="{fill}" stroke="{GREEN}" stroke-width="1.5" points="' +
                     ' '.join(f'{px},{py}' for px, py in pts) + '"/>')
            if lab:
                o.append(f'<text x="{(xa + xb) / 2}" y="{mid + 4}" {FONT} '
                         f'text-anchor="middle" fill="black">{lab}</text>')
    o.append('</svg>')
    with open(os.path.join(OUT, path), 'w') as f:
        f.write('\n'.join(o) + '\n')
    print(path, W, H)


def overview():
    starts = [14, 26, 38, 50, 62]
    sck = [(0, '1')]
    for s in starts:
        for i in range(8):
            sck += [(s + i, '0'), (s + i + 0.5, '1')]
    mosi = [(0, '1'), (12, 'x')]
    for s, lab in zip(starts, ['Addr', 'Cmd', 'Tap', 'Param', 'Param']):
        mosi += [(s, 'd', lab), (s + 8, 'x')]
    mosi.append((72, '1'))
    miso = [(0, 'z'), (23, 'x')]
    for s, lab in zip(starts[1:], ['IDlo', 'IDhi', 'Data', 'Data']):
        miso += [(s, 'd', lab), (s + 8, 'x')]
    miso.append((73, 'z'))
    ack = [(0, '1')]
    for s in starts[:-1]:
        ack += [(s + 9.5, '0'), (s + 11, '1')]
    render('overview.svg', 'controller packet overview', [
        ('/CS', [(0, '1'), (12, '0'), (72.5, '1')]),
        ('SCK', sck), ('MOSI', mosi), ('MISO', miso), ('/ACK', ack),
    ], 6, 79)


def address_byte():
    sck = [(0, '1')]
    for i in range(8):
        sck += [(13 + 4 * i, '0'), (15 + 4 * i, '1')]
    for i in range(5):
        sck += [(62 + 4 * i, '0'), (64 + 4 * i, '1')]
    render('address-byte.svg', 'address byte 01h being sent', [
        ('/CS', [(0, '1'), (12, '0')]),
        ('SCK', sck),
        ('MOSI', [(0, '1')] + bits(13, 0x01, 4) + bits(62, 0x42, 4, 5),
         digits(13, 0x01, 4) + digits(62, 0x42, 4, 5)),
        ('MISO', [(0, 'z'), (54, 'x')] + bits(62, 0x41, 4, 5), digits(62, 0x41, 4, 5)),
        ('/ACK', [(0, '1'), (54, '0'), (58, '1')]),
    ], 6, 82, grid=[13 + 4 * i for i in range(8)] + [62 + 4 * i for i in range(5)])


os.makedirs(OUT, exist_ok=True)
overview()
address_byte()
