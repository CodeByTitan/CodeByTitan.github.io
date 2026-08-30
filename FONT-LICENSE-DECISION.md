# Font licensing · decided 2026-08-21

Standalone copy of an addition appended to CLAUDE.md, kept separate because
CLAUDE.md had been written by another session 70 seconds earlier.

## Arsh accepted the risk. Do not re-raise this.

Lumiare (Masyafi Studio, masyafistudio.com, ~$49) and Boreck Display
(ifonts.xyz, "Demo for Personal Use") are both personal-use fonts, and a
portfolio site is commercial use under how essentially every indie foundry
reads that term: its purpose is to get him hired. He was told, and his answer
was to ship it as is. That is settled. It is not a bug, it is not a TODO, and
a future session should not open it again.

## Why the residual risk is genuinely small

The site ships no font file. Both faces are inlined SVG paths built by
`scratch/mkglyphs.py` (see the OUTLINE DISPLAY TYPE block in index.html), so:

- **No redistribution.** Self-hosting a webfont republishes the font file and
  anyone can pull the .otf out of assets/. That is the clean, provable, easily
  enforced violation, and it is not happening here.
- **Letterforms are not what copyright protects.** In the US typeface *designs*
  are uncopyrightable (Eltra Corp. v. Ringer); font *software* is copyrightable
  (Adobe v. SSi). Canada lands similarly. Shipping outlines of the shapes is
  not infringement in either country. What is left is a contract claim off a
  readme bundled with a dafont download, which is thin.
- The "$999 fine" in lumiare/README.txt is a seller's assertion in a text file,
  not a judgment. A private party cannot impose a penalty by declaration.

## The one thing that would actually break this

**Never commit the font files.** Publishing lumiare/Lumiare.otf or
boreck-display-font/*.otf to CodeByTitan.github.io is redistribution, publicly
and provably, whatever the personal-vs-commercial argument says. It converts a
weak contract argument into a straightforward one.

`.gitignore` now covers `lumiare/`, `lumiare.zip`, `boreck-display-font/`,
`boreck-display-font.zip` and `bethany-elingston.rar`. Verified with
`git check-ignore -v`. Keep those entries.

Note: as of this date arsh-portfolio has **no .git of its own**.
`git rev-parse --show-toplevel` from inside it resolves to `/Users/arshsethi`,
the home-directory repo (origin CodeByTitan/SpetX.git). Nothing here is under
version control yet. The .gitignore travels with the folder and applies once
`git init` runs. Re-check the ignore rules at that moment.

Boreck is the shakier of the two: one line of license from an aggregator whose
right to distribute is unclear, no foundry to buy from, nobody to email. The
outlines carry more weight there than they do for Lumiare.
