# arsh-portfolio: the complete guide for Claude

Personal portfolio for Arsh Sethi. One static page (`index.html` plus
`assets/`), deploying to GitHub Pages at https://codebytitan.github.io (repo
name must be exactly `CodeByTitan.github.io`; not initialised yet).

Immediate goal: win the Senior/Experienced Product Designer role at trophi.ai
(AI gaming coach startup, a16z-backed, St. John's NL, remote). Standing goal:
the link on every application he sends.

---

## RULE ZERO

**No em dashes. Anywhere.** Site copy, captions, letters, commit messages, this
file, chat. Restructure the sentence instead. Separators in labels are a middle
dot. `tools/verify.py` greps for the character and the entity and fails on
either. It has already caught one that would otherwise have shipped.

## HOW TO READ THIS FILE

This is not a summary, at Arsh's request. It is the whole working memory of the
project: the facts, the confirmed wordings, the decisions, the reasons behind
them, and the traps. **Everything here is current.** Where something was tried
and rejected it says so, because the reason is what stops the next session
reinventing it.

Sections 1 and 2 are about him and are the ones that must never be violated.
Sections 3 to 5 are the content and the design system. Section 6 is bugs worth
remembering. Keep this file current as you work: record the reasoning, not just
the change.

---

# 1. WHO ARSH IS

## 1.1 Identity

- Arsh Sethi. Fredericton, New Brunswick, Canada.
- Public designation, exact: **Product Designer & Software Engineer**
- sethi.arsh2004@gmail.com · +1 506 721 9278
- github.com/CodeByTitan · linkedin.com/in/arsh-sethi-727917223
- cloots.ca (his product) · dapatlantic.com (his agency)

## 1.2 The journey, as facts

- Came to Canada as an international student. Bachelor of Computer Science,
  University of New Brunswick, from Sept 2022, graduating April 2026. **First
  year at the Saint John campus.**
- Started Python, then Java in 2021. Five years of Java by 2026.
- In first year he challenged Java I and Java II for credit and passed both
  examinations.
  - **CONFIRMED WORDING ONLY: "the first student at the Saint John campus to
    do so for both courses."** He is 100% sure of the both-courses claim.
  - **"Challenge for credit" is jargon and the page now explains it.** Arsh,
    2026-08-29: *"i think we should explain what challenge for credit means, i
    don't think most people would understand this, it means that I didn't
    actually had to take the course for full semester and I gave the exam on the
    first day of sem and passed."* The timeline detail now reads: **"Challenge
    for credit: sit the final exam in week one, skip the course. Passed Java I
    and Java II, the first at the campus to do both."** The surprising part is
    the one to protect: you sit the whole course's final exam *before being
    taught any of it*. A reader outside a Canadian university reads
    "challenged for credit" as a pass/fail retake and the achievement
    evaporates.
  - Note the tail moved from "the first at the campus to do **it**" to "to do
    **both**". "It" was ambiguous and could be read as challenging one course,
    which is exactly the version he is not sure about. "Both" is the confirmed
    claim and is now unambiguous. Keep it that way.
  - He *thinks* he was also first for Java I alone but is NOT sure. **Never use
    that version.** An uncertain superlative is the one line that gets
    challenged in an interview.
- Fourth year: mobile development course, grade A+. He asked to challenge that
  course too and was refused (fourth-year rule). He built the course project
  (Helv) himself; there was a group but he did the build.
  - **SENSITIVE: never publish anything like "teammates only submitted
    deliverables."** Agreed public wording: **"Designed and implemented the full
    application."** The course record shows a group; a solo claim in print
    invites a contradiction and reads as blaming collaborators.
- `assets/arsh-first-winter.jpg` was taken in Saint John, first winter of 2022:
  navy turban, navy FILA hoodie, snow bokeh. Same campus and semester as the
  Java challenge exams, which is why it belongs in the journey chapter. He knows
  he looks young in it; in a documentary chapter that is the point, anywhere
  else it would undersell him. **Approved for the journey chapter only.**
- **He is a gamer with real sim racing time.** His household bought an actual
  racing rig and he played GT7 on it heavily for about a week and by his own
  account got good. Honest scope: about a week. The claim is "I know this world
  as a player," never "sim racing expertise." Best used in the trophi cover
  letter, not necessarily on the page. Agreed wording: *"I'm a gamer, and I know
  the seat your product coaches from: I've driven GT7 on a full simulator rig.
  Picking up new games fast is half of what makes me useful to a coaching
  product; I remember what the first hour of not knowing feels like."*

## 1.3 Positioning: the candidate's edge

Every letter, answer and line should land the same thing, because it is his
genuine advantage: **range**. Java, then Kotlin, then Dart, mobile and
serverless (40+ Cloud Functions in production). He picks up an unfamiliar stack
deliberately and quickly.

In priority order:

1. **Show the range; never assert it.** "Adaptable", "fast learner", "picks
   things up quickly" are what every applicant writes and no reader credits.
   They are unfalsifiable, so they carry no information. The same claim with
   evidence ("shipped production work in Java, Kotlin and Dart across mobile and
   serverless") is unanswerable, and the reader reaches the conclusion
   themselves, which is where conviction comes from.
2. **Turn an unfamiliar stack into a short bridge, not a gap.** Name what
   transfers at the level of the model rather than the API: Cloud Functions to
   Lambda is the same event-driven stateless design with the same cold-start and
   IAM problems, so what is new is one vendor's surface. That reads as
   seniority. "I would have no problem picking it up" reads as optimism and
   invites doubt.
3. **State a gap plainly, then shrink its footprint.** One clause, never the
   through-line. Never let "I want to learn X" become the stated reason for
   applying to a senior role.
4. **Learning is a track record, not a promise.** Four languages across three
   platforms *is* the proof.

**Never write a comparative claim about other applicants.** "More versatile than
most", "few candidates offer this range". It cannot be substantiated, this
project cannot see the other applicants, and to a hiring reader it lands as
arrogance and devalues the true statement next to it.

Register to hit: an intermediate designer whose taste reads as senior
potential. The reaction the site must produce: *"the site itself is the proof,
he could do it for us."*

## 1.4 Honesty rails, absolute

Everything on the site must be true and interview-defensible. **Positioning
chooses emphasis among true facts. It never adds facts.** Use only the CONFIRMED
wordings for the sensitive claims. If a fact is not in this file and he did not
say it in the session, it does not go on the page.

This has already bitten: several strong-sounding drafts for the journey hook
were thrown out because they invented biography ("never seen snow", "minus
twenty", "the coldest place I had ever been"). All plausible. None of them
things he said.

---

# 2. HOW TO WORK WITH ARSH

## 2.1 Opinion first, action on his word

For anything about his content, his likeness or his claims: when he asks "what
do you think", **answer the question and wait.** Staging his photo before he
said yes annoyed him: *"i asked you for what do you think about the photo not
just put it in directly."* Build-step execution is fine autonomously.

## 2.2 He catches real things. Engage with the substance.

His catches have repeatedly beaten the automated checks: the scroll-jack, the
duplicated name, the sole-credit line, one project taking over the whole site,
the em dashes, the dead marquee, the nested boxes, a heading that was a label
rather than a hook. When he pushes back, the useful reply is a measurement, not
agreement.

## 2.3 What he reliably rejects

- **Anything that reads as a template or as machine-made.** No Material or
  Bootstrap cards, no purple-gradient AI look, no emoji decoration.
- **Full-width hairline rules under headings and between list rows.** His
  words: "the signature of a shitty ass claude code design". Space separates.
  See 4.6.
- **Rectangular boxes.** "Who is using a rectangular box in fucking 2026."
- **Dated motion.** The constant-scroll marquee, by name. Scroll-jacking is a
  hard no after one bad build.
- **Colours that read robotic.** He dropped a deep corporate navy for exactly
  that reason.
- **Textbook voice.** `FIG. 13 · DAPATLANTIC.COM, BUILT AND RUNNING` read to
  him "like a fucking textbook of a student".
- **Assertions instead of evidence.** And any comparative claim.

## 2.4 Less text, more impact

His standing brief, close to verbatim: the site should work like a picture book,
because clients and hiring managers will not read paragraphs. **Body text is the
caption, not the exhibit.** A reader should be able to take a chapter without
reading a paragraph: the year, a short verb phrase, one line. Every round of
copy should come out shorter than it went in.

## 2.5 Verification is visual, not code review

Judging by reading the diff is what shipped the scroll-jack. **Screenshot it and
read the screenshot.** Run the wheel test. Measure contrast rather than
eyeballing it. `tools/verify.py` exists for the mechanical half; the other half
is looking.

## 2.6 Concurrent sessions

More than one Claude chat has worked this repo in the same minute. Check
`CLAUDE.md`'s mtime before writing, prefer appending, and keep a standalone copy
of any large addition. `ROUND-5-MANDATE.md` exists because of this.

## 2.7 Git

**Since 2026-08-30 the folder is its own repo.** `git init` was run in it, the
first commit (`be95ad7`, 80 files, 8.0MB) is pushed, and `origin` is
`https://github.com/CodeByTitan/CodeByTitan.github.io.git`, created
**private** at his request. `git rev-parse --show-toplevel` now resolves
here. Before that date it resolved to `/Users/arshsethi`, the home-directory
repo (origin `CodeByTitan/SpetX.git`), and any git command run in the folder
acted on that repo. If a session ever sees that path again, stop: the `.git`
has gone missing.

What ships and what stays local is `.gitignore`'s job: raw font archives,
`_source/`, the personal-use display faces, `Gotham/` and the misnamed
`Android Studio.zip` (it is the Gotham archive; `unzip -l` shows only
`Gotham/*.otf`) stay out. The three staged TNR MT cuts and the woff2 subsets
in `assets/fonts` ship. `CLAUDE.md` is committed.

**Pages does not serve a private repo on a free plan.** The repo is named
`CodeByTitan.github.io` so that flipping it to public is the whole deploy:
Pages then publishes `main` at https://codebytitan.github.io with no rename.
Before that flip, decide what a public repo should carry: this file (candid
notes, his words), `FONT-LICENSE-DECISION.md`, and the shipped font files
(see 8.4). `gh` is not installed; the repo was created through the GitHub API
with the classic PAT (`repo` scope) that osxkeychain holds for github.com,
which is also what authenticates the push.

## 2.8 His keyboard inserts stray `d` characters

**His `d` key is loose and fires on its own**, before or after the character he
meant, so a stray `d` can land anywhere in a message. His words: *"my keyboard
has a loose d key so it keeps on typing d before or after."*

This is not cosmetic and it has already put a wrong fact on the page. He wrote
"dgc any1" while correcting the ANY1 origin story; that went into the copy as
the literal phrase, and the real one is **"gc any1"**. A whole round of copy,
plus a note in this file telling the next session not to gloss "dgc", was built
on a keyboard fault.

**How to apply:** an unexpected `d` next to a word is a typo until proven
otherwise, especially in a short quoted string, a name, or an acronym. The same
goes for other doubled or orphaned letters in his messages (he also writes
"usedd", "namd", "dso"). Never treat a malformed token as meaningful, and never
put one on the page or into this file. If a stray character would change a fact
that ships, **ask**: one question is cheaper than a wrong claim in an interview.

---

# 3. THE PROJECTS

Page order, and the weighting is deliberate: **this is a portfolio of many
projects, not a case study for one.** **As of 2026-08-29 ANY1 comes before
Cloots**: 00 hero, 01 journey, 02 ANY1, 03 Cloots, 04 Helv, 05 DAP, 06
Groundwork, 07 contact. Two reasons, both his: the portal's typed line
answers ANY1's closing sentence, the millionaire certainty, which only lands
if the reader has just left it; and the portal's approach band now darkens
the any1 night instead of the winter ground, a far smaller step into black
(*"that gradient transition would be much better then"*). The `#cloots`
section opens on `data-phase="any1"` for the same reason. Chapter numbers
and the HUD follow `data-chapter`, so renumber both attributes and the
`.micro` labels together when the order changes. Arsh's complaint about an earlier build,
close to verbatim: it "literally made the portfolio website another thing for
cloots to be displayed, which is just bullshit." Cloots is capped at two phases.
Weight is earned by what a project proves about him, not by how recent it is.

## 3.1 Cloots (flagship, two phases maximum)

**Two phases means two, and as of 2026-08-29 it is enforced in the markup:**
the portal, then `#brief` (the product: wordmark, hook, copy, the four stats,
**all six phone screens: Ask Cloots upright, the other five laid flat on the
loop** (4.5, "The loop"; until 2026-08-30 they were one 3 by 2 grid), the
engine as a short beat
with no panel and no phone, the four decisions), then `#ship`. His words:
*"reduce the phases of cloots down to 2. we got like three different web app
screens for this shit. lets not give algorithm its own screen and lets have
the 6 screens in mobile app we are showing distributed properly they look all
over the place right now."* Before that the chapter was three scenes after
the portal: the brief with two phones, a tinted rounded `.engine` panel with
the algorithm phone and the flow, and a rack of three more phones, then the
ship. The panel was the third "screen". The six phones run in the order a
session does: the feed recorded live, a card, the product page, then Ask
Cloots, the closet, and what the app learned. Two-up on a phone, because
one-up was six screen-heights of scroll.

**2026-08-30, the grid became the loop.** His instruction, with the Sobha
ring and an agency hero of flat isometric cards as references: *"can we have
our screenshots for cloots be used in the form of how It looks in the
screenshot above and they combine to form like an infinity sort of animation
... just leave this screen in place and use every other screenshots for the
laid flat screens animation."* "This screen" was the Ask Cloots phone (its
search bar carries the app's infinity button), which stays upright in the
chassis; the recording, the feed, the product page, the closet and the taste
model lie flat on a figure-eight beside it. The 3 by 2 grid's tidiness is the
thing the loop's static pose has to keep, because "distributed properly" was
his fix and the first build of the loop undid it (4.5). The unreferenced
`cloots-app-*.jpg` set is a duplicate of `cloots-screen-*` (checked frame
against frame), and `cloots-screen-home-feed.jpg` is a seventh screen the
live site does not render, so neither joined the loop.

**The fourth stat, 2026-08-30.** "1 / DESIGNER ENGINEER" became
"1,000+ / EXTERNAL TESTERS" on his instruction: *"instead fo 1 designer
engineer, put 3000+ users externally tested or tested by 1000+ external users,
something along those lines."* He gave two figures in one breath. The smaller
went on the page because it is true under either reading, and 8 carries the
question; put 3,000+ in only when he confirms it. The odometer takes the
comma and the plus as still columns, the way it takes the M in 1M+. The
sole-credit line ("Designed and developed solo") already carries what the
retired stat said.

- Role, exact: **Co-founder & Lead Engineer**. Never "Founder": he has
  co-founders. May 2025 to present.
- **The honesty line, which must survive every rewrite:** "Designed and
  developed solo. / Shipped as a team. / Très beau." (Earlier wording was
  "Designed by me. Built by me. Shipped by us." He changed it; the *meaning* is
  the invariant: sole credit stops at design and build, the venture and the
  shipping are a team. `tools/verify.py` checks the current wording.)
  "Très beau" is masculine singular, agreeing with the work.
- AI-powered fashion/streetwear discovery app. iOS + Android, in App Store and
  Google Play review. cloots.ca built in React.
- The product: a swipe feed over a **1M+ product catalog** (his figure,
  2026-08-29: "change the catalog numbers to be 1M+ products"; it was 63,000+
  until then, and the old number must not come back through an old draft or
  the JobClanker resume pool). Swiping teaches
  it your taste in real time (OpenAI embeddings + MongoDB Atlas vector search);
  the taste model rebuilds itself from stored history if state is lost. Semantic
  search combines LLM query expansion with vector and keyword retrieval, ranked
  in about **1.5 seconds**.
- Engineering: Flutter client (Riverpod, freezed, Hive), ~40 TypeScript
  serverless functions on MongoDB Atlas, Firebase (Cloud Functions v2, Auth,
  Firestore), Shopify catalog pipeline with daily currency normalisation, Google
  and Apple Sign-In with per-user data isolation, App Store submission and code
  signing, Jest + flutter_test coverage.
- Design argument: dark streetwear aesthetic where the clothes are the only
  colour; motion is feedback not decoration; empty/failure/offline are designed
  screens; first-session clarity.
- **The real wordmark carries the brand**, the one whose "oo" is an infinity
  ligature. Never typeset "Cloots" in italic beside it: *"it does not have the
  infinity. I want the infinity."*
- The keyhole scene dives through the **logo**, an infinity loop as the portal,
  using the white-glyph wordmark as an SVG luminance mask. It is now **the
  portal**, a full-bleed takeover on a black ground with no chrome: see 4.5 for
  the storyboard and why every beat is where it is.

### Cloots screenshots: one source, one device, never mixed

**Every Cloots screen on the portfolio comes from the cloots.ca repo and
nowhere else.** Arsh caught the earlier set: *"The screens that are being used
for cloots are not the ones that we are using in Cloots website... don't use
mixed devices for Cloots."* He was right twice over, in content and in geometry.

**The repo is `~/Desktop/cloots-web-app`** (github dev090/cloots-web-app), not
`~/Desktop/ClootsWeb-main` (github Param21Sidhu/ClootsWeb), which is what gets
pointed at by name. ClootsWeb-main is older, its `HomePage.jsx` renders only
Navigation, StartupAnimation, HeroText, Waitlist and Footer, and its
`PhoneShowcase` component is unused scaffolding whose copy still says "Drop in
your simulator export". **The whole built site there ships exactly one image, the
text logo.** It has no app screenshots at all. `cloots-web-app` is the one with
`PhoneFrame.jsx`, and that file is where the `.mock-phone` / `.mock-screen` /
`.mock-island` chassis in 4.5 was ported from.

The five stills the live site actually renders, and where:

| cloots-web-app | section | portfolio |
|---|---|---|
| `images/homeimg.png` | Discover | `cloots-screen-swipe-feed.jpg` |
| `images/proddetails.png` | Discover | `cloots-screen-product-details.jpg` |
| `images/search.png` | Discover | `cloots-screen-ask-cloots.jpg` |
| `images/algorithm.png` | HowItWorks | `cloots-screen-algorithm.jpg` |
| `images/closetdemo.jpg` | HowItWorks | `cloots-screen-closet.jpg` |
| `screens/swipe.mp4` | HowItWorks | `cloots-swipe-demo.mp4` + its poster |

`images/swipe-extra.png` exists and is referenced nowhere on the site, so it is
not used here either. `screens/{2,8,9,10}.png` are a second consistent set at
1206x2622; same aspect, also unused by the live site.

**The geometry is the part that was actually visible.** Every source in that
folder is **1320x2868**, one iPhone simulator, ratio 1:2.173, which against the
chassis's `aspect-ratio: 9/19.5` (1:2.167) is a match to within a fifth of a
percent. The set that was on the page instead was 900x1847, 900x1810, 900x1947
and 720x1386: **four different aspect ratios**, which is what "mixed devices"
looks like from the outside. It had already forced a workaround, an
`object-fit: contain` exception for the three worst offenders, because cover was
amputating their UI text. Fixing the sources deleted the need for it. The stills
are now 900x1955 and all six frames render on `cover`.

The recording is the one that still needs containing: the site ships it at
1080x2200, which is 1:2.04.

**Rules for the next round.** Take a Cloots screen only from `cloots-web-app`
and only one the site renders. Downscale to **900 wide** (the frame is at most
300 CSS px, so 900 covers a 3x display) and keep it under the 350KB image cap
that `tools/verify.py` enforces. Regenerate the video poster from frame 0 of
whatever video is installed, or the poster and the first frame disagree and the
phone flickers when it starts. And check the alt text against the picture: the
old ask-cloots alt described a raised keyboard that the shipped screen does not
have.

## 3.2 ANY1 (own screen, and the emotional spine; chapter 02, before Cloots)

**This is the origin story and it carries more weight than its scale suggests.**
His account, in his words:

- **His first genuine app, built with his bare hands, back when there was no
  AI.** He has not written code manually in a long time, which is exactly why it
  now reads as a genuine feat.
- It was **a literal copy of Instagram**. He says this himself and he is proud
  of it, not embarrassed. He copied the menu cards, the chat page, the profile
  page, and **the double-tap-the-avatar account switch, and it worked.**
- **He had no idea design resources existed.** No Dribbble, no Awwwards, no
  Behance. His method was to **download other apps and use them as his
  benchmark.** That naivety is the best line on the page and it must be told
  plainly.
- **The name comes from an Instagram comment, not from inside a group chat.**
  Corrected by Arsh on 2026-08-29. The original page copy said the way in was to
  post "gc any1?" **into a bigger group**, which was the wrong venue. What
  actually happens: people comment **"gc any1"**, or **"gc anyone"**, or
  "random gc anyone", **under somebody's Instagram post or reel**, and wait for
  a stranger to add them. The wording varies, the question does not. That is how
  he got into the chats he was in, he says people still do it today, and it is
  where **ANY1** comes from. The app's own launch screen reads **GC ANY1**, so
  copy and artwork agree.
  **Trap, and it cost a round:** the correction arrived as "dgc any1" and went
  onto the page that way. There is no d. See 2.8.
- **The gap was search, and he checked before building.** In his words: Telegram
  surfaced only three or four groups a search and the ones he found were for
  downloading things rather than talking in; Reddit had communities you post to
  rather than chat in; Discord had the servers but they are hard to find from
  the open internet. That research beat is now the second paragraph of the ANY1
  copy, and it is the reason the product exists, so do not cut it for length
  without asking. **He is unsure whether Reddit has since added group chat
  ("i think"), so that must never be stated on the page**: same rule as the
  Java I superlative in 1.2.
- **He thought he was going to become a rich millionaire from this one app.** No
  idea about product market fit or marketing. He says this about himself and
  wants that self-aware voice on the site. **On the page since 2026-08-29** as
  ANY1's last sentence, "I was certain it was going to make me a
  millionaire.", which is the setup the portal's line answers. Keep it last:
  the reader has to carry it into the black.
- **He built it shut in.** A couple of months barely leaving the house, working
  at night with the lights off. That is what the `any1` phase is: the darkest
  ground on the page, a night sky with stars.
- Why it matters: **it actually worked.** He could hand it to a friend and they
  could really use it. That is the bar most student projects never clear.
- Stack: Kotlin, Firebase, Dagger-Hilt. 2022, first year.

His own public README on `CodeByTitan/Any1-updated-` already says "profile
switch feature similar to Instagram" and "chat page built similar to instagram",
so the honesty is on the record and safe to quote.

**The video assets.** Two raw screen recordings live as GitHub release assets on
`Any1-updated-`, archived at `_source/any1/` (gitignored). Both are Android
emulator captures; the app screen is exactly `crop=476:868:773:84` of the raw
1920x1080 frame, which excludes the emulator skin, the Android Studio toolbar
and the black bars. Three clips ship:

- `any1-launch.mp4` (video A, t=0.3, 7s). The launch screen's meme wall is
  **animated**, which a still could never show.
- `any1-switch.mp4` (video B, t=33.5, 7s). The profile double tap, the account
  sheet sliding up, Add account, a second account signing in. The Instagram
  feature he copied, on camera, end to end.
- `any1-demo.mp4` (video A, t=16.6, 8s). Profile, settings, the dark mode
  toggle.

Scrubbed: the test email `oko607283@gmail.com` is legible on the login frames
and is outside every clip. The avatars and messages belong to real people from
his group chats; keep faces small.

The figures use `.mock-phone--a`, the same chassis as Cloots at the aspect of
the phone it actually ran on, **with no dynamic island**, because an iPhone
island over an Android status bar reads as a bug. The argument was always the
chassis: a 2022 first app and a 2026 shipped app in identical chassis is a
silent statement about the arc, and it costs nothing.

## 3.3 Helv (own screen)

- Android app, Kotlin + Firebase, **classic Android views, not Compose. Never
  list Compose for Helv.** Sept to Dec 2025, fourth-year mobile dev course.
- github.com/CodeByTitan/Helv (public; renamed from HandyHub, so code and
  package still say handyhub).
- Books on-demand home services: browse categories, choose a job, book it.
- Wording: **"Designed and implemented the full application"**, interface
  through to the Firebase data model. See the sensitivity note in 1.2.
- **The grade is the exhibit, not the app.** A+ set at `clamp(104px,17vw,240px)`
  next to the feedback that mattered: it was further along than the stage asked
  for. The honest reason is stated on the page and it is a better story than
  talent: reuse. He had already shipped apps, so he arrived with the components
  built and spent the term on the parts that were hard.
  - **"Fidelity" is the right word.** He thought it was wrong. It is exactly the
    term a design professor would use: high fidelity means closely resembling
    the finished product.
  - The feedback is never quoted, because the exact wording is not known. It is
    described.
- Tagline: **"A school project that forgot it was one."**
- Six Pixel 9 Pro screens at `assets/helv/`, in journey order: home, provider,
  jobs, job detail, messages, profile. `.mock-phone--p9` is the chassis at
  1280/2856. Originals in `_source/helv/`.
- Repo note: it was private with world-readable Firestore rules; auth-only rules
  were drafted before he made it public. If the repo gets promoted harder,
  verify the rules were actually applied.

## 3.4 DAP Atlantic Tech Inc. (own screen)

- Role on the portfolio: **Full-Stack Developer.** He is also a director; his
  decision was to lead with the developer title publicly and disclose the
  directorship honestly when a form asks. **Do not print "Director" on the
  page.**
- Sept 2025 to present. Registered digital agency, web/app/branding for small
  businesses across Atlantic Canada.
- Tagline: **"Where the deadline belongs to somebody else."** That is the actual
  difference between client work and personal projects, which is why it works
  where "Client work, scoped and shipped" did not.
- Named deliverables, presented as two cards: a restaurant redesign with a
  data-driven menu system and an accessibility pass; a marketing site for an
  immigration consultancy with a live news feed powered by an LLM API.
- Stack: React, TypeScript, SASS/SCSS, HTML5, CSS3. Shown as chips, not a
  definition list: the stack is what a technical reader scans for and a
  lab-report row buried it.
- `assets/dap/dap-site.jpg` is dapatlantic.com captured live.

## 3.5 SQLDB and Angular (paired, smallest)

Both live in the Groundwork chapter's drag strip.

- **SQLDB**, 2023. Java Android app exposing complex SQL database operations
  through a mobile UI: the interface, the database interaction layer, the
  operation workflows. MySQL. **Built in 12 hours, and the speed story is real
  and confirmed.**
- **Angular coursework.** One full university course (4 months; **do not state
  the duration**, list the work): several web applications, some solo, some
  team, including front ends wired to a REST API with authentication.
  TypeScript, SASS. Not on GitHub.

## 3.6 UNBDine: a journey beat, never a project screen

Rejected as a project by Arsh, kept as a story on his agreement.

- The most serious thing he was considering as a starter project after arriving,
  while in Saint John.
- The problem was lived: he was in residence, and at peak hours around 10 to
  11am the cafeteria filled up. You paid at the cashier then waited in a long
  line. He and plenty of others **would turn back at the line and not eat.**
- The product followed: order from class, pay online, food ready when class ends.
- **He shut it down** when he learned the cafeteria was being renovated into a
  buffet. The premise no longer existed.

**The app is not the interesting part. The judgment is.** He found a real
problem from his own life, started building unprompted in his first year in a
new country, and killed it on evidence. Most people at that stage keep building
because stopping feels like failing. It also makes Cloots look like a pattern
rather than a fluke, which is the only evidence on the page that the instinct
predates the company.

Fences: journey chapter only, next to the first-winter photo. Never a card,
never a repo link, never a screenshot. Two or three sentences, not the full
account. **Never call it a failure and never explain the shutdown at length**;
explaining reads as defending.

## 3.7 Explicitly not on the portfolio

- **Grinners Food Systems** (2023 food-service job): real work history for
  application forms, not portfolio material.
- **LiQart, RideShare, BudgetMaster, DialogPracticeApp, dineadmin.** Arsh's
  verdict, quoted in spirit: they are "totally shit", none deserve to be on the
  site. **Do not reopen this.**
- Anything implying **CI/CD experience** (he has none), React years beyond what
  cloots.ca and DAP evidence, or any tool he has not used (**no Figma claims**).

---

# 4. THE DESIGN SYSTEM

## 4.1 The phase engine, the spine of the page

**The page is a journey and the journey is told in colour temperature.** This is
the single most important structural idea in the build.

Sections declare `data-phase`. One table, `PHASES` in the script, holds the
ground, the gradient over it, the ink that ground can carry, the accent, the
panel and card tones, and the particle field. **Nothing else in the file paints
a background**, so adding a chapter is adding a row.

| phase | ground | ink | carries |
|---|---|---|---|
| `frost` | `#FFFFFF` with a slanted seam to `#9ae0ff` | `14,20,24` | hero, faint snow |
| `winter` | `#DAE7F2` over `#EDF5FB → #7CA4C7` | `12,26,40` | journey, full snow |
| `portal` | `#000000`, no gradient | `234,246,255` | the black stage for the Cloots logo |
| `cloots` | `#FBFEFC` + green radials | `12,26,20` | the flagship |
| `any1` | `#05070E → #1B3563` | `226,238,255` | night, stars |
| `helv` | `#FFFBEF` + amber radials | `32,24,6` | the school year |
| `dap` | `#F5F9FC` + one cool radial | `12,22,32` | client work, groundwork |
| `hope` | `#FFF9F0 → #FFAF69` | `34,20,6` | the close |

**The winter row is sampled, not invented.** `assets/arsh-first-winter.jpg` is
entirely hue 201 to 221: `#082B56` for the turban and hoodie, `#99B6D0` and
`#C9D9E9` for the snow and sky. His photograph already was the palette, which is
why the frost of the hero lands on the winter ground with no seam and why the
photo dissolves into the page through a mask instead of sitting in a frame.

Four things are load-bearing:

1. **The phase pick is one decision, not one trigger per section.** Independent
   ScrollTriggers overlap on short sections and whichever fires last wins; that
   is how Helv never got its phase at all, because DAP was inside the band at
   the same moment. The section we are in is **the last one whose top has
   crossed 0.42 of the viewport**: deterministic, and it cannot gap between
   sections either.
2. **Two wash layers, not one.** CSS cannot tween a gradient, so a phase change
   paints the incoming gradient on the idle layer and cross-fades the pair.
3. **`--bg-rgb` is derived from the interpolated ground**, not held in the
   table. Every scrim on the page is built from it (the nav, the HUD, the chip
   fills). It used to stay on the frost value for the whole scroll, so the menu
   wore a cold white wash over a sunrise.
4. **It runs under reduced motion**, with the tween collapsed to 1ms. Changing
   colour is not motion and the story is in the colour. Without GSAP the page
   stays on `frost`, which is dark ink on near-white and readable everywhere, so
   the failure mode is safe by construction.

`tools/verify.py` fails if a `data-phase` is used that `PHASES` does not define.

**Two things the portal added to the engine, 2026-08-29:**

- **`cloots` is no longer declared anywhere in the markup.** The `#cloots`
  section opens on `winter` (the approach band does the darkening in flow), and
  the pinned frame `#khFrame` carries `data-phase="portal"`, then **relabels
  itself `cloots` at 78% of the pin**
  from the scene's `onUpdate` (and back to `portal` on the way up). The
  geometry rule reads the attribute live, so the two never disagree; the scene
  calls `phaseAPI.go(want, 0.55)` and then `phaseAPI.pick()`, which picks the
  same phase and is a no-op. The `phaseAPI` object exists for exactly this and
  nothing else should reach through it. `verify.py`'s guard therefore lists
  `portal` but not `cloots` in "used": that is correct, not a gap.
- **`go(name, dur)` takes an optional duration.** Only the portal passes one:
  it hands the ground over in the last quarter of a pin, under a dissolving
  frame, and the full 1.05s left the brief's ink mid-grey on a mid-grey stage
  after a fast flick. Everything else takes `DUR`.
- **Under reduced motion `portal` is painted as `cloots`** (`go()` maps it).
  There is no pin and no relabel in that state, so the black stage would have
  sat under the brief's dark ink for most of a viewport. The frame paints its
  own black in CSS, so it is a black poster on the Cloots ground there, and the
  section reads.
- **The nav scrim toggle (`is-scrolled`) now runs before the reduced-motion
  return.** It is legibility, not motion. Inside the animated branch it left the
  reduced-motion nav with no scrim, transparent, ink-coloured links over a
  black frame for a full viewport: the menu vanished.

## 4.2 The frost palette, and why it moved

Arsh gave three frosty blues to replace a deep navy that read robotic:
`#9ae0ff`, `#70d3ff` (his pick), `#23bbff`.

**Measured against the page, all three fail as an accent on light ground:**
1.42, 1.65 and 2.14 to 1. Below the 3:1 floor for UI parts, let alone text. A
straight swap makes every accent moment look like disabled placeholder text.

The resolution: **make the accent a scale, not a hex.** `#0B5D8A` is the same
hue driven dark, 6.98:1 on a near-white page, and carries links, rules and
labels. `#70d3ff` is his exact colour and owns the dark phases, where it
measures 11.5:1. Nothing was compromised; it was relocated.

The structural consequence is the gift: to use frost blue properly the page
needed dark grounds, and that is what became the phase engine.

## 4.3 The type stack: one face, one job

| face | job | how it ships |
|---|---|---|
| **Boreck Display** | his name, and nothing else | SVG outlines |
| **Editor's Note** | the hero line and project taglines | webfont, 42KB |
| **Lumiare** | project names | SVG outlines |
| **Inter** | statements, headings, subheads, labels, nav, buttons | Google Fonts |
| **Futura PT** | body copy | webfont, 20KB |
| **Space Mono** | figures, captions, data | Google Fonts |
| **TNR MT Bold Italic** | timeline keys, the ship board | self-hosted |

**The rule that governs additions: a face earns a slot only by doing a job no
face already present can do.** Count is not the problem and never was. Two faces
sharing one job is the problem, because then a reader cannot infer the system
and the type reads as decoration rather than structure.

Test it this way: could a stranger scrolling for ten seconds tell you what each
font is for?

Faces that failed that test and are gone:

- **Switzer.** Its only job was structural headings, and set beside Inter Bold
  at 48px they are nearly indistinguishable. Arsh's own instinct to reach for
  Inter is what exposed it.
- **Munich Sans.** 55 glyphs, letters only: no numerals, no comma, no period, no
  middle dot, no ampersand. Tested against all 105 mono-voice strings on the
  page, **76 break**. The mono voice *is* figures and separators. It briefly
  held the field labels and was pulled: on a dark ground a single light weight
  at `--ink-60` was barely readable, and under 60px numerals it could not hold
  the weight.
- **Bemore Serif.** Held the hero line for about an hour before Editor's Note
  replaced it. Arsh does not like it.
- **SF Pro** and **Helvetica Neue**, both superseded on the body.

**Constraints worth knowing:**

- **Boreck is unicase.** Lowercase renders as the same capitals, so `Arsh Sethi`
  always sets as `ARSH SETHI`. Its ampersand is broken, which is why the
  designation line is never set in it.
- **Lumiare's numeral one reads close to an I**, so `ANY1` looks like `ANYI`.
  Tracking was raised to 0.05em and the surrounding labels carry the name in
  Inter. Open if he wants it solved differently.
- **Futura Book's x-height is 415/1000 against Helvetica Neue's 516**, measured
  off the files. It reads about 20% smaller at the same pixel size, so every
  body-level size went up by ~1.18 when it landed: body 17px to 20px, leading
  1.65 to 1.58, plus `letter-spacing:.004em` because a geometric sans wants air
  at text size. **A straight family swap would have silently shrunk every
  paragraph.**
- Futura is a display face and long passages in it are genuinely harder to read.
  What makes it viable here is the copy diet: short paragraphs by design.
- **The Futura subset is named FIRST in `--sans`**, unlike the Helvetica Neue
  build which preferred the system copy. macOS Futura and Futura PT are
  different cuts, so preferring the local one would render this page differently
  on a Mac than on Windows. 20KB. Everyone gets the same page.

**Gotham Black, one job: the line at the Cloots door.** He supplied the
files himself (`Gotham/`, gitignored, fourteen cuts) and asked for it by name
the same day Anton went in: *"i added gotham font use that instead"*. Only
`assets/fonts/gotham-900.woff2` ships, cut by `tools/mkwebfonts.py`. **Gotham
is a commercial face (Hoefler&Co).** The files are his; whether the licence
he holds covers web embedding is his to confirm, and it is the same open
question 4.4 already carries for Editor's Note and Futura. Do not add other
Gotham weights to the page without that answer. The line is set uppercase,
`font-weight:900`, `letter-spacing:.01em`, `clamp(34px,5.6vw,88px)`, on a
15ch measure so it breaks into two lines.

Anton stays cut and declared (`anton-400.woff2`, `@font-face`) as the
fallback in the portal line's stack. It was the first answer to the same
instruction ("we need a bold font. something that matches cloots font. what
font are we using in cloots website for the main page, maybe use that").
cloots.ca sets its body in Raleway and its showcase headlines (`.big-head`,
the Discover and "Meet your next favourite brand" panels) in **Anton**, from
Google Fonts, uppercase, `letter-spacing:.015em`, `line-height:1.04`. The
portal's typed line is set exactly that way. It is the Cloots brand's own
headline voice quoted at its own door, which is why a sixth face is allowed
on a page whose rule is one face, one job: the job is "speak as Cloots for one
line". Never use it anywhere else. SIL OFL 1.1; the source and licence live in
`anton/` (gitignored) and `tools/mkwebfonts.py` cuts `assets/fonts/anton-400.woff2`
(23KB) from it. SF Pro Text, which cloots.ca also ships, is Apple-licensed and
must never be copied here.

## 4.4 The outline pipeline

Boreck, Lumiare and (formerly) Bemore are personal-use demo fonts. Shipping the
`.otf` on a public repo redistributes it. So **the display strings are converted
to SVG paths once** by `tools/mkglyphs.py` and inlined. No font file ships, no
FOUT, identical rendering everywhere.

Two mechanics that cost a debugging round each:

- **One `<path>` per glyph, never a concatenated `d`.** With fill-rule nonzero,
  two overlapping glyph outlines cancel and punch a hole. Boreck's S tail did
  exactly that through the E in SETHI.
- **Size by height with `width:auto`.** An inline `<svg>` with a viewBox and no
  width attribute defaults to 100% of its container, which made the hero name
  fill the viewport on the first attempt.

The hero line, when it was Bemore, used **one SVG with two `<g>` groups** rather
than two SVGs, because "ship." needed its own colour tween and two separate SVGs
need hand baseline alignment that drifts at every viewport. That pattern is
worth remembering even though that line is live text now.

`tools/mkwebfonts.py` subsets the real families (currently Futura) by **unicode
range, not by the characters on the page**: `--text` would silently drop a glyph
the first time a line of copy is edited.

### Font licensing: settled for two faces, open for two

**Boreck and Lumiare are settled. Do not re-raise them.** Both are personal-use
fonts, a portfolio is commercial use under how most indie foundries read that,
Arsh was told, and he chose to ship. See `FONT-LICENSE-DECISION.md` for the
full reasoning. The residual risk is genuinely small **because they ship as
outlines**: no font file is redistributed, and typeface *designs* are
uncopyrightable in the US and Canada (Eltra v. Ringer) while font *software* is
(Adobe v. SSi). Shipping shapes is not shipping software.

**That premise no longer covers the whole page, and this is worth a look.** That
document's own words for the one thing that would break the argument were
"never commit the font files". Since it was written, four faces have started
shipping as actual files in `assets/fonts/`:

| face | ships as | licence |
|---|---|---|
| Editor's Note | 4 woff2 | "Demo for Personal Use", ifonts.xyz |
| Futura PT | 3 woff2 | Paratype commercial, no licence bundled |
| TNR MT Std | 3 otf | Monotype commercial (predates this work) |
| Boreck, Lumiare | outlines only | settled, see above |

**Editor's Note is cheap to fix and Futura is not.** Editor's Note sets four
short strings (the hero line, two taglines, the close), so it can be outlined
the same way Boreck and Lumiare are and the exposure goes to zero. Futura is
body copy across the entire page and **cannot** be outlined; it either ships as
a file or is replaced with something licensed for web use. This is Arsh's call
in exactly the way the first one was, but he should make it knowing the premise
changed rather than inheriting a "settled" note that was settled about a
different situation.

## 4.5 Components

- **The phone chassis** is ported byte-for-byte from his Cloots web app
  (`.mock-phone` family): titanium rail gradient, action/volume/power buttons on
  the rails, 2.6rem screen clip, dynamic island. Only permitted adaptations: a
  page-relative drop shadow and no green glow layer. His verdict on an earlier
  CSS approximation: *"entirely garbage."* Use his chassis. Variants:
  `.mock-phone--a` (476/868, ANY1) and `.mock-phone--p9` (1280/2856, Helv), both
  without the island because those are Android captures.
- ~~**The keyhole is a panel, not a takeover.**~~ **Reversed on his
  instruction, 2026-08-29.** His words: *"instead of showing that as a
  rectangular, I want you to transition our previous phase into a complete
  black gradient that sets up the stage for the cloots logo, no need to show
  case study or whatever, I say we turn it pitch black and then the cloots logo
  starts blinking pure white, this obviously happens through the scroll, then
  the pure white logo fades out a bit to show the screens underneath and then
  we can do the zoom in transition that then forms a base path to the next
  phase showing cloots swipe feed for streetwear."* The old panel note stays
  visible because the reason it was a panel ("the one hard edge on the page")
  is the reason the takeover has to be built the way it is: **the ground goes
  black first**, through the `portal` phase, so the frame arrives into black
  and there is no edge to read. A full-bleed black frame on a blue ground would
  have been the rectangle he was objecting to, only bigger.

  **Revised the same day, and this is the version on the page.** His second
  message: *"this transition from the winter to this darkness needs to be a
  much smoother transition, like it should blend through gradients or whatever
  like all the other phases do, and instead of making Cloots flicker, i would
  rather that you do typewriter effect for something else like give it a good
  name or subheading, we can discuss what that can be later, choose something
  for now and then that heading then erases in the typewriter effect and we see
  cloots logo fade in with the exact same transition that we use in our
  website splash screen... I would say remove the flicker effect. during this
  we absolutely hide the top menu bar."* Three decisions came out of it:

  - **The darkening is in the page flow, not a time cross-fade.**
    `.portal-approach` is a 72svh band before the frame, transparent to black,
    so the reader scrolls THROUGH the blend. It was over the winter ground with
    the snow behind it; since ANY1 moved ahead of Cloots it is over the any1
    night with the stars, and the step into black is small. The `#cloots` section opens on
    `winter`, and the stage only cross-fades to black when the frame's top
    crosses the 0.42 line, by which point the band above it is already dark
    and hides the fade. A whole-viewport cross-fade to black had been tried
    first and read as a cut: it is a luminance jump no other phase change makes.
    The band paints a background, the one exception to 4.1's rule, because it
    is the transition rather than a ground.
  - **The line is Cloots's own.** "Meet your next favourite brand." is the
    heading of the cloots.ca MeetBrand section, Canadian spelling included, so
    it is provably his copy and not a claim about him. **Placeholder** by his
    instruction ("choose something for now"); see 8.
  - **The logo arrives the way cloots.ca's splash brings it in.** Read out of
    `cloots-web-app/src/components/startup-animation.css`: two elliptical
    clip-paths growing from the top corners of the logo box
    (`hingeRevealLeft/Right`, `ellipse(0% 0% at 0% 0%)` to
    `ellipse(150% 150% at 0% 0%)`), nested, so the visible region is their
    intersection and the wordmark opens from its top centre outward, with a
    fade over the first tenth and a white drop-shadow glow that peaks and
    settles. Here they are two `<clipPath>` ellipses in user space wrapping
    the solid `<image>`, sized by `layoutKeyhole` and grown from zero by the
    timeline, so the fall scales them with the logo. Nothing is visible until
    each ellipse reaches the box's centre, which is true of the splash too;
    it is the dark beat before the bloom.

  **The clock is 4.35s and the line is typed in one second.** His notes
  on 2026-08-29, in order: *"i want it to be smooth and just make it have a
  pause after delivering the whole line and then we want the transition to
  cloots quickly as possible"*; *"less pause on completion"*; *"why are we
  not pausing at "be" we need to pause and flicker the typewriter there
  once"*; *"increase the duration of typewriter to 1 second then, increase
  the pause at be"*; *"make the pause at be exact same as the one we have
  in our starting page line."* So: `AUTO_MS` 4350 on a precise pointer, and
  in timeline fractions: caret 0.0115; "THIS MIGHT JUST BE" typed 0.023 to
  0.179 (0.68s) and "THE ONE." 0.317 to 0.391 (0.32s), 22 glyphs at 45ms,
  1.0s of typing; between them **the hero's beat**, 0.6s with the caret
  blinking twice (`HOLD/4` yoyo, repeat 3, the hero's exact tween, `HOLD`
  converted to a fraction of the clock); then the caret blinks on the whole
  line to 0.527 (0.6s) and the line fades out 0.529 to 0.587 (no
  glyph-by-glyph erase; `typed.n` is set to 0 at 0.59 under the faded line
  so a reverse scrub still works); logo and hinge 0.591, screens 0.706, fall
  0.775 to 0.959, dissolve 0.931 to 1.0, nav 0.94 on the ground's timeline,
  `FLIP_AT` 0.87. In seconds: line done at 1.70, held to 2.30, logo at 2.57,
  screens at 3.07, fall 3.37 to 4.17, brief at 4.05.

  **The glyphs bloom and the caret glides**, the hero's two devices,
  after a 20-agent review of the 8s build rated the 0-to-1 pops and the
  `gsap.set` caret jumps as the visible half of "jittery". A single step in
  `showUpTo` tweens the one glyph that changed over 0.12s (at 45ms a glyph
  that is a soft edge two and a half glyphs wide); a first paint, a refresh
  or the snap to zero sets everything flat. `placeCaret` is its own
  function, glides over 0.10s, and jumps only on those flat paints or a
  row change; `onRefresh` calls it unconditionally, one frame later
  (inside a resize-triggered refresh the pinned frame is still mid
  relayout and the rects put the caret on a row the line did not end up
  having, measured at 390 to 350px), because on a cold load
  the first placement is measured against the fallback face (Gotham is
  font-display swap) and the old refresh hook returned before reading a
  rect, so the caret sat at the fallback's x and height until the first
  glyph. A `ResizeObserver` on the line re-places it too, after layout,
  with the final rects. And an instant placement first kills the caret's
  positional tweens: a resize mid-pin shifts the scroll, the progress
  jumps, the chase types forward and erases back while the refresh corrects
  the pin, and a `gsap.set` for a row change raced a glide still running,
  which kept rendering and won (measured at 390 to 350px: caret one row
  off, `caretRow` saying otherwise).

  **The nav fades out over the approach, not at the pin.** Arsh, on the
  3.6s cut: *"the top bar should slowly fade out at this point. currently
  its not, its just randomly going off as of now."* It used to be switched
  off in the first 2% of the pin. Now it is a tween on the ground's
  timeline, `autoAlpha` 1 to 0 over the second half of the approach share
  (`A * 0.45` to `A * 0.95`), so it goes as the marbling comes up and is gone
  before the frame pins. It returns at 0.94 of the pin **on the same
  timeline**, through a `fromTo` with `immediateRender: false`. Both
  halves were on different timelines for one build and disagreed after a
  reload restored below the portal: the nav came up hidden on the Cloots
  brief and visible inside the pin. One property, one owner. And the
  `fromTo`: a plain `to()` records its start value on first render, and a
  page restored below the portal renders that at progress 1 with the nav
  visible, which left it visible through the whole pin on a reverse scrub.

  **The ground is a fixed layer behind the page, and it fades in already
  moving.** Arsh, later the same day: *"even during the transition from any 1
  to the black thing/image, we need to fade in the image and it should already
  be moving, it should not be still at the start."* So `.portal-ground` is
  `position:fixed`, z-index -1 (above the stage, under everything in flow),
  with its own scrubbed timeline from the approach band's top entering the
  viewport to the end of the pin: opacity 0 to 1 across the approach (over
  the any1 night and its stars), held, then out with the dissolve; the pan
  runs the whole way and the breath plays whenever the layer is in range. The
  band no longer paints black; the moving image is the transition. The frame
  is transparent in the animated state (`.js-anim .keyhole`) so the ground
  shows through its glyphs, and **the brief is `autoAlpha` 0 beneath it until
  the dissolve** or it would show through too; in the static states the frame
  keeps its own black. Everything below about the pan and the breath still
  holds; only the element moved.

  **The ground under all of it is his liquid-marbling texture, moving.**
  Arsh, 2026-08-29, with a reference (an Instagram poster, a motion-blurred
  photo with GOTHAM set over it): *"i added a liquid marbling painting texture
  image, use that in the background for this instead of pitch black, add a
  little blur to it ... and I want this blur to keep moving as user is
  scrolling."* How it is built:
  - The blur is **baked, not filtered**: `tools/mkportalbg.py` takes
    `_source/marbling/original.jpg` (6000x3000, gitignored) to
    `assets/portal-bg.jpg` (1920x960, ~52KB) with a horizontal smear (squeeze
    the width, box blur, stretch back) and a light gaussian. A CSS or SVG
    filter on a full-viewport layer would re-render every frame; a transform
    on a pre-blurred image is a compositor move. The texture is monochrome,
    thin white ribbons on black: the first bake (90px streak, 35% overlay)
    erased it, so the streak is short (~18px) and the ribbons are lifted 25%.
  - `.portal-bg` (14% oversize a side) **pans on the scroll** across the
    whole pin, xPercent -7 to +7 and scale 1.06 to 1, scrubbed; inside it
    `.portal-bg-img` **breathes on the clock** (a 9s yoyo, 1.6% x, 1.2% y,
    3% scale) so the ground never reads as frozen when the reader stops. Two
    nested elements because two tweens on one transform overwrite each other.
    The breath is paused whenever the frame is off screen.
  - The `::after` overlay fades to black along the top so the approach band's
    black runs into the frame with no edge, and darkens the middle only 12 to
    18% so the white Gotham still clears the brightest ribbon.
  - The mask's black base now reveals the texture rather than black, so the
    fall goes into the marbling, not into a void; the dissolve is unchanged.

  **The portal, beat by beat** (the numbers are pin progress; the pin is 1.6
  viewports on desktop, 1.3 on mobile, `pinSpacing:false`, plus a
  `.portal-tail` of 60svh / 30svh so the brief's top meets the viewport top as
  the black clears; the pin's `end` is read off the DOM as frame plus tail):
  - 0.00 to 0.02, the nav goes (`autoAlpha`). It returns 0.94 to 1.00, already
    in day mode, and scrolling back up brings it back the moment the reader
    leaves the pin. The HUD is left alone; he named the top bar.
  - 0.02 to 0.40, the line types. **There is no black beat first**: he found
    that a pitch-black screen is an invitation to scroll faster, and blew
    straight through the typing ("I couldn't even stay at it"). Anton, white,
    uppercase, centred, per-glyph spans like the hero's, a proxy `{n}` tweened
    with `ease:'none'`, caret placed from the last visible glyph's live rect.
  - **The typing is scrubbed AND capped on the clock.** The glyph count on
    screen chases the scrubbed target one glyph per 45ms on `gsap.ticker`, so
    a flick cannot type the line in three frames; it lands where the scroll
    is, at reading speed. Three rules, each paid for by a measurement: outside
    the pin and past 0.58 the count **snaps** to zero (walking it down left
    four glyphs lingering into the logo for 14 frames); the line **types to
    full before it may erase** (without that a trackpad pass showed four
    glyphs and then nothing, the scrubbed target already falling before the
    chase had caught it); only then does it follow the target down. Measured
    before any cap: a normal trackpad pass typed and erased the whole line in
    under 0.3s. What this cannot do is hold the scroll: a reader who flicks
    from black to past 0.58 in under 1.2s never sees the line, which is the
    correct outcome for a flick.
  - 0.40 to 0.46, hold, the caret blinking on the clock (a class the timeline
    toggles, a CSS animation), or a slow reader's next notch lands on a frozen
    frame. 0.46 to 0.56, it erases; the caret goes at 0.565.
  - 0.57 to 0.70, the hinge, the glow peaking at 0.64. **The ellipses start
    at 0.7x the logo box, not at zero, with a linear ease.** Their
    intersection does not touch the glyphs until about 0.75x, so from zero the
    reveal measured as 88px of black then a 23px pop; from 0.7x the opening
    spans most of the window. The glyph edge sweep is the splash; the dead
    corner-growth before it was not.
  - 0.72 to 0.78, the white fades to 22% and the screens fade up underneath.
  - 0.80 to 1.00, the fall through the first loop, the solid logo to zero by
    0.87 and its group hidden at 0.875 so nothing invisible is scaled.
  - 0.86, the frame relabels `cloots` and the ground hands over under the
    still-opaque frame in 0.55s (see 4.1).
  - 0.90 to 1.00, the frame dissolves over the brief, which has been scrolling
    up beneath it the whole pin. **`autoAlpha` on the pinned frame itself, not
    `opacity` on `#keyhole`:** with `pinSpacing:false` the released frame stays
    translated over the brief's first viewport, and at opacity 0 it was still
    hit-testable, so "Visit cloots.ca" could not be clicked. Not
    `pointer-events:none` on the frame either: that would hand the pointer to
    the brief under the opaque black mid-pin.
  - The portal's `scrub` is 0.5, not the page's 0.22: on a flick the timeline
    catches up over half a second, so the beats render as motion rather than
    as a jump cut. The first build washed to the ground and released onto a
    viewport of empty cream; measured, it read as dead page.

  **What the flicker taught before it was cut:** the masked screens must be
  hidden until the fade beat or the glyphs show before the logo has arrived;
  the nav's scrim follows `--bg-rgb`, so any ground hand-over while the frame
  is still opaque black puts a cream bar over black unless the nav is hidden
  or held night; and a zero-duration `set()` on a scrubbed timeline is fully
  reversible, which is what made the strike work and is what the caret uses.

  The white logo is a second `<image>` of the same PNG drawn solid above the
  masked screens, inside the two hinge clips, in its own `<g>` so the fall
  scales it with the mask. It rests at 22% with the clips open in the static
  states; `.portal-line` is `visibility:hidden` unless `.js-anim`, so those
  states are logo only. `.keyhole-frame` carries `z-index:3` so
  the pinned frame paints above the brief scrolling under it; `.scene` is
  `position:relative`, so without it DOM order would put the brief on top.
- **The loop** (`#loop`, 2026-08-30): the other five Cloots screens laid flat
  on a figure-eight beside the upright Ask Cloots phone. The reference is the
  Sobha Privy Collection "Handpicked" ring (read in
  `_source/reference/sobha-handpicked-carousel.md`) crossed with an agency
  hero of flat isometric cards he sent, and the figure is an infinity because
  the wordmark's "oo" is one and the Ask Cloots button is one. Built in CSS
  3D and the GSAP already on the page, not three.js: what forced that site
  into WebGL was bending photo tiles onto a tight ring, and a phone screen
  must stay flat (a bent iPhone reads as a rendering error), so flat cards on
  a 3D path is exactly what `perspective` and `translate3d` are for, the
  cards stay real `<img>` elements with alt text, and the three degrade
  states cost nothing. How it is built, every number tunable by eye:
  - **The stage is the camera**: `perspective:1600px` at `50% 42%`,
    `container-type:inline-size` so the cards size in `cqw`, `overflow:clip`
    (on the stage, never on the plane: overflow on a `preserve-3d` element
    flattens it). The plane is `preserve-3d`, posed `rotateX(54 - 6p)
    rotateZ(24 - 5p)` where `p` is the block's progress through the viewport,
    so it flattens and squares a little as it scrolls through: the Sobha
    camera flight in two numbers. Positive rotateZ puts the far lobe upper
    left and the near lobe lower right, his "going from up to down right".
  - **The track** is a Gerono lemniscate, `x = A sin t, y = (A/2.09) sin 2t`,
    A = 0.40 of the plane width, 2.09:1 measured off `cloots-infinity-ink.png`.
    `z = 26 cos t` lifts the right lobe into a bridge over the left, so at
    the crossing one card passes over another rather than through it, and
    the browser's 3D sorting does the rest. It is **drawn**, a 1px hairline at
    22% ink 30px under the plane (below the lowest card, or it draws across
    the sunk arm's screens), written by `measure()` from the same equation
    the cards ride: a line that is the loop, the argument 4.6 makes for the
    timeline spine.
  - **Fifteen cards**, three sets of five, 11cqw wide (12.5 under 900px, 15
    under 560), spaced evenly in `t`. The repeats are `aria-hidden` with
    empty alt and the recording's repeats are its poster, so there is one
    video and it keeps `.app-video`'s play-on-view and reduced-motion pause.
    Cards are axis-aligned, not turned to the tangent: turned, half of them
    would ride upside down.
  - **Scroll drives it, nothing else.** `TRAVEL` 0.5: a card covers half the
    track while the block crosses the viewport, the Sobha ring's half turn,
    scrubbed at `SCRUB`, and it stops when the hand stops. **No idle drift**:
    a track that moves on its own is a marquee, and 4.6 says what happened to
    those. The pointer tilts the plane up to 1.5 degrees on both axes,
    smoothed at 0.05 on `gsap.ticker` only while the block is on screen and
    only on a fine pointer. Depth fade 0.72 at the far edge to 1 at the near,
    animated state only.
  - **Every state shows the composed picture.** `loop.layout()` and
    `loop.pose()` live above the reduced-motion return and run at load
    (`p` 0.42, the CSS pose matches it), so reduced motion and a GSAP outage
    show the static isometric figure, opacity 1 throughout; the cards' CSS
    transform parks them off-canvas until that first layout so nothing
    stacks in a corner for a frame. No script at all is a plain five-up row
    with the repeats and the track hidden. Sizes are read in `measure()`
    only, at load, on resize and on ScrollTrigger refresh, never per frame
    (6, trap 18). The figure is a `.device-fig`, so it gets the same rise as
    every phone on the page; the kept phone keeps its parallax.
  - **The first build, and why it changed.** Ten cards at 12.5cqw on a 37
    degree tilt with no drawn track: the screenshot showed two diagonal
    clusters with an empty crossing, which is the "all over the place" he
    fixed on 2026-08-29 wearing a new hat; the cards stood too upright to
    read as laid flat (cos 37 is 0.80 of their height, the agency reference
    is nearer 0.6); and the frame where the block enters clipped the far
    cards at the stage's top. Drawn track, 52 degrees, fifteen smaller
    cards and a longer perspective fixed all three in one pass.
  - **Measured, headed Chromium, 1440 by 900, wheel through the block**:
    frame p50 8.3ms, p95 9.3, p99 9.4, worst 15.8, zero frames over 24ms on
    the second and third passes, identical to the claims block and the Helv
    gallery on the same run. Headless numbers are meaningless here (see 7).
    `verify.py` green in full, zero horizontal overflow at 390.
  - **Not built, each with a reason**: the kept phone standing at the
    crossing with the cards orbiting it (the phone would occlude the
    crossing, which is the interesting part, and the near arm would occlude
    the phone); the flat cards in the chassis (his words were "laid flat
    screens", and the chassis rule is about not faking a phone); a pinned
    section (4.7 allows one pin and the portal has it).
  - **Open for his eye**: the pose (54/24 at rest), the track's weight (a
    22% hairline is a whisper), fifteen against ten, the fade, and the phone
    layout, where the kept phone fills the width and the loop sits under it
    small.
- **The drag gallery is one implementation** bound by `[data-gallery]` and
  `data-gal-*`. Both the Helv screens and the Groundwork strip use it. It
  scrolls natively on every pointer; an earlier build pinned the page for +=320%
  and that was the first thing Arsh complained about.
- **The veil** (formerly the cold pane) is a canvas of warm haze over the close.
  The pointer burns a hole and it drifts back over: texture painted once,
  `destination-out` radial gradients to clear, a 0.011-alpha redraw each frame
  to refill, pointer moves interpolated so a fast flick leaves no gaps, rAF
  gated by IntersectionObserver. Resting opacity **0.38**, full bleed and
  radially masked (`155% 72%`, not the original `130% 118%`, which was still
  fully opaque where it met the top edge and drew a hard horizontal seam).
- **The particle field** is one canvas with two cross-faded modes, snow and
  stars, driven by the phase engine so a phase change never pops a layer.
- **Accent ticks, not dividers.** A 22 to 26px accent mark above a block, which
  draws the full width on hover where the block is interactive. Used by the
  channels, the deliverables, the Cloots claims and the Groundwork cards. This
  is the site's own vocabulary and new components should reach for it.

### The chrome

**The nav and the HUD are glass at the top of the page.** The bar used to paint
`rgba(--bg-rgb,0.94)` unconditionally, so the top 68px of every phase was a flat
opaque band and the hero seam appeared to begin below the menu. It is fully
transparent with no blur at scroll 0 and the phase gradient runs through it; the
scrim and a 14px blur fade in on `.is-scrolled`, where they are doing legibility
work over sliding content rather than covering the design. The hairline flipped
with it: hidden at the top, shown once there is a scrim for it to sit on.

**The links take full `--ink` while the bar is bare**
(`.nav:not(.is-scrolled) .nav-links a`), since there is no scrim under them.
Measured on the live page, the ground behind them at the top right is `#CAEDFE`
and ink reads 15.1:1 on it.

Both invert on the `any1` phase via `.is-night`, which the phase engine toggles
from the same table that paints the ground.

### The contact block

Four hairline rows with a label left and a value right is a form, not an
invitation, and Arsh named it: "the signature of a shitty ass claude code
design". What replaced it:

- **A live clock instead of a rule and the word STATUS.** `America/Moncton`,
  `en-US` (because `en-CA` renders "a.m." and the label voice wants "AM"),
  refreshed every 20s, wrapped in try/catch so a runtime without timezone data
  prints nothing rather than a wrong hour. It runs outside the GSAP branch
  because it is information, not motion. A ticking local time says "somebody is
  there, and it is this hour where they are" in a way a status pill cannot.
- **Each channel says what it is FOR**: the fastest way, the receipts, the
  formal one, the thing I am building now. A label and a URL is a form; naming
  the job makes it a recommendation, which is what makes reaching out feel
  invited rather than listed. Handles are shown, not URLs, because URLs are for
  machines.
- **No dividers.** The accent tick above each channel draws its full column on
  hover, so the only line on the block is an interaction.

### The chapter hook

A chapter opens on a claim, not a label. `.chapter-hook` is Inter Bold 800 at
`clamp(32px,5.2vw,76px)`, two masked lines that rise on entry, sized
deliberately under the hero name so it reads as the second voice rather than a
second hero. A label describes the chapter; a hook makes a claim the chapter
then has to keep. See 5.1 for the line and why it works.

### The close

Editor's Note **Semibold 600** at `clamp(44px,8.4vw,124px)`, centred, full
bleed. Semibold and not the Light the rest of the editorial voice uses, because
this is the last thing on the page and the only line asked to carry weight. Bold
700 was rendered and compared: it loses the high-contrast serif's character.

## 4.6 What was removed, and why

Recording these so they do not come back:

- **Both scrolling marquees.** The mechanism was the problem, not the face;
  setting the same ticker in Lumiare would not have saved it.
- **The principles section.** All four principles were already argued with
  evidence inside the Cloots decision grid, so the section restated claims it
  had already earned.
- **The horizontal card rack as the home for every non-Cloots project.** That is
  what made the site a Cloots site.
- **Every full-width hairline rule** under headings and between list rows: the
  project headers, the spec lists, the stats, the Cloots claims, the engine
  flow, the Helv grade. Space separates. Kept on purpose: link underlines (they
  mean "this is a link"), the gallery progress rail (it is a control), the
  timeline spine (it *is* the timeline), the nav hairline (it only appears once
  content is sliding under it).
- ~~**The card boxes** on the Groundwork strip.~~ **Back, on his instruction,
  2026-08-29:** *"sqldb angular and that horizontal slider should be inside
  those lined boxes that we had before, i liked them."* This entry stays visible
  rather than being deleted, because the removal and the restoration are both
  real decisions and the next session needs to know the argument ran both ways.
  What is on the page now is a **hairline frame, not a card**: `1px solid
  var(--line)`, the keyhole's own `clamp(18px,2.2vw,30px)` corner, and **no
  fill**. No fill for two reasons: 2.3's "who is using a rectangular box in
  fucking 2026" is about a filled rectangle with hard corners, and the dap
  ground is already tinted, so a filled card there would be the nested-boxes
  mistake that killed the footer panel. The accent tick survives inside the
  frame; it is the site's vocabulary and it no longer has to stand in for one.
- **The tinted footer panel**, which sat on a tinted page with the veil inset
  inside it: nested boxes.
- **The tinted `.engine` panel** in the Cloots chapter (32px radius, `--panel`
  fill, its own heading and its own phone). It made the chapter three screens
  and the algorithm a scene of its own. The copy and the four-step flow
  survive as a beat inside the product phase, on the page ground. See 3.1.
- **`FIG. NN ·` caption numbering** throughout.

## 4.7 Motion

- **Animation-heavy is the brief**, awwwards reference level, scroll-driven.
  *"my design is actually animation heavy, in fact cloots is basically the same,
  it has animations every part of the app."*
- **Smooth scroll is ON, and this reverses the previous rule.** Arsh asked for
  it directly against the Sobha Privy Collection site (an awwwards winner):
  *"they have a smoothness that is not there in our current website"* and then
  *"and yes i want real smoothening."* What that site actually runs, read out of
  its bundle: Locomotive Scroll v4 at `smooth:true, lerp 0.1`, a custom
  "gravity well" layer that drives the lerp toward zero near six anchors so the
  page decelerates into them, and Motion One spring physics on the reveals.
- **What is on this page instead: Lenis 1.3.26, vendored at `assets/lenis.min.js`.**
  Not Locomotive, which transform-translates the document and would break every
  `position:fixed` layer here (nav, HUD, both washes, the canvases) plus the one
  pin, find-in-page and anchor jumps, and whose v4 is abandoned. Lenis drives
  the real window scroll, so **no `scrollerProxy` is needed and adding one would
  break the pin.** Vendored rather than CDN because it decides how the page
  feels and a third-party outage must not be able to change that.
- **`lerp` is 0.18 and the number is derived, not taste.** Lenis damps with
  `1 - exp(-lerp*60*dt)`, so the fraction of a flick outstanding after t seconds
  is `exp(-lerp*60*t)`. The section 7 wheel gate reads the position 230ms after
  a 700px flick and demands 600px: lerp 0.10 leaves 25.2% and travels 524px and
  **fails**, 0.15 travels 612px and is marginal, 0.18 travels 641px and passes.
  Measured in the real harness: 633 to 726px across twelve flicks. 0.18 is a
  93ms time constant, long enough to fuse the operating system's stepped
  delivery into one continuous curve, which is where nearly all of the
  perceived smoothness lives, and short enough that the page is never visibly
  behind the hand.
- **The settings that are load-bearing**, each one a bug if changed:
  `allowNestedScroll:true` (the drag galleries are horizontal scrollers; Lenis
  tests per axis, so vertical wheel scrolls the page and horizontal moves the
  strip. Without it Lenis eats the whole gesture and both strips read as dead);
  `anchors:true` with **no offset** (Lenis already honours
  `[id]{scroll-margin-top:72px}`; passing `offset:-72` double-counted and every
  menu jump landed 144px low, measured); `autoRaf:false` with GSAP's ticker
  driving `lenis.raf` (one clock: two rAF loops read the scroll a frame apart
  and the parallax swims); `ScrollTrigger.addEventListener('refresh', ...)`
  calling `lenis.resize()` (a refresh re-measures the pin spacer and can change
  document height, and Lenis clamps against a cached limit).
- **Lenis is not constructed on a touch-primary device.** `syncTouch` is false,
  so it would have nothing to do there but run a rAF, and iOS momentum plus
  rubber-band plus a collapsing URL bar do not need a fourth opinion. The gate
  is the `FINE` flag the file already computes. A laptop with a touchscreen
  gets smoothing on the trackpad and native scroll under the finger.
- **Scrub compounds with the smoothing, so it came down.** `SCRUB` and
  `SCRUB_SLOW` are variables, not literals: 0.22 and 0.45 when Lenis is running,
  the original 0.6 and 1 when it is not (mobile, and the no-Lenis fallback).
  Scrub was tuned when it was the only smoothing on the page. Left at 0.6 on top
  of Lenis's 0.28s settle, the parallax trails the page by most of a second and
  reads as drift, which is the "laggy and unresponsive" failure mode wearing a
  different hat. With Lenis the scroll is already continuous, so scrub only has
  to absorb the residue and everything rides one eased value, which is the
  property that makes a page feel like one object.
- **The portal autoscrolls, and that is his decision against this rule.**
  2026-08-29: *"it doesn't matter what speed is user scrolling with, we need
  to control the flow of the scroll or animation so that no matter what speed
  the user is coming in with the scroll, it works in the exact same pace every
  single time."* So on a precise-pointer device, entering the pin from above
  snaps to its start and carries the page to its end at one constant pace
  (`AUTO_MS`, 8s) whatever the hand did: wheel-down and the scroll keys are
  swallowed while it runs (a capture-phase listener ahead of Lenis), and
  **scrolling up at any moment aborts it** and hands the page back. That
  escape is the whole difference from the pin he hated, which took input and
  gave nothing. The timeline stays scrubbed to the scroll; only the driver
  changed, so every state is still reachable by hand after an abort, in both
  directions, and touch devices keep the plain scrub (there is no Lenis to
  hold a finger, and holding a finger is worse). It is driven as **one
  Lenis animation**: `lenis.scrollTo(end, {duration: AUTO_MS/1000, easing:
  linear, lock: true, force: true})`, after an immediate snap to the start,
  and an abort is `lenis.stop(); lenis.start()` (a `scrollTo(current,
  {immediate})` returns early when the target equals `targetScroll`, which
  a running animation keeps it equal to, so it never cut the animation).
  **An abort is a deliberate up, not any negative delta.** A macOS trackpad
  emits sub-pixel opposite-sign deltas at finger lift-off and on a re-grip,
  and the first build aborted on any of them, after which the typewriter
  was the finger's: the review flagged it, and it is the likeliest reason
  "slow and jittery" survived a clean clock on his machine. Negatives now
  accumulate (reset by any positive of 1px or more, or after 250ms of
  silence) and the abort fires at -10px accumulated or a single -6px, which
  still releases on the first real upward motion. Aborts are logged to
  `window.__portalAbortLog` with `dx`, `dy`, the accumulator and the time
  since the clock started, so one reproduction tells lift-off from re-grip.
  **And the clock re-arms**: after an abort, the next wheel-down or scroll
  key inside the pin restarts it from wherever the page is, at the same
  pace, no snap (`autoDrive`, a persistent capture listener). That is a
  product decision made for him from his own rule: inside the pin, down
  always means the clock and only up hands the page back.
  The first build drove it with a `scrollTo({immediate:true})` on every
  `gsap.ticker` tick instead, and that is the jitter Arsh saw (6, trap 18):
  each immediate call made Lenis reset and rewrite `<html>`'s class list,
  5,759 times in one 8s traversal.
  `window.__portalAutoOff = true` turns it off for a harness that parks the
  pin by hand.

  **`onEnter` is not "the reader scrolled down into the pin".** Found the
  same afternoon by the gate, then confirmed three ways: it also fires when
  ScrollTrigger's first refresh finds the page already past the trigger (a
  reload with the scroll restored below the portal, a `#ship` load) and when
  an anchor animation flies through it (Contact in the nav, Lenis's 0.9s
  anchor scroll). What it looked like: the page snapped to the pin start
  (5591 at 1440x900) and sat there, Contact never arrived, a reload
  mid-page landed in the portal. `autoStart` therefore takes an entry only
  when `direction === 1`, the scroll is still inside the pin
  (`st.scroll() < st.end - 1`), and it is not within 1.5s of setup or of a
  click on any `a[href^="#"]` (a capture-phase listener stamps
  `autoSkipUntil`). It also starts from `start + 1`, not `start`: a snap to
  the exact float start can read as before the pin and fire `onLeaveBack`,
  which stops the run it just began. The gate checks all three jumps
  (`portalJumps`).
- **No scroll-jacking elsewhere, and this is a different thing from smoothing.**
  What burned him was **pinning**: an early build held the page for multiple
  viewports and he hit it immediately, *"the scroll is so difficult... laggy and
  unresponsive."* That is a displacement failure, input in and nothing moves.
  Smoothing is a latency question: displacement stays 1:1 and only the arrival
  is eased. **THE TEST STANDS: 12 simulated wheel flicks of 700px must each move
  the page at least 600px**, and it is what pins the lerp. Exactly one pin
  exists (the portal), and it is now 1.6 viewports on desktop, 1.3 on
  mobile, up from 0.7. That is not the thing he rejected: that was two screens
  of input with nothing moving. Here something visibly changes at every
  progress value except two short holds (the black beat before the line
  types, and the hold after it, where the caret blinks on the clock). Do
  not add a "gravity well" or a snap point; that is the
  part of the reference site closest to what he already rejected, and this page
  has reading copy where that site has full-bleed media.

### Two registered eases, and why there are two

`gsap.registerEase` is in core, so a damped harmonic oscillator costs one
`Math.exp` and no plugin file. CustomEase is free but is a separate fetch this
page will not make.

- **`settle`** is critically damped and monotone. Safe anywhere, and the only
  one allowed inside a scrubbed timeline, where the hand drives time in both
  directions and an overshoot is not a bounce but a wobble the reader can scrub
  back and forth. This is why the keyhole's `back.out(1.4)` became `settle`:
  monotone, and it is what that block's own note always described, "arrives 12%
  large and settles to rest".
- **`spring`** is lightly underdamped, peak 1.0285 at t 0.558, so a 2.9% nudge
  rather than a bounce. Entrance reveals only, never on a scrub.
- **Both are normalised so f(1) is exactly 1.** GSAP does not renormalise an
  ease, and the raw closed forms land at 0.9949 and 0.9998, which would park
  every reveal a fraction short of its mark for ever.
- **Opacity must not ride the spring.** On a long settle a combined
  opacity-plus-transform tween leaves the subject half lit through most of its
  travel, which reads as a slow fade instead of an arrival. Transform takes the
  long curve, opacity takes about half the time on `power1.out`, both at
  position 0. The device figures are the worked example.
- Travel came down as duration went up. A long throw reads cheap; the duration
  is what carries the weight.

### The bug this uncovered: three reveals were inert

`.hk` (chapter hook), `.cl` (close line) and `.ship-line` are plain spans, so
they computed to `display:inline`, **and a transform on an inline box is
discarded.** GSAP reported `yPercent: 118` while the browser computed an
identity matrix. Measured before the fix: the translateY of all three never left
0 through the entire reveal. Three of the four largest typographic moments on
the page simply appeared. The hero escaped it only because its inner element is
an `<svg>`, which is replaced and does accept a transform.

Fixed with `.hk,.cl,.ship-line{display:block}`. **Block, not inline-block:**
build trap 4 is about per-character spans becoming break opportunities, and
these are whole lines already inside a block-level `.line-mask`, so there is no
wrapping exposure. Verified: identical layout at 1440, 768 and 390, identical
document height, centering preserved on the two centred blocks, and the close
line now travels 148px and overshoots to -4.2 before settling, which is the
2.9% the spring is designed for.

### The depth pass

Smoothness is largely a depth cue. A page where everything travels at one rate
reads as a flat card sliding under glass however high the frame rate is, and the
reference site runs eleven rates against this page's four. New rates live in one
block labelled THE DEPTH PASS rather than filed per section, because depth is a
system and the only way to judge it is to read the rates against each other.

Two rules held throughout, and they are the important part:

1. **Nothing that is being read moves.** The chapter hooks, the timeline keys
   and details, the engine flow rows and the Cloots claim paragraphs are all
   deliberately at rate zero. A paragraph that drifts while the eye is in it is
   worse than no parallax at all. `.claims` is a two column grid of four
   paragraphs, which is the exact shape that invites a column-offset drift; do
   not.
2. **Amplitudes stay small and neighbours disagree.** Matched rates cancel: the
   sixteen phone figures all ran an identical 18px and travelled as one rigid
   slab. They now run an irregular table (15/27/20/31/17/24), irregular rather
   than a ramp because an even gradient across a row reads as a tilt.

Subjects: the two hero name lines (widened from [-6,-10], which is 7.5px against
12.6px over a whole viewport and below the threshold where two rates read as two
planes at all, to [-10,-20]); the ground itself at 3% using the 8% of bleed
`.stage-wash` already carried; the three project wordmarks, asymmetric 20 to
-10 so the name is still rising as it settles into reading position; the A+ at
16% in `yPercent` so the amplitude tracks the clamp with no media query; the
stamp on `y` only, because rotate and scale belong to its entry tween and a
second writer fights it.

**The stats row is the one subject with an alignment contract** and it is the
one to watch. Four figures in a row are a grid, and a reader who notices the
offset reads a broken baseline rather than depth. It started at 9/17/25/33,
a 24px spread at the ends of the travel, which is visible as misalignment. It is
now 5/9/13/17. If Arsh reads it as a mistake, take it to zero; nothing else in
the pass depends on it.

### Canvas work that the smoothing forced

Native scroll runs on the compositor and rides through a main-thread stall.
Lenis integrates the scroll position in JS, so **every main-thread cost became a
felt cost** and two had to be paid for.

- **The veil re-stroked its whole texture on every re-entry.** The
  IntersectionObserver called `size()`, which always called `paintTexture()`,
  which strokes about 2000 needles plus two full-canvas gradients,
  synchronously. Measured at 268ms, and it showed up in the profile as a stall
  at exactly scrollY 15068, which is where the close is. The texture only
  depends on the size, so re-entry at an unchanged size is now one blit.
- **Melting moved off the pointer event and onto the frame.** A trackpad
  delivers pointermove faster than frames, so one sweep issued up to 25
  destination-out fills between two paints. The handler now records a target and
  the melt happens once per frame, reusing the interpolation that already
  existed for fast flicks. `getBoundingClientRect` came out of the handler for
  the same reason: a forced layout read interleaved with Lenis's scroll writes.
- The veil dropped to `DPR 1.5` (it is a soft warm gradient at 0.38 opacity
  behind a feathered mask, and fill rate is DPR squared), its refill gated to
  6.5s after the last melt instead of running for ever, and its refill alpha
  made time-based so a 120Hz display does not refreeze it in half the time.
  Grain count is now per CSS pixel, `(W*H)/(DPR*DPR)/650`, which is
  arithmetically identical to the old expression at DPR 2 so the appearance Arsh
  approved is preserved exactly, while 1.5 and 1 stop thinning out.
- **The particle field keeps DPR 2** (dots 0.7 to 2.4 CSS px across would
  visibly soften) but no longer clears a full viewport canvas on the four phases
  that carry `fx:'none'`. The rAF stays alive so a phase change has no restart
  seam.
- The engine flow wrote four `classList.toggle` calls per scroll frame; the lit
  count takes five values, so it is cached and the common frame is one compare.

**Measured result**, 1440 by 900, GPU, full-page scroll: frame p50 8.3ms both
before and after, but p95 15.7 to 10.9, p99 18.2 to 12.2, worst frame 268ms to
20ms, and frames over 24ms from 6 to **zero**. The page was never slow on
average; it hitched, and hitches are what read as unsmooth.

- **The hero types itself.** Editor's Note Light, 52ms a glyph, with a **0.6s
  beat after "I design in code,"** (the comma is typed before the pause falls).
  It was 1.0s until 2026-08-29; his words: "reduce the time spent at I design
  in code, the delay for the next line reduce it a bit". `HOLD` in the hero
  block is the one number.
  The beat is declared in the markup as `<i class="tw-hold">`, sitting between
  the words it follows, so editing the copy cannot move it to the wrong glyph.
  Each segment restarts its leading edge at its own first character; carrying
  the previous segment's head across the beat would light the first glyph after
  it the instant typing resumed. Every glyph is laid out
  in its final position from the first frame and only opacity animates; alpha
  comes from how far the cursor has passed it over a 2.4-character soft edge, so
  the whole effect is two tweens. The caret glides along a line and **snaps
  across a line break**, because easing across a wrap sends it sailing back over
  the measure and reads as a bug.
- **Reduced motion and no-GSAP are both fully readable states** and every round
  must re-verify them. The typewriter split, the phase tween and the veil all
  live inside the animated branch so nothing can leak. **Lenis is inside that
  same branch**, after both early returns, so reduced motion and a GSAP outage
  both fall back to native scroll with no dead wheel. There is a third state
  now: Lenis missing while GSAP loads, which falls through to the original
  anchor handler and native scroll. All three are in the harness.

---

# 5. COPY AND VOICE

## 5.1 The fixed lines

- Cut from the Cloots brief, 2026-08-29: "Onboarding runs through Google and
  Apple sign-in. No forms before value, no tour to sit through. The first
  session teaches by doing." His words: *"what kind of value are you providing
  with this line btw? ... literally every app uses google and apple sign in,
  dawg is that the thing to point out?"* The only idea in it worth keeping is
  the third decision card ("The first session had one job"), which already
  carries it. The test for any line in a brief: does it say something only
  this product can say. Sign-in providers never pass it.
- Hero: **"I design in code, because *beauty* belongs in function."** (`beauty`
  italic in the phase accent.) This replaced "I design in code. I ship.", which
  was his earlier identity statement and is still true if it is ever wanted.
- Designation, exact and unchanged: **"Product Designer & Software Engineer"**,
  set in **Inter Bold** at `clamp(18px,1.6vw,24px)` in full `--ink`. Bold at a
  muted tone reads muddy, and this is the designation rather than a caption, so
  it takes the full ink and negative tracking, which is what Inter wants as the
  weight comes up.
- Journey hook: **"Four winters ago, none of this existed."** A hook makes a
  claim the chapter then keeps; a label just names the section. The timeline
  underneath is the proof, because every project on the page postdates the
  photograph beside it.
- Cloots ship board: see 3.1.
- Status: **"Open to anything worth building."** followed by his own framing:
  roles, projects, things that do not exist yet; if it genuinely intrigues him
  he will build it; *"Right now, at the age I am, that is what I love doing. It
  might change. It has not yet."* That last beat is his and it is the most human
  line on the page.
- Close: **"The best one isn't built yet. / Come build it with me."** Kicked off
  by "Nobody asked for any of this", which carries the founder beat that used to
  be its own chapter.

## 5.2 The troll voice

*"maybe we can add a bit more personality to the portfolio website because i am
a bit of a troll."* This is a real design direction.

- **Dry and specific, never zany.** No emoji, no exclamation marks, no jokes
  about being an AI, no "fun fact" labels. The humour comes from stating an
  embarrassing true thing flatly next to the evidence.
- **Annotation is its home**: small caption voice pinned to the artefact it is
  about, so the joke sits beside the proof rather than in a headline.
- Shipped examples: "Instagram Direct, beat for beat, drawn by hand from
  memory." / "Double tap the avatar to switch accounts. Yes, I copied that one
  too." / "I was certain this was going to make me a millionaire." / "A school
  project that forgot it was one."
- **It may never touch** the Cloots case study, the Saint John Java claim, the
  DAP client work, or the contact block. Those stay straight.
- It has to stay compatible with the register in 1.3. Personality raises the
  senior read when it is confident and lowers it when it is needy.

## 5.3 Captions

Say what a thing **proves**, not what it is. "Pending, scheduled, cancellable.
The state machine, visible" earns its place because it cashes in the body copy
above it. `FIG. NN ·` numbering is gone. Middle dots separate.

**And the proof has to be legible from the picture alone.** The Cloots feed
carried "THE CLOTHES ARE THE ONLY COLOR" as its caption, which is the design
argument from 3.1 verbatim, and the card that actually explains it sat thirty
lines further down. Arsh: "what does this even mean ... its not very obvious to
read is it." A caption that states a conclusion the reader cannot yet see is a
riddle. It is now "BLACK AND WHITE INTERFACE. THE CLOTHES GET THE COLOR.",
where the first half is what the screenshot shows and the second half is what
that proves. The same pass (2026-08-29) took the last six `FIG. NN ·` numbers
off the page; they had survived in the Cloots chapter after 4.6 said they were
gone.

## 5.4 The audience mapping

The site's argument was built to mirror what trophi.ai's posting cares about
without parroting it: activation, onboarding, first-session clarity, engagement
loops, designing user-friendly AI/ML features, comfort with ambiguity, high
ownership, scrappiness. Those now live inside the Cloots decision grid rather
than in an abstract principles list. Their "you will NOT enjoy this role if"
list reads like a description of a solo founder, which is the overlap to keep
visible.

---

# 6. BUILD TRAPS

Each of these cost a debugging round. They are not obvious and they fail
quietly.

1. **A `.night`-style scope must restate every derived token, not just the
   source tuples.** A custom property's `var()` is substituted where it is
   *declared*, so `--bg` declared on `:root` had already computed to the light
   value and inherited that way down.
2. **GSAP's pin copies the pinned element's margins onto its spacer and zeroes
   them on the element.** An inset expressed as `margin` on the pinned node is
   silently thrown away. Put it on a wrapper the pin owns. The keyhole measured
   1440px wide at `left:48` and ran off the right edge while looking correct on
   the left.
3. **Overlapping ScrollTriggers race.** Whichever fires last wins. See 4.1.
4. **`display:inline-block` on split characters makes every character a break
   opportunity**, so the line wraps mid-word. Plain `display:inline` leaves
   Unicode line breaking alone and still measures.
5. **Concatenated glyph paths cancel** under fill-rule nonzero. See 4.4.
6. **An inline SVG with a viewBox and no width defaults to 100%** of its
   container.
7. **A scroll-trigger `start` can begin before scroll 0** in a short viewport,
   which had the hero name rendering grey on first paint and in the og capture.
   `clamp(top 148px)` fixes it.
8. **A radial mask can still be fully opaque where it meets an edge**, drawing a
   hard seam. The veil's mask went from `130% 118%` to `155% 72%` for this.
9. **A `max-width` on a container is inherited by its heading.**
   `.footer-status` at `22ch` broke a 62px heading one word per line.
10. **`en-CA` renders "a.m.", `en-US` renders "AM".**
12. **A pinned full-viewport frame with `pinSpacing:true` releases onto its own
    height of empty ground.** The portal washed to the page colour and then
    the reader scrolled a whole viewport of that colour before the next scene
    arrived. `pinSpacing:false` lets the next scene scroll up beneath the pinned
    frame, and the frame dissolves over it. Needs a `z-index` on the frame or
    the later, `position:relative` sibling paints on top.
14. **`html{scroll-behavior:smooth}` breaks every `ScrollTrigger.refresh()`
    made at scrollY > 0.** ScrollTrigger measures a start by scrolling to the
    trigger and reading back, and it samples `scroll-behavior` once, at its
    first scroll function; with smooth live, the scroll never lands before the
    read, and every trigger's start comes out as docTop minus scrollY. A window
    resize at scrollY 800 was enough: the portal pinned a screen early and
    every reveal on the page misfired for the rest of the visit. This was on
    the page before the portal and nothing noticed, because nobody resized.
    `docEl.style.scrollBehavior = 'auto'` is set inline the moment GSAP is
    known present, before the first `ScrollTrigger.create`. Anchors do not
    care: Lenis drives them, and the no-Lenis path passes `behavior:'smooth'`
    explicitly.
15. **Two GSAP tweens on two fresh proxy objects never overwrite each other.**
    `go()` tweened `{t:0}` afresh every call, so `overwrite:'auto'` was a no-op
    and a fast pass through the portal ran the 1.05s and the 0.55s ground
    tweens together; the long one finished last and painted the whole Cloots
    chapter black, with `cur` already `cloots` so nothing repaired it. Hold the
    handle and kill it before starting the next (the `from` snapshot is the
    live mix, so the join is seamless). The same class of bug: `--ink-rgb`
    carried four components mid-tween because `interpolate()` returns
    `rgba(...,1)` and a regex stripped only the wrapper; every
    `rgba(var(--ink-rgb),a)` on the page was invalid for the length of every
    phase change. `rgbTuple()` now, which was already there.
16. **A pinned element with `pinSpacing:false` stays translated over the next
    scene after release, and at opacity 0 it is still hit-testable.** See 4.5.
17. **`onRefresh` fires AFTER ScrollTrigger has re-evaluated function-valued
    tween targets; `onRefreshInit` fires before.** Geometry that those
    functions read (`khGeom`, `khOrigin`) has to be recomputed in
    `onRefreshInit`, or a resize leaves the hinge and the fall on the old box
    until the refresh after that. **And in `onRefreshInit` the pinned element
    is still pinned**, with the width ScrollTrigger locked on it at pin time,
    so measuring the frame's own `clientWidth` there is one refresh stale in
    both directions (measured: 1140 on an 1100px viewport). `layoutKeyhole`
    measures `documentElement.clientWidth/Height` (viewport minus scrollbar,
    current the moment the window changes), floored at 520 the way the
    frame's CSS is.
13. **Anything that reads as legibility rather than motion must live above the
    reduced-motion return.** It has moved twice: out of the animated branch,
    then off ScrollTrigger entirely, because with the GSAP CDN blocked the nav
    had no scrim and its links were ink on the black frame for 1.4 viewports.
    The scrim is now one rAF-throttled scroll listener with no library. The nav scrim toggle sat inside the animated branch
    and the reduced-motion nav had no scrim at all, which nobody noticed until
    a full-viewport black frame passed under it and the menu vanished. Audit
    the branch for the same class of thing before adding a dark scene.
11. **`scroll-snap-type: mandatory` eats a scroll container's own
    `padding-inline`.** The Groundwork track carries `padding-inline: var(--mx)`
    so its first card lines up with the section heading. Mandatory snap instead
    parked `scrollLeft` at exactly 48px and put the card at x=0 while the
    heading sat at x=48. It was invisible for as long as the cards had no
    outline, and an obviously broken left margin within a second of them getting
    one. The fix is `scroll-padding-inline: var(--mx)` on the **viewport**, not
    more padding on the track: snap aligns against the scroll padding, so the
    card now lands at 48/35/26/20 against a heading at 48/35/26/20. Any future
    outlined element inside a mandatory-snap strip hits this.

---

18. **An attribute write on `<html>` is a full-document style recalc, and
    the next layout read pays for it mid-frame.** 2026-08-29, the portal
    typewriter "slow and jittery" in Brave and clean in Chromium. Traced: the
    long frames were `UpdateLayoutTree` of 750 elements, forced from Lenis's
    `setScroll` and from anything reading `scrollY`, dozens of times a second.
    Two writers were dirtying the root: Lenis's `updateClassName()` (the
    per-tick immediate `scrollTo` in the first autoscroll, 5,759 class writes
    in 8s) and the phase engine's seven `setProperty('--...')` calls on
    `docEl.style` every frame of a phase change (699 in the same 8s). Chromium
    recalculates at ~24us an element and stays under 16ms; Brave at ~63us,
    17 to 47ms a frame, 30 to 110ms frames, glyph intervals 29 to 220ms
    instead of a steady 112. Fixes: the autoscroll is one Lenis animation
    (4.7); the token tween paints at 40Hz; the flip at `FLIP_AT` runs `go()`
    at 0.05s because the marbling is opaque over the stage there anyway.
    The gate counts frames with a root write during a traversal. Rule:
    nothing writes to `<html>` or `<body>` per frame. Tokens that must
    animate go on the smallest subtree that reads them, or at a lower rate.
    And the first traversal after Brave launches is clean, so a single look
    proves nothing: measure the second.

# 7. VERIFICATION

`tools/verify.py` runs the mechanical half. Run it after every round.

1. **Wheel test: 12 flicks of 700px, each must travel >= 600px, six from the
   top and six from just past the portal.** It is what pins the Lenis lerp (see
   4.7 for the arithmetic; it measures 230ms after each flick, so a lerp below
   0.15 fails it on the first flick). It runs on either side of the portal
   because the portal autoscrolls by design and would fail it by construction.
   **The portal's own contract** is the second half of the same check: the
   traversal from pin start to pin end must take `window.__portalAutoMs`
   (4.35s, plus or minus 0.6)
   whether the reader arrives at 60px/30ms, 300px/60ms or 1200px/230ms, and a
   wheel-up during it must abort it (`portalTraversalSeconds`,
   `portalPacePass`, `portalAbortOnWheelUp`). And three ways past the pin
   must **not** start it: the Contact anchor, a reload restored below it, a
   `#ship` load (`portalJumps`, `portalJumpPass`). Every one of those failed
   the first time it was checked. Two more since the review: three
   lift-off artefacts (-0.4, -1, -2) fired into a running clock must leave
   it running (`portalLiftoffPass`), and a real abort followed by a
   wheel-down inside the pin must re-arm and reach the end in the time the
   remaining distance implies (`portalRearm`, `portalRearmPass`). And
   `portalRootWrites`, the number of
   frames in which `<html>` or `<body>` had an attribute written during one
   traversal, must stay under 80 (it was in the thousands before trap 18;
   what remains is the phase engine's 40Hz token paint).
   **A harness parks through Lenis, never `window.scrollTo`.** Lenis ignores
   a native scroll while it is still smoothing the last flick's tail, so a
   `window.scrollTo` fired right after a wheel test silently does not happen:
   the second wheel run "collapsed to 55px a flick" because the jump past the
   portal never landed and the flicks walked into it from above, which is the
   autoscroll working. `verify.py`'s `park(y)` uses `window.__lenis`, the handle the page exposes for it, and
   `lenis.scrollTo(y, {immediate:true, force:true})`.
2. Zero horizontal overflow at 1440, 768 and 390.
3. Zero console errors and zero page errors.
4. Computed fonts resolve: body Futura Web, `.micro` Inter, `.disp` Inter,
   `.mono` Space Mono, the ship board TNR MT Std. A silent system-font fallback
   is a known failure mode.
5. **prefers-reduced-motion**: all content visible, veil at opacity 0, videos
   paused, zero dimmed nodes.
6. **GSAP CDN blocked**: page fully readable, zero dimmed nodes, nav name
   visible, no errors. Lenis is constructed after that early return, so this
   state is native scroll and there is no dead wheel.
6b. **`assets/lenis.min.js` blocked**: the third state. Page scrolls natively,
   the original anchor handler binds, no errors, nothing dimmed. And
   **touch-primary emulation** (iPhone, tablet): `window.__lenis` must be
   false and the page must still scroll and reach the bottom.
6c. **`node --check` on the inline script before anything else.** A stray `*/`
   inside a long comment took the whole motion system down for one round and
   only the browser harness caught it. The parse check is two seconds.
7. Phase guard: every `data-phase` used is defined in `PHASES`.
8. No dead anchors, no broken media, every image <= 350KB.
9. **grep: zero em dashes**, zero `#05157D`, zero `#FFFCFB`, zero marquee, the
   ship board line intact.
10. Screenshot 1440 and 390, mid-scroll states, **and read them.** Note when
   screenshotting a scrubbed subject: `scrollIntoView({block:'center'})` lands a
   `top bottom` to `bottom top` trigger at roughly progress 0.5, which is
   exactly where a symmetric `fromTo(y:a -> y:-a)` parallax is at zero. The
   stats row looked perfectly aligned in the first capture for that reason.
   Capture the ends of the travel, not the middle.
11. **Frame profile, not just frame rate.** Record rAF intervals across a full
   page scroll and read p95, p99 and the worst frame, not the mean. The page
   was at p50 8.3ms while carrying a 268ms stall; the mean hid it completely.
   Target: zero frames over 24ms. **Profile headed.** Headless Chromium
   composites in software here: on 2026-08-30 it reported p50 16.7ms and 54
   to 65 frames over 24ms on regions nothing had touched, and the loop looked
   heavier than its baselines only in that environment. The same script with
   `headless=False` (window parked off screen) gave p50 8.3 and zero over 24
   everywhere. The first pass after launch is still the warm-up (6, trap 18):
   read the second.

Tooling: Playwright chromium via
`/Users/arshsethi/Desktop/AndroidStudioProjects/JobClanker/.venv/bin/python`.
Review renders accumulate in `_source/review/` (gitignored).

---

# 8. OPEN

1. **TNR MT Bold Italic against Editor's Note.** Two serifs, arguably one job.
   TNR holds the timeline keys and the ship board. This is the last real
   redundancy in the type stack and it is one edit either way. TNR matters to
   him personally, which is a real reason.
2. **Lumiare's `ANY1` reads close to `ANYI`.** See 4.3.
3. **Bemore Serif** is in the repo, gitignored, unused. He wants it replaced.
4. **Editor's Note and Futura ship as font files**, which the settled licence
   position did not cover. See 4.4.
5. **The og-image** regenerates from the live hero; re-run it after visual
   changes.
6. **Deploy** has not happened. The repo exists since 2026-08-30 (private,
   see 2.7); the deploy is the flip to public plus the checks listed there.
7. Pending his assets: a possible bitmoji or line portrait for the reserved
   `.hero-avatar` slot (his call alone, and the advice he accepted was to route
   it small near the footer rather than the hero), and a possible current photo.
8. **About 3.5MB of unreferenced Cloots assets** sit in `assets/`. They cost
   nothing at runtime. Do not delete without asking. The 2.3MB marbling
   original he dropped into `assets/` lives in `_source/marbling/` now
   (gitignored, over the 350KB cap); only the baked `portal-bg.jpg` ships.
9. **The stats row parallax is the one to review by eye.** See 4.7. It is the
   only new rate on a subject with an alignment contract, and taking it to zero
   costs nothing else.
9a. **The 1M+ odometer ignites to `#70d3ff` on the Cloots ground at
   1.5:1.** Found by the legibility tester on 2026-08-29. 4.2 records that
   this hex cannot carry type on a light ground, and the ignite paints the
   base row exactly that colour; the `.ig-glow` duplicate is what carries the
   light. It was on the page before the portal and it is a design decision
   (the frost accent moment), so it is flagged rather than changed: ignite the
   base row to `--accent` (#0E7A52, about 5.5:1 there) and let the glow carry
   the frost, or leave it. His call.
9b. **The portal's typed line is settled: "This might just be / the one."**
   His words, 2026-08-29, full stop included (I once tried to drop it; "i
   am good with fullstop leave it"). The beats went through two rounds the
   same day: first a jab, "THIS MIGHT JUST BE" typed, a held beat on the
   break, then "THE ONE." on its own line; then, after he watched it, *"it is
   still animating every little character very slowly, the typewriter, i
   don't want that, i want it to be smooth and just make it have a pause
   after delivering the whole line and then we want the transition to cloots
   quickly as possible."*, and then the jab came back: *"why are we
   not pausing at "be" we need to pause and flicker the typewriter there
   once"*, *"increase the duration of typewriter to 1 second"*, and *"make
   the pause at be exact same as the one we have in our starting page
   line."* So now: 22 glyphs in 1.0s, the hero's 0.6s beat at "BE" with the
   caret blinking twice, a 0.6s hold on the whole line, a 0.25s fade, and
   Cloots on a 4.35s clock (4.5). `beatAt`, the glyph count at the
   `<i class="tw-br">` marker, is where the typing splits. Before it, briefly, "Wrong app. Right instinct."
   (his pick from the second list) and "This one might work."; the record of
   the earlier round follows. On a phone the line is sized in `vw` (7.8vw
   under 700px) rather than the 34px floor: at 390px the floor broke "THIS
   MIGHT JUST BE" before "BE", three lines with the jab's first half
   orphaned, and a width in vw scales with the text so the first line stays
   whole at every phone width.
   **Earlier:** "Wrong app. Right instinct."**
   His pick, 2026-08-29, second round. The first pick, "I ran out of apps to
   copy.", he withdrew himself: *"cloots is actually a copied app tbh, just
   made better and design is not copied but the idea/concept is."* Record
   that: **Cloots's concept is not original and the page must never imply it
   is.** The line now answers ANY1's closing sentence, added the same day in
   his words: "I was certain it was going to make me a millionaire." The
   conviction was wrong, the judgement under it was not, and the wordmark
   is the proof. Rejected on the way: "Meet your next favourite brand."
   (Cloots copy, not his journey), "Four winters later.", a list of
   place/date and question lines ("stop giving me shitty lines"), and the
   copy line above. The lesson for the next line anyone writes for him: a
   claim with attitude that a fact underwrites, not a caption, a question or
   a date. One string in the markup (`#portalLine`); keep it under about 30
   characters or the type beat needs more of the pin. A two-sentence line
   breaks where `<i class="tw-br"></i>` sits in the markup, which the
   splitter turns into a real `<br>`; without it the first render broke
   "WRONG APP. RIGHT / INSTINCT." wherever the measure allowed. Whether the HUD chapter counter should also hide during the
   black is his call; he named only the top bar.
10. **Deliberately not done in the smoothing round**, each with a reason:
   - **Gravity wells and snap points.** The reference site has six and one. It
     is the part of that site closest to what Arsh already rejected, and this
     page has reading copy where that one has full-bleed media.
   - **Moving the two canvas loops onto `gsap.ticker`.** It would give one clock
     for decorative work as well as scroll, but it rewrites both shutdown paths
     and both are currently correct. Not worth the risk for measured-free work.
   - **Frame-rate-independent particle motion.** The snow genuinely does fall at
     double speed on a 120Hz display, so this is a real bug, but the fix changes
     what Arsh has been looking at on his own machine. His call, not a silent
     one.
   - **The phase cross-fade dipping to 75% coverage at its midpoint**, so every
     chapter change washes slightly toward the flat ground. Holding the outgoing
     layer and cutting it after would fix it. It is a visual design change to
     the spine of the page and wants his eye first.
   - **The hero typewriter starts while its container is still translating**, so
     the caret chases a moving target for its first line. Moving the start from
     0.7 to 1.05 fixes it and adds about 200ms to the hero settle. Choreography
     he has already approved, so it wants his word.
   - **`.claim-wipe` and `.state-row` match zero elements**: two reveal blocks
     and their CSS are dead. Zero runtime cost, so left alone.
11. **Reference he pointed at, 2026-08-29: the "Handpicked" photo ring on
   sobha-privy-collection.com (section `#selection`, Vide Infra).** He asked
   how the images are animated; the full read is in
   `_source/reference/sobha-handpicked-carousel.md`, with three frames of the
   real render and the beautified plugin beside it. The short version: not
   DOM. Thirteen photos are textures on tiles bent onto a radius-15 ring with
   three.js's CurveModifier (`PlaneGeometry(5, 2.83, 10, 1)`, unlit
   `MeshBasicMaterial`), drawn on one transparent canvas pinned for three
   screens while the copy scrolls past at 1:1. Scroll progress flies the
   camera along a five-key cardinal spline (starts outside the ring, pitched
   32 and rolled 30 degrees, ends dead ahead and rolled 8) and turns the ring
   half a revolution by scroll *velocity* (`0.5 * Δprogress` per frame, so it
   stops when the wheel stops). Opacity is keyed to position on the ring
   (25% at the left-hand point, 100% at the right, about 45% on the far arc,
   which reads as depth). Mouse adds a 1.4 degree tilt and a slow drift.
   Entry and exit are eased by `camera.setViewOffset` (25% of the viewport)
   rather than cut at the sticky boundary. The curved edges he noticed are the
   tell that it is geometry: CSS 3D cannot bend a face. Getting back to it
   has traps (wheel is swallowed by the horizontal slider above it; load
   `/#selection`), also in the note. **Built on 2026-08-30 as the Cloots
   loop** (4.5, "The loop"), on his instruction, in CSS 3D rather than
   three.js for the reasons recorded there. What is open is his eye on it,
   listed in 4.5. **A variant lives on branch `loop-video-upright`** (his
   instruction the same night): the recording upright in the chassis, Ask
   Cloots on the loop with the other four stills, captions swapped. `main`
   keeps Ask Cloots upright. Compare them by eye before either is merged.
12. **The tester count.** 1,000+ external testers is on the page; in the same
   sentence he said 3,000+ users. Confirm the real figure and what it counts
   (testers, or sessions) before the site goes public. See 3.1.
