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

echo "the plate is text, not an image"
if grep -qE '<img|srcset=|\.png' README.md; then
  bad "README references an image; the portrait must stay 60 columns of text"
else
  ok "no image files in the README"
fi
width=$(awk '{ if (length($0) > m) m = length($0) } END { print m }' assets/portrait.txt)
[ "$width" -le 60 ] && ok "plate is ${width} columns wide" || bad "plate is ${width} columns, expected 60 or fewer"

echo "ascii plate matches generator"
if diff -q <(python3 scripts/ascii.py) assets/portrait.txt >/dev/null; then
  ok "assets/portrait.txt is current"
else
  bad "assets/portrait.txt differs from scripts/ascii.py output"
fi
if grep -qF "$(sed -n '20p' assets/portrait.txt)" README.md; then
  ok "README embeds the current plate"
else
  bad "README ASCII block is stale, re-embed assets/portrait.txt"
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
