# Emos21/Emos21

The GitHub profile README for Amos Mwangi. The rendered `README.md` at the repo root is
what appears above the pinned repositories at github.com/Emos21, so this repo is a
publishing surface, not an application.

## What it is

- `README.md` is the profile page. Everything else exists to produce it.
- `assets/banner.png` is the hero plate: a 1-bit dithered portrait set in a printed-manual
  layout, rendered from HTML by headless Chrome. `assets/banner-compact.png` is the same
  plate reflowed for narrow viewports.
- `scripts/` holds the generators. No asset is hand-edited in an image editor; every one is
  reproducible from the source photograph with `scripts/build.sh`.

## Rules

- **Every claim is verifiable.** Numbers come from the GitHub API, from a repository, or
  from a system that is actually in production. Nothing is estimated upward, and nothing
  goes in that Amos cannot defend in an interview.
- **Register:** printed technical manual. Warm paper (`#F5F2EA`), ink (`#12110F`), one
  vermilion accent (`#B3352A`), IBM Plex Mono throughout, hairline rules, figure captions.
- **Light surfaces only.** No dark-mode variant of the plate.
- **No emojis. No em dashes.** Enforced by `tests/check.sh`.
- **Signal over ornament.** No animated SVGs, no trophy walls, no third-party stats cards.
  Third-party cards would also undercount: most of the 2026 work sits in private repos.
- Type in the plate must survive being scaled down to a phone. Check it before committing.

## Stack

Python 3 with Pillow and NumPy for the image work, plain HTML and CSS for the plate layout,
headless Chrome as the renderer, bash for the build. No dependencies beyond Pillow, NumPy
and a Chrome binary.
