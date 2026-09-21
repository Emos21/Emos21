# Operating this repo

## Where it lives

| | |
|---|---|
| Remote | `git@github.com:Emos21/Emos21.git` (public) |
| Live page | https://github.com/Emos21 |
| Working copy | `~/Desktop/github-profile` |
| Source photograph | `~/Downloads/Images/mimi.jpeg` (not committed) |

Publishing is `git push` to `main`. GitHub picks up the README immediately; the image URLs
are proxied through camo, so a changed asset can take a minute to refresh in a warm cache.

## Rebuilding the plates

```bash
scripts/build.sh
```

That runs, in order:

1. `scripts/portrait.py` reads the photograph, crops the plate, upscales it to the exact
   pixel size the banner renders at, then Floyd-Steinberg dithers it to 1-bit ink with an
   alpha channel. Output: `assets/portrait.png` (560x966) for the wide plate and
   `assets/portrait-compact.png` (468x852) for the narrow one.
2. Headless Chrome shoots `scripts/banner.html` at 1600x640 with a device scale factor of 2.
   Output: `assets/banner.png` (3200x1280).
3. The same for `scripts/banner-compact.html` at 1000x600. Output:
   `assets/banner-compact.png` (2000x1200).
4. `scripts/ascii.py` re-renders the 80-column text portrait to `assets/portrait.txt`,
   which is pasted into the collapsed block at the foot of the README.

Requirements: `python3` with Pillow, a `google-chrome` binary, and IBM Plex Mono installed
for the user running the build (`~/.fonts/ibm-plex-mono`, then `fc-cache -f`). Without the
font, Chrome falls back to DejaVu Sans Mono and the plate loses its proportions.

## Checks

```bash
tests/check.sh
```

Verifies the README has no emojis and no em dashes, that every referenced local asset
exists at the expected dimensions, that the embedded ASCII plate still matches what
`scripts/ascii.py` produces, and that every outbound link answers. LinkedIn answers `999`
to anything that is not a browser; the check treats that as reachable.

Run it before every push. The profile is the first thing a recruiter sees, so a broken
image or a dead link is the whole cost of the page.

## Deploy state

Live as of 2026-09-21: rewritten README with the printed-plate banner, a five-row selected
work table, verified figures, and the ASCII plate. Previous version was a plain text
README with a dead portfolio link to `emos21.github.io/Emos`, now pointing at
`amosmwangi.com`.
