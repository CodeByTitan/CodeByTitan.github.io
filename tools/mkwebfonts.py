"""Subset Futura PT and Anton to a Latin range and ship them as woff2.

    .venv/bin/pip install fonttools brotli
    .venv/bin/python tools/mkwebfonts.py

Range, not --text: subsetting to the exact characters currently on the page
would silently lose a glyph the first time a line of copy is edited. The raw
futura-pt/ and anton/ folders are gitignored; only the woff2 cuts ship.
"""
import os
from fontTools import subset

RANGES = ",".join([
    "U+0020-007E", "U+00A0-00FF", "U+0100-017F", "U+2010-2015", "U+2018-201E",
    "U+2020-2022,U+2026,U+2030,U+2039,U+203A",
    "U+20AC,U+2122,U+2190-2199,U+2212,U+00D7",
])
CUTS = [("futura-pt/FuturaCyrillicBook.ttf",   "fu-400"),
        ("futura-pt/FuturaCyrillicMedium.ttf", "fu-500"),
        ("futura-pt/FuturaCyrillicBold.ttf",   "fu-700"),
        # Anton, cloots.ca's own headline face (.big-head), used for the one
        # line that types at the Cloots door. SIL OFL 1.1, anton/OFL.txt.
        ("anton/Anton-Regular.ttf",            "anton-400"),
        # Gotham Black, his own files (Gotham/, gitignored), for the portal line.
        # Commercial face: the web licence is his to hold, see CLAUDE.md 4.3.
        ("Gotham/Gotham Black/Gotham Black.otf", "gotham-900")]
for src, name in CUTS:
    out = "assets/fonts/%s.woff2" % name
    subset.main([src, "--unicodes=" + RANGES,
                 "--layout-features=*", "--flavor=woff2", "--output-file=" + out])
    print("%-16s %3dKB" % (name, os.path.getsize(out) // 1024))
