#!/usr/bin/env python3
"""Turn the studio headshot into 1-bit dithered plates for the banners.

Floyd-Steinberg at the exact pixel size each banner renders it, so the pattern
stays crisp instead of turning to mush under a browser downscale.
"""
from pathlib import Path

from PIL import Image, ImageOps, ImageEnhance, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC  = "/home/mg/Downloads/Images/mimi.jpeg"
CROP = (104, 2, 408, 512)          # tall plate crop: ears kept, shoulders at the base
PLATES = [
    ("assets/portrait.png", (560, 966)),          # 280x483 CSS in banner.html at 2x
    ("assets/portrait-compact.png", (468, 852)),  # 234x426 CSS in banner-compact.html at 2x
]

def plate(size):
    im = Image.open(SRC).convert("L").crop(CROP)
    im = ImageOps.autocontrast(im, cutoff=1).resize(size, Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2.2, percent=115, threshold=3))
    im = ImageEnhance.Brightness(im).enhance(1.04)
    g = im.convert("1").convert("L")              # Floyd-Steinberg
    out = Image.new("RGB", size, (18, 17, 15))
    out.putalpha(g.point(lambda v: 255 - v))      # ink coverage as alpha
    return out

for path, size in PLATES:
    plate(size).save(ROOT / path)
    print("wrote", path, size)
