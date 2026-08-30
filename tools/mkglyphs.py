"""Convert display strings to SVG outlines.

Boreck Display and Lumiare are personal-use demo fonts. Shipping the font
files on a public site redistributes them; shipping paths does not, and the
type then renders identically everywhere with no FOUT. See CLAUDE.md 8.5.
"""
import sys, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform

BORECK = "boreck-display-font/boreckdisplay-bold.otf"
LUMIARE = "lumiare/Lumiare.otf"


def outline(path, text, tracking=0.0):
    """Return (svg_path_d, width, ymin, ymax) in font units, y already flipped."""
    f = TTFont(path)
    gs = f.getGlyphSet()
    cmap = f.getBestCmap()
    upm = f["head"].unitsPerEm
    hmtx = f["hmtx"]

    # kerning from GPOS is skipped on purpose: these are short display strings
    # set with explicit tracking, and a demo font's kern coverage is unreliable.
    d = []
    x = 0.0
    ymin, ymax = 1e9, -1e9
    for ch in text:
        if ch == " ":
            # advance of the space glyph, or a quarter em if it has none
            gn = cmap.get(32)
            x += (hmtx[gn][0] if gn else upm * 0.25) + tracking * upm
            continue
        gn = cmap.get(ord(ch))
        if gn is None:
            raise SystemExit("missing glyph for %r in %s" % (ch, path))
        # y flip: font units go up, SVG goes down
        t = Transform(1, 0, 0, -1, x, 0)
        pen = SVGPathPen(gs, ntos=lambda v: repr(round(v, 1)))
        gs[gn].draw(TransformPen(pen, t))
        seg = pen.getCommands()
        if seg:
            # one path per glyph, never a concatenated d: with fill-rule
            # nonzero two overlapping glyph outlines cancel each other and
            # punch a hole (Boreck's S tail crosses into the E).
            d.append('<path d="%s" fill="currentColor"/>' % seg)
        bp = BoundsPen(gs)
        gs[gn].draw(bp)
        if bp.bounds:
            ymin = min(ymin, bp.bounds[1])
            ymax = max(ymax, bp.bounds[3])
        x += hmtx[gn][0] + tracking * upm
    width = x - tracking * upm
    return "".join(d), width, ymin, ymax


def svg(path, text, tracking=0.0, cls="", label=None, pad=0.02):
    d, w, ymin, ymax = outline(path, text, tracking)
    # viewBox in the flipped space: y runs from -ymax (top) to -ymin (bottom)
    px = w * pad
    top = -ymax - (ymax - ymin) * pad
    h = (ymax - ymin) * (1 + 2 * pad)
    vb = "%.1f %.1f %.1f %.1f" % (-px, top, w + 2 * px, h)
    lab = label if label is not None else text
    return ('<svg class="%s" viewBox="%s" role="img" aria-label="%s" '
            'preserveAspectRatio="xMinYMid meet" focusable="false">'
            '%s</svg>') % (cls, vb, lab, d)


if __name__ == "__main__":
    out = {}
    # the hero name, one SVG per line so the existing per-line rise still works
    out["hero_arsh"] = svg(BORECK, "ARSH", tracking=0.028, cls="hero-line nm", label="Arsh")
    out["hero_sethi"] = svg(BORECK, "SETHI", tracking=0.028, cls="hero-line nm", label="Sethi")
    out["nav_name"] = svg(BORECK, "ARSH SETHI", tracking=0.05, cls="nav-nm", label="Arsh Sethi")

    for key, txt in [
        ("cloots", "Cloots"), ("any1", "ANY1"), ("helv", "Helv"),
        ("dap", "DAP Atlantic"), ("sqldb", "SQLDB"), ("unbdine", "UNBDine"),
        ("angular", "Angular"), ("lets", "Let’s talk"),
    ]:
        out["p_" + key] = svg(LUMIARE, txt, tracking=0.0, cls="pt", label=txt)

    json.dump(out, open(sys.argv[1], "w"), indent=1)
    for k, v in out.items():
        print(k, len(v))

# Usage:
#   python3 -m venv .venv && .venv/bin/pip install fonttools
#   .venv/bin/python tools/mkglyphs.py glyphs.json
# Then paste the strings into index.html. Re-run this only when a display
# string changes; the paths in index.html are the shipped artefact.


BEMORE = "Bemore Serif.otf"


def svg_groups(path, parts, tracking=0.0, cls="", label=None, pad=0.03):
    """One SVG for a whole line, with each part in its own named <g>.

    The hero quote needs "ship." to take a colour tween on its own while the
    rest of the line stays ink. Two separate SVGs would have to be baseline
    aligned by hand; one SVG with two groups cannot drift.
    """
    f = TTFont(path)
    gs, cmap, hmtx = f.getGlyphSet(), f.getBestCmap(), f["hmtx"]
    upm = f["head"].unitsPerEm
    x = 0.0
    ymin, ymax = 1e9, -1e9
    groups = []
    for gname, text in parts:
        d = []
        for ch in text:
            if ch == " ":
                sp = cmap.get(32)
                x += (hmtx[sp][0] if sp else upm * 0.25) + tracking * upm
                continue
            gn = cmap.get(ord(ch))
            if gn is None:
                raise SystemExit("missing glyph for %r in %s" % (ch, path))
            pen = SVGPathPen(gs, ntos=lambda v: repr(round(v, 1)))
            gs[gn].draw(TransformPen(pen, Transform(1, 0, 0, -1, x, 0)))
            seg = pen.getCommands()
            if seg:
                d.append('<path d="%s"/>' % seg)
            bp = BoundsPen(gs)
            gs[gn].draw(bp)
            if bp.bounds:
                ymin = min(ymin, bp.bounds[1])
                ymax = max(ymax, bp.bounds[3])
            x += hmtx[gn][0] + tracking * upm
        groups.append('<g class="%s">%s</g>' % (gname, "".join(d)))
    w = x - tracking * upm
    px = w * pad * 0.4
    top = -ymax - (ymax - ymin) * pad
    h = (ymax - ymin) * (1 + 2 * pad)
    return ('<svg class="%s" viewBox="%.1f %.1f %.1f %.1f" role="img" aria-label="%s" '
            'preserveAspectRatio="xMinYMid meet" focusable="false">%s</svg>'
            ) % (cls, -px, top, w + 2 * px, h, label, "".join(groups))
