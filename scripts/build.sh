#!/usr/bin/env bash
# Rebuild the README plate: dithered portrait, then the banner via headless Chrome.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/portrait.py

google-chrome --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1600,640 \
  --allow-file-access-from-files \
  --screenshot=assets/banner.png \
  "file://$PWD/scripts/banner.html"

google-chrome --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1000,600 \
  --allow-file-access-from-files \
  --screenshot=assets/banner-compact.png \
  "file://$PWD/scripts/banner-compact.html"

python3 scripts/ascii.py > assets/portrait.txt
echo "banners and assets/portrait.txt rebuilt"
