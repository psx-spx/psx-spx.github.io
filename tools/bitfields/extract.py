#!/usr/bin/env python3
"""Find the register bit-layout tables in docs/ and parse them.

Used by the mkdocs hook, which draws them. Nothing is transcribed by hand: the
field names come straight out of the document text, so the diagrams cannot drift
away from the tables.

Blocks are rejected rather than guessed at. Run this directly with --report to
see what converts and, more usefully, what does not and why.
"""
import argparse
import glob
import os
import re

FIELD = re.compile(r'^ {0,6}(\d+)(?:\s*-\s*(\d+))?\s+(\S.*)$')
TRAILING_PAREN = re.compile(r'\s*\((?:[^()]|\([^()]*\))*\)\s*$')
BINARY = re.compile(r'^[01]{6,}$')
SYMBOL = re.compile(r'^([A-Z][A-Z0-9_]{1,7})\s+(\S.*)$')
FILLER = re.compile(r'^(garbage|not used|unused|unknown|reserved|zero|n/?a)\b', re.I)

WIDTHS = (8, 16, 24, 32, 64)
MIN_FIELDS = 3


class Reject(Exception):
    pass


def strip_xref(s):
    """Drop a trailing ';...' cross-reference.

    The semicolon has to be at paren depth zero: several lines read
    "(0=No, 1=Error; Wrong Parity, when enabled)", and cutting at the first ';'
    would leave an unbalanced parenthesis behind.
    """
    depth = 0
    for i, c in enumerate(s):
        if c == '(':
            depth += 1
        elif c == ')':
            depth = max(0, depth - 1)
        elif c == ';' and depth == 0:
            return s[:i]
    return s


def clean_label(raw):
    """Keep the field name, drop the cross-reference and the value enumeration."""
    s = strip_xref(raw).strip()
    prev = None
    while prev != s:                      # e.g. "Foo (0=a, 1=b) (R/W)"
        prev = s
        s = TRAILING_PAREN.sub('', s).strip()
    s = re.sub(r'^-\s+', '', s)           # bare "-" placeholder in the symbol column
    m = SYMBOL.match(s)
    if m and len(m.group(2)) > 3:         # "OPTM  Option Map Select" -> keep both
        s = f'{m.group(1)} {m.group(2)}'
    s = re.sub(r'\s+', ' ', s)
    return s.rstrip(' .,:-')


def parse_block(body):
    """Return (fields, register width), or raise Reject with the reason."""
    # A value-enumeration table ("Transfer Type 0..7", one row per value) has the
    # same shape as a bitfield list and must not be drawn as one. Two tells: a
    # ruler line of underscores, and a comma-separated list of values.
    for line in body:
        if re.search(r'_{3,}', line):
            raise Reject('ruler line - value table, not a bitfield')
        if re.match(r'^ {0,6}\d+(,\d+)+\s', line):
            raise Reject('comma-separated values - value table, not a bitfield')

    fields = []
    for line in body:
        m = FIELD.match(line)
        if not m:
            continue
        lo = int(m.group(1))
        hi = int(m.group(2)) if m.group(2) else lo
        label = m.group(3)
        if BINARY.match(label.split()[0]):
            raise Reject('binary-string table, not a bitfield')
        if hi < lo:
            lo, hi = hi, lo               # MSB-first notation, e.g. "31-29"
        fields.append((lo, hi, clean_label(label)))

    if len(fields) < MIN_FIELDS:
        raise Reject(f'only {len(fields)} fields')

    fields.sort()
    top = fields[-1][1]
    if top > 63:
        raise Reject('top bit beyond 64')
    for (_alo, ahi, _), (blo, _, _) in zip(fields, fields[1:]):
        if blo <= ahi:
            raise Reject('overlapping ranges')

    width = next((w for w in WIDTHS if top < w), None)
    if width is None:
        raise Reject('no standard width fits')

    covered = sum(hi - lo + 1 for lo, hi, _ in fields)
    if covered < width * 0.5:
        raise Reject(f'under half the bits described ({covered}/{width})')
    if fields[0][0] != 0:
        raise Reject('bit 0 not described - probably not a register layout')
    if not all(lab for _, _, lab in fields):
        raise Reject('a field has an empty label after cleanup')

    # The diagram is worth drawing when the register is a bit-packing, because
    # what it shows is where the flags sit. A register that is two 10bit
    # coordinates and some padding has nothing to show that the text does not
    # already say, so the picture would be decoration.
    informative = [(lo, hi) for lo, hi, lab in fields
                   if lab.strip() and not FILLER.match(lab.strip())]
    if not any(hi - lo + 1 <= 2 for lo, hi in informative):
        raise Reject('wide numeric layout - diagram adds nothing')

    return fields, width


def fill_gaps(fields, width):
    """Undescribed bits still occupy space in the register."""
    out, cur = [], 0
    for lo, hi, lab in fields:
        if lo > cur:
            out.append((cur, lo - 1, ''))
        out.append((lo, hi, lab))
        cur = hi + 1
    if cur < width:
        out.append((cur, width - 1, ''))
    return out


def slug(heading, seen):
    s = re.sub(r'[^A-Za-z0-9]+', '-', heading.lstrip('#').strip()).strip('-').lower()
    s = s[:52] or 'block'
    n, base = 2, s
    while s in seen:
        s = f'{base}-{n}'
        n += 1
    seen.add(s)
    return s


def blocks_for(page, text, rejects=None):
    """Yield (fence_line, name, heading, fields, width) for one document.

    Deterministic and self-contained, so every caller agrees on the names.
    """
    seen = set()
    lines = text.split('\n')
    heading = ''
    i = 0
    while i < len(lines):
        if lines[i].startswith('#'):
            heading = lines[i]
        if lines[i].startswith('```'):
            j = i + 1
            body = []
            while j < len(lines) and not lines[j].startswith('```'):
                body.append(lines[j])
                j += 1
            nonblank = [b for b in body if b.strip()]
            hits = [b for b in nonblank if FIELD.match(b)]
            if len(hits) >= 2 and len(hits) >= 0.6 * len(nonblank):
                try:
                    fields, width = parse_block(body)
                    yield i, f'{page}--{slug(heading, seen)}', heading, fields, width
                except Reject as e:
                    if rejects is not None:
                        rejects.setdefault(str(e), []).append(f'{page}:{i + 1}')
            i = j + 1
        else:
            i += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--docs', default='docs')
    ap.add_argument('--report', action='store_true',
                    help='list what was skipped and why')
    a = ap.parse_args()

    rejects, total = {}, 0
    for path in sorted(glob.glob(os.path.join(a.docs, '*.md'))):
        page = os.path.basename(path)[:-3]
        text = open(path, encoding='utf-8').read()
        total += sum(1 for _ in blocks_for(page, text, rejects))

    print(f'converted: {total}')
    print(f'skipped:   {sum(len(v) for v in rejects.values())}')
    if a.report:
        for reason, where in sorted(rejects.items(), key=lambda kv: -len(kv[1])):
            print(f'  {len(where):4d}  {reason}')
            for w in where[:3]:
                print(f'          {w}')


if __name__ == '__main__':
    main()
