"""The CLAUDE.md section 7 checklist, run end to end."""
import os, json, glob, re, io
from playwright.sync_api import sync_playwright

ROOT = "/Users/arshsethi/Desktop/AndroidStudioProjects/arsh-portfolio/"
URL = "file://" + ROOT + "index.html"
R = {}

p = sync_playwright().start()
b = p.chromium.launch()

# --- 3. wheel test: native scroll, no jacking ---
c = b.new_context(viewport={"width": 1440, "height": 900})
pg = c.new_page()
errs = []
pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
pg.on("pageerror", lambda e: errs.append(str(e)))
pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2400)
# The portal autoscrolls by design (CLAUDE.md 4.7, his decision), so the
# wheel gate runs on either side of it: six flicks from the top, six from just
# past the pin. Then the portal's own contract: the same traversal time from
# any entry speed, and wheel-up aborts.
pin = pg.evaluate("(()=>{const t=ScrollTrigger.getById('portal');return t?[Math.round(t.start),Math.round(t.end)]:null})()")
# window.scrollTo is ignored by Lenis while it is still smoothing the last
# flick's tail (it treats a native scroll mid-smooth as its own), so a jump
# fired straight after a wheel test silently does not happen. Park through
# Lenis when it is there.
def park(y):
    pg.evaluate("(y)=>{window.__lenis?__lenis.scrollTo(y,{immediate:true,force:true}):window.scrollTo(0,y)}", y)
    pg.wait_for_timeout(900)
travels = []
for start in ([0, pin[1] + 300] if pin else [0, 0]):
    park(start)
    for i in range(6):
        before = pg.evaluate("scrollY")
        pg.mouse.wheel(0, 700)
        pg.wait_for_timeout(230)
        travels.append(round(pg.evaluate("scrollY") - before))
R["wheelTravels"] = travels
R["wheelPass"] = all(t >= 600 for t in travels)
if pin:
    times = []
    expect = (pg.evaluate("window.__portalAutoMs || 8000")) / 1000.0
    # frames with a write to <html>/<body>: records are delivered once a
    # frame, so one callback is one full-document style recalc however many
    # properties were written in it
    pg.evaluate("""(()=>{ window.__rootWrites = 0; const o = new MutationObserver(ms => { window.__rootWrites += 1; });
      o.observe(document.documentElement, {attributes:true}); o.observe(document.body, {attributes:true}); })()""")
    for step, gap in ((60, 30), (300, 60), (1200, 230)):
        park(pin[0] - 900)
        pg.mouse.move(700, 450)
        t0 = None
        for _ in range(60):
            pg.mouse.wheel(0, step); pg.wait_for_timeout(gap)
            y = pg.evaluate("scrollY")
            if t0 is None and y >= pin[0] - 2: t0 = pg.evaluate("performance.now()")
            if y >= pin[1]: break
        for _ in range(400):
            if pg.evaluate("scrollY") >= pin[1]: break
            pg.wait_for_timeout(50)
        times.append(round((pg.evaluate("performance.now()") - t0) / 1000, 2) if t0 else None)
    R["portalTraversalSeconds"] = times
    R["portalPacePass"] = all(t and abs(t - expect) < 0.6 for t in times)
    R["portalRootWrites"] = pg.evaluate("window.__rootWrites") // 3   # three traversals were observed
    R["portalRootWritesPass"] = R["portalRootWrites"] < 80
    park(pin[0] - 400)
    pg.mouse.wheel(0, 700); pg.wait_for_timeout(1500)
    y1 = pg.evaluate("scrollY"); pg.mouse.wheel(0, -300); pg.wait_for_timeout(800); y2 = pg.evaluate("scrollY")
    R["portalAbortOnWheelUp"] = y2 < y1 + 20
    # a trackpad's lift-off artefacts (sub-pixel negatives) must not abort
    park(pin[0] - 400)
    pg.mouse.wheel(0, 700); pg.wait_for_timeout(600)
    pg.mouse.wheel(0, -0.4); pg.wait_for_timeout(40); pg.mouse.wheel(0, -1); pg.wait_for_timeout(40); pg.mouse.wheel(0, -2); pg.wait_for_timeout(300)
    R["portalLiftoffPass"] = bool(pg.evaluate("!!window.__portalAutoInfo()"))
    # a deliberate abort, then wheel-down inside the pin re-arms at the same pace and finishes
    park(pin[0] - 400)
    pg.mouse.wheel(0, 700); pg.wait_for_timeout(900)
    pg.mouse.wheel(0, -300); pg.wait_for_timeout(600)
    aborted = not pg.evaluate("!!window.__portalAutoInfo()")
    ya = pg.evaluate("scrollY"); pg.mouse.wheel(0, 120); pg.wait_for_timeout(200)
    rearmed = bool(pg.evaluate("!!window.__portalAutoInfo()"))
    t0 = pg.evaluate("performance.now()")
    for _ in range(200):
        if pg.evaluate("scrollY") >= pin[1]: break
        pg.wait_for_timeout(50)
    took = (pg.evaluate("performance.now()") - t0) / 1000
    expected = expect * (pin[1] - ya) / (pin[1] - pin[0])
    R["portalRearm"] = {"aborted": aborted, "rearmed": rearmed, "took": round(took, 2), "expected": round(expected, 2)}
    R["portalRearmPass"] = aborted and rearmed and abs(took - expected) < 0.7
    # three ways past the pin that must NOT start the autoscroll: a nav anchor
    # below it, a reload with the scroll restored below it, a #hash load
    jumps = {}
    park(0)
    tgt = pg.evaluate("Math.round(document.querySelector('#contact').getBoundingClientRect().top+scrollY)")
    pg.click('nav a[href="#contact"]'); pg.wait_for_timeout(2500)
    jumps["anchor"] = abs(pg.evaluate("scrollY") - tgt) < 120
    park(pin[1] + 2500)
    pg.reload(wait_until="load"); pg.wait_for_timeout(2500)
    jumps["reload"] = pg.evaluate("scrollY") > pin[1] + 1500
    pg.goto(URL + "#ship", wait_until="load"); pg.wait_for_timeout(2500)
    jumps["hash"] = pg.evaluate("scrollY") > pin[1] + 500
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2500)
    R["portalJumps"] = jumps
    R["portalJumpPass"] = all(jumps.values())

