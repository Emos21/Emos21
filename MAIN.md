# Operating this repo

## Where it lives

| | |
|---|---|
| Remote | `https://github.com/Emos21/Emos21` (public), branch `master` |
| Live page | https://github.com/Emos21 |
| Working copy | `~/Desktop/github-profile` |
| Source photograph | `~/Downloads/Images/mimi.jpeg` (not committed) |

Publishing is `git push origin master`. GitHub picks up the README immediately.

## Regenerating the portrait

```bash
python3 scripts/ascii.py > assets/portrait.txt
PYTHONPATH=scripts python3 scripts/portrait_svg.py
```

`scripts/ascii.py` crops the photograph, corrects for a monospace cell being roughly twice
as tall as it is wide, maps brightness onto the ramp `@%#*+=-:.` and trims the solid block
where the black shirt saturates to a single character. Output is 60 columns and 37 lines.

`scripts/portrait_svg.py` then sets that text as one `<text>` element per line, each with a
`textLength` that pins the row to exactly 60 cells so no font substitution can change the
proportions, and a cell twice as tall as it is wide. Rows carry staggered
`animation-delay`s 55ms apart, so the plate prints top to bottom in about two seconds and a
cursor blinks underneath. Output: `assets/portrait.svg`, which the README embeds at 660px.

The hidden state of a row comes from `animation-fill-mode: both`, never from `opacity: 0` in
a base rule. That way an environment that runs no animation still shows the whole portrait.

Requirements: `python3` with Pillow. Nothing else, and no browser.

## Regenerating the stack ticker

```bash
python3 scripts/stack_svg.py
```

Edit `ITEMS` at the top of the script to change the list. The script lays the chips out in
a strip, repeats the strip until it is wider than the 660px window plus one full sequence,
and animates the group by exactly one sequence width, which is what makes the loop
seamless. Speed is `SPEED`, in pixels per second; duration is derived, so adding items
changes the cycle length and not the pace. A gradient mask fades both edges, measured at
ink 241 at x=2, 0 by x=44, and 247 at x=658.

## Checks

```bash
tests/check.sh
```

Verifies the README has no emojis and no em dashes, that it loads no raster image, that the
plate is 60 columns or narrower, that the ticker carries every named item with enough
copies for a seamless loop, that `assets/portrait.txt` and `assets/portrait.svg` both
still match their generators, that the SVG carries every row, its reduced-motion and
dark-scheme rules, and no row that starts invisible, and that every outbound link answers.
LinkedIn answers `999` to anything that is not a browser; the check treats that as
reachable.

Run it before every push. The profile is the first thing a recruiter sees, so a broken
link is the whole cost of the page.

## Deploy state

Live as of 2026-09-22: README led by the animated character plate, then the five highlighted
systems (Arizona Sunshine, ClearDD, ProcureCrawl, Extreme POS, Classy Carry), the stack as a
scrolling ticker over the stack table, four verified figures, and contact. The shields.io
badges are gone; nothing on the page is fetched from a third party. Two earlier shapes were rejected on the way: a dithered
photograph set as a printed plate, and the plate as a fenced code block, which inherited the
viewer's line-height and stretched the face.

Browser-verified on 2026-09-22 with Playwright: at animation time 0 no row is painted, the
first row lands at 600ms, the last at about 2s; `prefers-reduced-motion: reduce` returns
`animation-name: none` with every row at full opacity; `prefers-color-scheme: dark` computes
the ink as `rgb(230, 237, 243)`.
