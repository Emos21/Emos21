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
```

`scripts/ascii.py` crops the photograph, corrects for a monospace cell being roughly twice
as tall as it is wide, maps brightness onto the ramp `@%#*+=-:.` and trims the solid block
where the black shirt saturates to a single character. Output is 60 columns and 37 lines.

After regenerating, paste the file into the fenced block at the top of `README.md`. The
block and the file must match exactly; `tests/check.sh` compares them.

Requirements: `python3` with Pillow. Nothing else, and no browser.

## Checks

```bash
tests/check.sh
```

Verifies the README has no emojis and no em dashes, that it loads no image files, that the
plate is 60 columns or narrower, that the embedded block still matches what
`scripts/ascii.py` produces, and that every outbound link answers. LinkedIn answers `999`
to anything that is not a browser; the check treats that as reachable.

Run it before every push. The profile is the first thing a recruiter sees, so a broken
link is the whole cost of the page.

## Deploy state

Live as of 2026-09-22: README led by the 60-column text portrait, then a five-row selected
work table, the stack, four verified figures, and contact. An earlier version of this
rewrite led with a dithered photograph set as a printed plate; Amos rejected it and the
assets and their generators were removed in the same series of commits.
