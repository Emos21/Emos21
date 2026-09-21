#!/usr/bin/env python3
"""Same headshot, rendered as text. 60 columns, aspect-corrected for a 1:2 cell."""
from PIL import Image, ImageOps, ImageEnhance

SRC   = "/home/mg/Downloads/Images/mimi.jpeg"
CROP  = (98, 14, 414, 448)
COLS  = 80
RAMP  = "@%#*+=-:. "          # dark -> light

im = Image.open(SRC).convert("L").crop(CROP)
im = ImageOps.autocontrast(im, cutoff=2)
im = ImageEnhance.Contrast(im).enhance(1.25)
rows = int(COLS * im.height / im.width * 0.5)
im = im.resize((COLS, rows), Image.LANCZOS)
px = im.load()
lines = ["".join(RAMP[min(len(RAMP) - 1, px[x, y] * len(RAMP) // 256)]
                 for x in range(COLS)) for y in range(rows)]
# drop the solid block where the black shirt saturates to one character
while lines and lines[-1].count(RAMP[0]) > COLS * 0.88:
    lines.pop()
print("\n".join(l.rstrip() for l in lines))
