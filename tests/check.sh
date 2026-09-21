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

echo "assets"
check_png() {
  if [ ! -f "$1" ]; then bad "$1 missing"; return; fi
  read -r w h < <(python3 -c "from PIL import Image;i=Image.open('$1');print(i.width,i.height)")
  if [ "$w" = "$2" ] && [ "$h" = "$3" ]; then ok "$1 ${w}x${h}"; else bad "$1 is ${w}x${h}, expected $2x$3"; fi
}
check_png assets/banner.png 3200 1280
check_png assets/banner-compact.png 2000 1200
check_png assets/portrait.png 560 966
check_png assets/portrait-compact.png 468 852

for ref in $(grep -oE '(src|srcset)="[^"]+"' README.md | cut -d'"' -f2); do
  [ -f "$ref" ] && ok "referenced $ref" || bad "referenced $ref is missing"
done

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
