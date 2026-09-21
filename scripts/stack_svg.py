#!/usr/bin/env python3
"""The stack as an infinite ticker, scrolling right to left.

A GitHub README cannot carry CSS or JavaScript, so the motion has to live
inside an image. Same trick as the portrait plate: an SVG with a stylesheet.
The strip holds enough copies of the list to keep the window full, and the
translation is exactly one copy wide, so the loop has no seam.
"""
import math
import sys

from xml.sax.saxutils import escape

ITEMS = ["Python", "Go", "Django", "FastAPI", "PostgreSQL", "Docker",
         "PHP", "TypeScript", "React"]

CELL_W  = 9.0                 # monospace advance
FONT    = CELL_W / 0.6
PAD_X   = 13.0                # chip padding
GAP     = 10.0
CHIP_H  = 30.0
VIEW_W  = 660.0               # visible window, matches the portrait plate
VIEW_H  = 52.0
FADE    = 44.0                # edge fade width
SPEED   = 46.0                # pixels per second
OUT     = "assets/stack.svg"

INK_LIGHT, INK_DARK = "#1F2328", "#E6EDF3"
RULE_LIGHT, RULE_DARK = "#D0D7DE", "#3D444D"

def chip(label, x):
    w = len(label) * CELL_W + PAD_X * 2
    y = (VIEW_H - CHIP_H) / 2
    return (
        f'<rect class="k" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{CHIP_H:.0f}"/>'
        f'<text x="{x + PAD_X:.1f}" y="{VIEW_H / 2 + FONT * 0.35:.1f}"'
        f' textLength="{len(label) * CELL_W:.1f}" lengthAdjust="spacingAndGlyphs"'
        f'>{escape(label)}</text>'
    ), w

def build():
    seq_w = sum(len(i) * CELL_W + PAD_X * 2 + GAP for i in ITEMS)
    copies = math.ceil((VIEW_W + seq_w) / seq_w) + 1
    parts, x = [], 0.0
    for _ in range(copies):
        for label in ITEMS:
            markup, w = chip(label, x)
            parts.append(markup)
            x += w + GAP
    duration = seq_w / SPEED
    strip = ("\n" + " " * 6).join(parts)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEW_W:.0f} {VIEW_H:.0f}"
     width="{VIEW_W:.0f}" height="{VIEW_H:.0f}" role="img"
     aria-label="Stack, scrolling: {", ".join(ITEMS)}">
  <style>
    text {{
      font-family: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas,
                   "DejaVu Sans Mono", "Liberation Mono", monospace;
      font-size: {FONT:.2f}px;
      fill: {INK_LIGHT};
    }}
    .k {{ fill: none; stroke: {RULE_LIGHT}; stroke-width: 1; }}
    /* The strip sits at its start position when nothing animates, so the
       first items are readable even then. */
    .strip {{ animation: run {duration:.1f}s linear infinite; }}
    @keyframes run {{
      from {{ transform: translateX(0); }}
      to   {{ transform: translateX(-{seq_w:.1f}px); }}
    }}
    @media (prefers-color-scheme: dark) {{
      text {{ fill: {INK_DARK}; }}
      .k {{ stroke: {RULE_DARK}; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      .strip {{ animation: none; }}
    }}
  </style>
  <defs>
    <linearGradient id="fade" x1="0" x2="1">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="{FADE / VIEW_W:.3f}" stop-color="#fff" stop-opacity="1"/>
      <stop offset="{1 - FADE / VIEW_W:.3f}" stop-color="#fff" stop-opacity="1"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <mask id="edges"><rect width="{VIEW_W:.0f}" height="{VIEW_H:.0f}" fill="url(#fade)"/></mask>
  </defs>
  <g mask="url(#edges)">
    <g class="strip">
      {strip}
    </g>
  </g>
</svg>
'''

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT
    svg = build()
    open(out, "w").write(svg)
    print("wrote", out, len(svg), "bytes")
