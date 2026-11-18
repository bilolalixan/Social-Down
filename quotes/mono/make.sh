#!/bin/bash
# Usage: ./make.sh "Quote matni" out-name   -> out-name.png (3240x5760) + out-name-2160.jpg
set -e
cd "$(dirname "$0")"
python3 - "$1" <<'PY'
import sys,html
q=html.escape(sys.argv[1],quote=False)
open('_tmp.html','w').write(open('template.html').read().replace('{{QUOTE}}',q))
PY
sed -e "s#m2.html#_tmp.html#" -e "s#quote-mono-small.png#$2.png#" r2.js > _r.js && node _r.js
python3 -I -c "
from PIL import Image
Image.open('$2.png').convert('RGB').resize((2160,3840),Image.LANCZOS).save('$2-2160.jpg',quality=98,subsampling=0)"
rm -f _tmp.html _r.js
