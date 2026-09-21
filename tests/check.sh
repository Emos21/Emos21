#!/usr/bin/env bash
# Invariants for the profile README. Run before every push.
set -uo pipefail
cd "$(dirname "$0")/.."
fail=0
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
ok()  { printf '  ok    %s\n' "$1"; }
bad() { printf '  FAIL  %s\n' "$1"; fail=1; }

echo "house style"
grep -q '—' README.md && bad "em dash in README.md" || ok "no em dashes"
if python3 -c 'import sys,unicodedata as u; t=open("README.md",encoding="utf-8").read(); sys.exit(1 if [c for c in t if u.category(c)=="So" or ord(c)>0x1F000] else 0)'; then
  ok "no emojis"
else
  bad "emoji or pictograph in README.md"
fi

echo "the plate is characters, not a photograph"
if grep -qE '\.png|\.jpe?g|\.gif' README.md; then
  bad "README references a raster image; the portrait must stay characters"
else
  ok "no raster images in the README"
fi
width=$(awk '{ if (length($0) > m) m = length($0) } END { print m }' assets/portrait.txt)
[ "$width" -le 60 ] && ok "plate is ${width} columns wide" || bad "plate is ${width} columns, expected 60 or fewer"

echo "animated plate"
if python3 -c 'import xml.etree.ElementTree as E; E.parse("assets/portrait.svg")' 2>/dev/null; then
  ok "assets/portrait.svg parses"
else
  bad "assets/portrait.svg is not valid XML"
fi
tmp=$(mktemp -t plate-XXXX.svg)
PYTHONPATH=scripts python3 scripts/portrait_svg.py "$tmp" >/dev/null
if diff -q "$tmp" assets/portrait.svg >/dev/null; then
  ok "assets/portrait.svg is current"
else
  bad "assets/portrait.svg differs from scripts/portrait_svg.py output"
fi
rm -f "$tmp"
rows=$(grep -c 'class="r"' assets/portrait.svg)
plate_rows=$(wc -l < assets/portrait.txt)
[ "$rows" = "$plate_rows" ] && ok "svg carries all $rows rows" || bad "svg has $rows rows, plate has $plate_rows"
grep -q 'prefers-reduced-motion' assets/portrait.svg && ok "reduced-motion gate present" || bad "no reduced-motion gate in the svg"
grep -q 'prefers-color-scheme' assets/portrait.svg && ok "dark-scheme fill present" || bad "no dark-scheme fill in the svg"
grep -q 'animation: print' assets/portrait.svg && ok "line-by-line print animation present" || bad "print animation missing"
if grep -qE '\.(r|p)[^{]*\{[^}]*opacity: *0' assets/portrait.svg; then
  bad "a row starts at opacity 0; the plate must be whole when animation never runs"
else
  ok "plate is whole without animation"
fi

echo "stack ticker"
if python3 -c 'import xml.etree.ElementTree as E; E.parse("assets/stack.svg")' 2>/dev/null; then
  ok "assets/stack.svg parses"
else
  bad "assets/stack.svg is not valid XML"
fi
tmp=$(mktemp -t stack-XXXX.svg)
python3 scripts/stack_svg.py "$tmp" >/dev/null
diff -q "$tmp" assets/stack.svg >/dev/null \
  && ok "assets/stack.svg is current" \
  || bad "assets/stack.svg differs from scripts/stack_svg.py output"
rm -f "$tmp"
chips=$(grep -c 'class="k"' assets/stack.svg)
items=$(python3 -c 'import sys; sys.path.insert(0, "scripts"); import stack_svg; print(len(stack_svg.ITEMS))')
if [ "$chips" -ge $((items * 2)) ]; then
  ok "$chips chips carry $items items, enough copies for a seamless loop"
else
  bad "$chips chips for $items items; the loop will show a gap"
fi
grep -q 'animation: run' assets/stack.svg && ok "ticker animation present" || bad "ticker animation missing"
grep -q 'prefers-reduced-motion' assets/stack.svg && ok "ticker reduced-motion gate present" || bad "no reduced-motion gate in the ticker"
grep -q 'prefers-color-scheme' assets/stack.svg && ok "ticker dark-scheme fill present" || bad "no dark-scheme fill in the ticker"
for label in Python Go Django FastAPI PostgreSQL Docker PHP TypeScript React; do
  grep -q ">$label<" assets/stack.svg || bad "ticker is missing $label"
done
ok "every named item is in the ticker"

echo "ascii plate matches generator"
if diff -q <(python3 scripts/ascii.py) assets/portrait.txt >/dev/null; then
  ok "assets/portrait.txt is current"
else
  bad "assets/portrait.txt differs from scripts/ascii.py output"
fi
for asset in assets/portrait.svg assets/stack.svg; do
  grep -q "$asset" README.md && ok "README shows $asset" || bad "README does not reference $asset"
done

echo "contact hygiene"
if grep -rqE 'signal\.me/#' README.md CLAUDE.md MAIN.md; then
  bad "a signal.me share link is in the repo; publish the username, not the token"
else
  ok "no signal.me share token published"
fi

echo "outbound links"
for url in $(grep -oE 'https://[a-zA-Z0-9./_#?=-]+' README.md | sort -u); do
  code=$(curl -s -o /dev/null -L --max-time 20 -A "$UA" -w '%{http_code}' "$url")
  case "$code" in
    2*|3*|999) ok "$code $url" ;;                 # LinkedIn answers 999 to non-browsers
    *)         bad "$code $url" ;;
  esac
done

echo
[ "$fail" = 0 ] && echo "all checks passed" || echo "checks failed"
exit "$fail"
