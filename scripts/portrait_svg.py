#!/usr/bin/env python3
"""Render the code-symbol portrait as an animated SVG.

Why an SVG and not a fenced code block: the block inherits the viewer's
line-height, which stretched the plate vertically and made the face look thin,
and it paints a grey panel behind the characters. Here the cell is exactly
CELL_W by CELL_H, the background is nothing at all, and the plate can print
itself one line at a time the way a terminal would.

The characters are still the artwork. assets/portrait.txt stays the source.
"""
import sys
from xml.sax.saxutils import escape

from ascii import plate, COLS, CELL

CELL_W   = 14.0
CELL_H   = CELL_W * CELL          # cell exactly twice as tall as it is wide
PAD      = 10.0
STEP     = 0.055                  # seconds between printed lines
DISPLAY_W = 660                   # rendered width in the README
OUT      = "assets/portrait.svg"

INK_LIGHT, INK_DARK, ACCENT = "#1F2328", "#E6EDF3", "#B3352A"

def build():
    lines = plate()
    w = COLS * CELL_W + PAD * 2
    h = (len(lines) + 1) * CELL_H + PAD * 2      # one spare row for the prompt
    last = STEP * len(lines)

    rows = []
    for i, line in enumerate(lines):
        y = PAD + (i + 1) * CELL_H - CELL_H * 0.26
        rows.append(
            f'<text class="r" x="{PAD:.0f}" y="{y:.1f}" textLength="{COLS * CELL_W:.0f}"'
            f' lengthAdjust="spacingAndGlyphs" xml:space="preserve"'
            f' style="animation-delay:{i * STEP:.3f}s">{escape(line.ljust(COLS))}</text>'
        )
    py = PAD + (len(lines) + 1) * CELL_H - CELL_H * 0.26
    prompt = (
        f'<text class="p" x="{PAD:.0f}" y="{py:.1f}" xml:space="preserve"'
        f' style="animation-delay:{last:.3f}s">$ </text>'
        f'<rect class="c" x="{PAD + CELL_W * 2:.1f}" y="{py - CELL_H * 0.62:.1f}"'
        f' width="{CELL_W * 0.78:.1f}" height="{CELL_H * 0.62:.1f}"'
        f' style="animation-delay:{last:.3f}s"/>'
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}"
     width="{DISPLAY_W}" height="{DISPLAY_W * h / w:.0f}" role="img"
     aria-label="Portrait of Amos Mwangi drawn in code symbols, printed line by line">
  <style>
    text {{
      font-family: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas,
                   "DejaVu Sans Mono", "Liberation Mono", monospace;
      font-size: {CELL_W / 0.6:.2f}px;
      white-space: pre;
      fill: {INK_LIGHT};
    }}
    /* No element is hidden by default: if animations never run, the plate is
       still whole. The backwards fill is what hides a line before its turn. */
    .r, .p {{ animation: print 1ms linear both; }}
    .c {{ fill: {ACCENT}; animation: blink 1.06s steps(1, end) infinite both; }}
    @keyframes print {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes blink {{ 0%, 49.9% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    @media (prefers-color-scheme: dark) {{ text {{ fill: {INK_DARK}; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .r, .p, .c {{ opacity: 1; animation: none; }}
    }}
  </style>
{chr(10).join("  " + r for r in rows)}
  {prompt}
</svg>
'''

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else OUT
    svg = build()
    open(out, "w").write(svg)
    print("wrote", out, len(svg), "bytes")
