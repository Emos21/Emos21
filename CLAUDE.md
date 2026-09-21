# Emos21/Emos21

The GitHub profile README for Amos Mwangi. The rendered `README.md` at the repo root is
what appears above the pinned repositories at github.com/Emos21, so this repo is a
publishing surface, not an application.

## What it is

- `README.md` is the profile page. Everything else exists to produce it.
- The portrait at the top is **characters, not a photograph**. `scripts/ascii.py` turns the
  source photo into 60 columns of text (`assets/portrait.txt`), and
  `scripts/portrait_svg.py` sets that text in an SVG that prints itself one line at a time
  and holds a cursor at the end. A picture drawn in code symbols is the point of the page; a
  photograph, or a dithered plate of one, is not.
- No PNG, JPEG or GIF belongs in this repo. `assets/portrait.svg` is type, not a bitmap: it
  is the same characters, with the cell geometry fixed so a stylesheet cannot stretch the
  face. `assets/stack.svg` is the stack as an infinite ticker, also type and hairlines. The
  README loads nothing from a third party: both images are in this repo.

## Rules

- **The portrait stays characters.** 60 columns, from `scripts/ascii.py`. Change the crop or
  the ramp and both `assets/portrait.txt` and `assets/portrait.svg` must be regenerated;
  `tests/check.sh` fails when they drift apart.
- **Motion has gates.** The plate must be whole when no animation runs, so no row may start
  at `opacity: 0`; the hidden state comes from a backwards fill. `prefers-reduced-motion:
  reduce` shows everything at once, and `prefers-color-scheme: dark` switches the ink. All
  three are asserted by the checks.
- **Two motions, ranked.** The plate printing itself is the signature and it runs once. The
  stack ticker is the quiet secondary: hairline chips, low contrast, 46 pixels a second, so
  it reads as drift rather than as a demand for attention. Nothing else moves.
- **Motion lives inside the images.** A README carries no CSS and no JavaScript, so any
  animation has to be a stylesheet inside an SVG. That is the only mechanism available and
  the reason both assets are SVG rather than markdown.
- **Every claim is verifiable.** Numbers come from the GitHub API, from a repository, or
  from a system that is actually in production. Nothing is estimated upward, and nothing
  goes in that Amos cannot defend in an interview.
- **No emojis. No em dashes.** Enforced by `tests/check.sh`.
- **Signal over ornament.** No animated SVGs, no trophy walls, no third-party stats cards.
  Third-party cards would also undercount: most of the 2026 work sits in private repos.

## Stack

Python 3 with Pillow for the one generator, bash for the checks. Nothing else.
