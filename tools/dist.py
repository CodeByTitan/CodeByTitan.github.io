"""Build dist/: index.html plus only the assets it references.

The live site is published from this folder by .github/workflows/pages.yml,
so CLAUDE.md, FONT-LICENSE-DECISION.md, tools/, the raw font archives and
every asset nothing references stay in the repo and never go online. A
reference is any `assets/...` path with a file extension that appears in
index.html: src, href, poster, CSS url() and JS strings alike.
"""
import os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
refs = sorted(set(r for r in re.findall(r"assets/[A-Za-z0-9_./-]+", html) if re.search(r"\.[a-z0-9]{2,5}$", r)))

dist = os.path.join(ROOT, "dist")
shutil.rmtree(dist, ignore_errors=True)
os.makedirs(dist)
shutil.copy2(os.path.join(ROOT, "index.html"), dist)
open(os.path.join(dist, ".nojekyll"), "w").close()

copied, missing, total = [], [], 0
for r in refs:
    src = os.path.join(ROOT, r)
    if not os.path.isfile(src):
        missing.append(r)
        continue
    dst = os.path.join(dist, r)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    copied.append(r)
    total += os.path.getsize(src)

print("dist: index.html + %d assets, %.1f MB" % (len(copied), total / 1048576))
if missing:
    # a path mentioned in a comment may not exist; a path in real markup that
    # does not exist is what verify.py's brokenMedia check is for
    print("referenced but not on disk (not copied):", missing)
if "--list" in sys.argv:
    print("\n".join(copied))