# --- 6/7. console + computed fonts ---
R["consoleErrors"] = errs
R["fonts"] = pg.evaluate("""() => {
  const f = s => { const n=document.querySelector(s); return n?getComputedStyle(n).fontFamily.split(',')[0].replace(/"/g,''):null; };
  return {body:f('body'), micro:f('.micro'), quote:f('.ship-claim'), heroQuoteSvg:!!document.querySelector('#heroShip svg.hs'), disp:f('.disp'), mono:f('.mono')};
}""")
R["meta"] = pg.evaluate("""() => ({
  title: document.title,
  desc: document.querySelector('meta[name=description]').content,
  theme: document.querySelector('meta[name=theme-color]').content,
  og: !!document.querySelector('meta[property="og:image"]'),
})""")
# links resolve (same-page anchors and file existence for assets)
R["deadAnchors"] = pg.evaluate("""() => [...document.querySelectorAll('a[href^="#"]')]
  .map(a=>a.getAttribute('href')).filter(h=>h!=='#' && !document.querySelector(h))""")
R["brokenMedia"] = pg.evaluate("""() => {
  const bad=[...document.images].filter(i=>i.complete && i.naturalWidth===0).map(i=>i.getAttribute('src'));
  const v=[...document.querySelectorAll('video')].filter(x=>x.readyState===0).map(x=>x.getAttribute('src'));
  return {img:bad, videoUnloaded:v};
}""")
c.close()

