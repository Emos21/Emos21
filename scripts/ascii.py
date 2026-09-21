#!/usr/bin/env python3
"""The portrait, drawn in code symbols.

60 columns. Rows are computed for a cell exactly twice as tall as it is wide,
which is the geometry scripts/portrait_svg.py then renders, so the face keeps
the proportions of the photograph instead of being stretched by whatever
line-height the viewer's stylesheet happens to use.
"""
import sys
from PIL import Image, ImageOps, ImageEnhance

SRC   = "/home/mg/Downloads/Images/mimi.jpeg"
CROP  = (98, 14, 414, 448)
COLS  = 60
CELL  = 2.0                    # cell height / cell width
RAMP  = "@%#*+=-:. "           # dark to light

def plate(crop=CROP, cols=COLS):
    im = Image.open(SRC).convert("L").crop(crop)
    im = ImageOps.autocontrast(im, cutoff=2)
    im = ImageEnhance.Contrast(im).enhance(1.25)
    rows = round(cols * im.height / im.width / CELL)
    im = im.resize((cols, rows), Image.LANCZOS)
    px = im.load()
    lines = ["".join(RAMP[min(len(RAMP) - 1, px[x, y] * len(RAMP) // 256)]
                     for x in range(cols)) for y in range(rows)]
    # drop the solid block where the black shirt saturates to one character
    while lines and lines[-1].count(RAMP[0]) > cols * 0.88:
        lines.pop()
    lines = [l.rstrip() for l in lines]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return lines

if __name__ == "__main__":
    print("\n".join(plate()))
