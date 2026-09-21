# Emos21/Emos21

The GitHub profile README for Amos Mwangi. The rendered `README.md` at the repo root is
what appears above the pinned repositories at github.com/Emos21, so this repo is a
publishing surface, not an application.

## What it is

- `README.md` is the profile page. Everything else exists to produce it.
- The portrait at the top is **not an image file**. It is 60 columns of text, generated from
  a photograph by `scripts/ascii.py` and stored in `assets/portrait.txt`, then pasted into
  the fenced block at the top of the README. A picture drawn in code symbols is the point of
  the page; a photograph, or a rendered plate of a photograph, is not.
- No PNG, SVG or GIF belongs in this repo. The only images the README loads are the six
  stack badges from shields.io.

## Rules

- **The portrait stays text.** 60 columns, from `scripts/ascii.py`. If the crop or ramp
  changes, regenerate `assets/portrait.txt` and re-paste the block; `tests/check.sh` fails
  when the two drift apart.
- **Every claim is verifiable.** Numbers come from the GitHub API, from a repository, or
  from a system that is actually in production. Nothing is estimated upward, and nothing
  goes in that Amos cannot defend in an interview.
- **No emojis. No em dashes.** Enforced by `tests/check.sh`.
- **Signal over ornament.** No animated SVGs, no trophy walls, no third-party stats cards.
  Third-party cards would also undercount: most of the 2026 work sits in private repos.

## Stack

Python 3 with Pillow for the one generator, bash for the checks. Nothing else.