# --- 4. reduced motion ---
c = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
pg = c.new_page(); pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2200)
R["reduced"] = pg.evaluate("""() => {
  const vis = s => { const n=document.querySelector(s); if(!n) return 'missing';
    const r=n.getBoundingClientRect(); const cs=getComputedStyle(n);
    return (r.height>4 && cs.opacity!=='0' && cs.visibility!=='hidden') ? 'ok' : 'hidden'; };
  return {
    heroName: vis('#heroName'), any1: vis('#any1 .proj-copy'), close: vis('.close-line'),
    veilOpacity: getComputedStyle(document.getElementById('veilCanvas')).opacity,
    videosPaused: [...document.querySelectorAll('video')].every(v=>v.paused),
    dimmedNodes: [...document.querySelectorAll('.tl-key,.flow-tok')]
      .filter(n=>parseFloat(getComputedStyle(n).opacity)<0.9).length,
  };
}""")
pg.screenshot(path="/private/tmp/claude-501/-Users-arshsethi-Desktop-AndroidStudioProjects-JobClanker/f7b3df84-3bea-447c-b41d-0a1109ddeb35/scratchpad/shots/v-reduce.png", full_page=True)
c.close()

# --- 5. GSAP blocked ---
c = b.new_context(viewport={"width": 1440, "height": 900})
pg = c.new_page()
pg.route("**/gsap*", lambda r: r.abort())
pg.route("**/ScrollTrigger*", lambda r: r.abort())
nogsap_err = []
pg.on("pageerror", lambda e: nogsap_err.append(str(e)))
pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2200)
R["noGsap"] = pg.evaluate("""() => ({
  gsap: typeof window.gsap,
  heroVisible: document.querySelector('#heroName').getBoundingClientRect().height>20,
  bodyText: document.body.innerText.length,
  dimmed: [...document.querySelectorAll('.tl-key,.flow-tok')]
    .filter(n=>parseFloat(getComputedStyle(n).opacity)<0.9).length,
  navName: getComputedStyle(document.getElementById('navNameFull')).opacity,
})""")
R["noGsapErrors"] = nogsap_err
pg.screenshot(path="/private/tmp/claude-501/-Users-arshsethi-Desktop-AndroidStudioProjects-JobClanker/f7b3df84-3bea-447c-b41d-0a1109ddeb35/scratchpad/shots/v-nogsap.png", full_page=True)
c.close()
b.close(); p.stop()

# --- 8. weights ---
big = []
total = 0
for f in glob.glob(ROOT + "assets/**/*", recursive=True) + [ROOT + "index.html"]:
    if os.path.isfile(f):
        sz = os.path.getsize(f)
        if "/fonts/" in f and f.endswith(("tnr-mt-italic.otf", "tnr-mt-bold-condensed.otf")):
            continue
        total += sz
        if sz > 350 * 1024 and not f.endswith((".mp4", ".otf", ".ttf")):
            big.append((os.path.relpath(f, ROOT), round(sz / 1024)))
R["oversizeImages"] = big
R["assetTotalMB"] = round(total / 1048576, 2)

# --- 9. greps ---
s = io.open(ROOT + "index.html", encoding="utf-8").read()
R["grep"] = {
    "emDash": s.count(u"—") + s.count("&mdash;"),
    "oldNavy": s.count("#05157D") + s.count("05157d"),
    "oldCream": s.count("#FFFCFB"),
    "oldRed": s.count("#AD2831") + s.count("#FFF3E0"),
    "marquee": s.count("mq-track"),
    "founderAmp": s.count("Founder &"),
    "shipLine": ("Designed and developed solo." in s and "Shipped as a team." in s),
    "phases": sorted(set(re.findall(r'data-phase="([a-z0-9]+)"', s))),
    "boreckFontFace": s.count("boreckdisplay"),
    "lumiareFontFace": s.count("Lumiare.otf"),
}
print(json.dumps(R, indent=1))

# --- phase palette guard -------------------------------------------------
# Every phase must declare a palette, or a section silently inherits whatever
# the previous one left on the root and the ink can land on the wrong ground.
_declared = set(re.findall(r'data-phase="([a-z0-9]+)"', s))
_defined = set(re.findall(r"\n    ([a-z0-9]+):\s*\{ base:", s))
R["phaseGuard"] = {"used": sorted(_declared), "defined": sorted(_defined),
                   "missing": sorted(_declared - _defined)}
print(json.dumps({"phaseGuard": R["phaseGuard"]}, indent=1))
