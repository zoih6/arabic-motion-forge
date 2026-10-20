---
name: arabic-type
description: Arabic typography correctness — shaping, RTL flow, diacritics, lam-alef, per-word reveal, bidi isolation, font loading and metrics. Mandatory for any project with Arabic on screen; use before animating any Arabic text, no exceptions.
---

# Arabic type

Non-negotiables (violations have ruined real renders):

1. **Shape first, move second.** Text animates as whole shaped words/lines (canvas `ctx.direction='rtl'` or DOM with proper font). Never per-character splitting — Arabic letters are contextual; splitting breaks connection. `safeTextUnits(text,{mode:'word'|'line'})` enforces; `mode:'char'` on Arabic throws — that is the guard, keep it.
2. **Font ready before frame one.** `document.fonts.load('700 64px "IBM Plex Sans Arabic"')` then `check` inside `filmReady`'s await; render at build time only after fonts resolve. Kit ships IBM Plex Sans Arabic + OFL in `assets/fonts/`; @font-face the file, don't trust system fonts.
3. **Real metrics, measured.** `fitText()`/`measureText` for width, `actualBoundingBoxAscent/Descent` for diacritic clearance; line boxes ≥1.35× size when tashkeel present. Test with the longest actual string incl. ٍ ُ ِ.
4. **Reveal via masks/clip, not fades on split glyphs.** Shaped-word matte bands (per-phrase reveal), trim-path underline strokes alongside text (stroke path computed independently; its head marker uses the same arc-length parameter).
5. **Bidi hygiene.** Latin digits/units inside RTL: isolate (`\u2066…\u2069` or CSS `unicode-bidi:isolate`); percent/LRN patterns tested at 1080p and 25% thumbnail. Numerals: choose Arabic-Indic ٠١٢ or Western consistently per brief; state the choice in style.json.
6. **lam-alef & final forms.** Verify لا connection and ـه/ـة finals at full scale in a still; watch descenders colliding on tight lines; `letter-spacing` on Arabic = tracking only ≥0.02em and never mid-word (breaks connection visually).
7. **Copy fidelity.** Approved wording is law — never re-phrase, re-vowel, or drop alif to fit a box; instead scale/fit or request an edit through the user.
8. QA: word-boundary screenshots at entrance mid-frame (no half-shaped glyph), reverse-check any "typewriter" claim: this kit implements matte-reveal equivalents, never claim AE-native Write-On.
