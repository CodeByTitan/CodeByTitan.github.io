"""Bake the portal ground: his liquid-marbling texture, motion-blurred.

    .venv/bin/python tools/mkportalbg.py

Source: _source/marbling/original.jpg (6000x3000, gitignored). Output:
assets/portal-bg.jpg, 1920 wide, under the 350KB image cap. The blur is a
horizontal smear (squeeze the width, box blur, stretch back), the look of the
reference he sent, done here once rather than with a CSS filter per frame.
The first bake used a 90px streak and a 35% overlay on top: the marbling is
monochrome, thin white ribbons on black, and it vanished. Keep the streak
short.
"""
import os
from PIL import Image, ImageFilter, ImageEnhance

SRC, OUT, W = "_source/marbling/original.jpg", "assets/portal-bg.jpg", 1920
FACTOR, RADIUS, SOFTEN, SAT = 6, 3, 1.6, 1.0   # ~18px streak, ~3px vertical: the ribbons survive
BRIGHT, CONTRAST = 1.25, 1.10                    # the texture is thin white lines on black; lift them a little

im = Image.open(SRC).convert("RGB")
base = im.resize((W, int(im.height * W / im.width)), Image.LANCZOS)
w, h = base.size
small = base.resize((max(1, w // FACTOR), h), Image.BILINEAR).filter(ImageFilter.BoxBlur(RADIUS))
out = small.resize((w, h), Image.BICUBIC).filter(ImageFilter.GaussianBlur(SOFTEN))
out = ImageEnhance.Color(out).enhance(SAT)
out = ImageEnhance.Brightness(out).enhance(BRIGHT)
out = ImageEnhance.Contrast(out).enhance(CONTRAST)
for q in (82, 78, 74, 70, 66, 62, 58):
    out.save(OUT, "JPEG", quality=q, optimize=True, progressive=True)
    if os.path.getsize(OUT) <= 340 * 1024:
        break
print("%s %dx%d %dKB q%d" % (OUT, w, h, os.path.getsize(OUT) // 1024, q))
