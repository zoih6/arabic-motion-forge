# Arabic Motion Forge

**An agent operating system for original Arabic motion design — layered choreography, Arabic-safe typography, deterministic rendering, crash-safe sessions.** Not a template pack: every project is authored from the brief; the kit guarantees the machinery, the quality contract and the evidence.

v2.0.0: English agent contracts, inspiration engine + motion dictionaries, draft-tier QA, session journals (hang-proof resumption), one-command bootstrap. `runtime/` is byte-frozen from v1 — old projects render identically (`tools/compat_check.py` proves it on every build).

## Install from a link (< 60 s, verified, no history, no media)

```sh
curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh
python3 ./motion-forge/tools/doctor.py
```

Any agent anywhere: fetch `AGENTS.md` + `SKILL.md` from this repo root and follow §0. Pinned older version: `--tag v1.0.0` on `tools/install_from_release.py`. Renderer deps (Chromium/FFmpeg) only when you actually render: `tools/bootstrap.py --install`.

## What a film gets from this kit

- **Layered motion, not flat slides** — per AGENTS.md §3: element decomposition, three-stage timing, mattes/trim reveals, multi-plane camera with depth-projection rules, motion-blur policy; every mechanism has a tested contract in `catalog/` (104 entries / 33 mechanisms) and dictionaries (`catalog/dictionaries/`: easings, camera, continuity, styles, direction axes).
- **Arabic correctness** — whole-word shaping, real metrics, bidi isolation, copy-hash lock; guards throw on the shortcuts that break scripts.
- **Originality gate** — `tools/direct.py` generates three structurally distinct concept directions from the topic; `tools/check_directions.py` refuses style-lock until rationales are real and fingerprints avoid the kit example and your prior projects.
- **Deterministic renders** — `seek(t)` purity, 10 s checkpoints streamed into FFmpeg, frame-count/PTS/decode asserts, per-part sha; `--tier draft` for motion review at half cost.
- **Evidence, not vibes** — quality loops bounded to 3 passes with reported numbers; publication verified by anonymous fetch + sha compare; nothing is claimed that the environment cannot prove (no Adobe AE here — Canvas equivalents are labeled as equivalents).
- **Sessions that don't die** — `journal.jsonl` milestones; resume = two reads, never re-asking, never re-rendering verified parts; strict output-size and memory discipline (AGENTS.md §9, `skills/performance`).

## Layout

```
AGENTS.md                canonical agent contract (English)      skills/            12 spec-compliant skills
SKILL.md                 router + load order + gates             runtime/           frozen math+canvas core (v1 API)
install.sh               one-shot bootstrap                       catalog/           motions, mechanisms, dictionaries, locks
tools/                   direct, check_directions, compat_check,  reference/         recipes per mechanism, AE equivalence,
  journal, render, doctor, new_project, check_project,             workflows/         route + production docs
  install_from_release, package_core, validate_kit …               tests/             node suite (20) + browser harness
examples/vertical-showcase/  80 s reference film (CODE PROTECTED — study, never copy)
```

## Releases

- **v2.0.0 assets**: verified core zip (no media, no demo scene), demo film, motion lab. Checksums in `SHA256SUMS.txt`; the installer validates before extracting.
- **v1.0.0 remains available** — same repo, tag `v1.0.0`; archive installs identically.

## Honesty ledger

Canvas-based AE-equivalent behavior (documented in `reference/ae-equivalence.md`), not AE-native. Demo covers representative examples per family, not all 104 labels as separate shots. Agent-side audio QA is numeric/spectral; humans should still listen before broadcast.

### للعربية (quick facts)
المدخل للوكلاء: `AGENTS.md` ثم `SKILL.md`. التثبيت من الرابط بأمر واحد أعلاه. كل مشروع يُصمَّم من الصفر؛ الفحص الآلي يمنع سرقة الأنماط ويتحقق من سلامة العربية والحركة والطباعة والتصدير. لا يُدَّعى تنفيذ After Effects أصلي — المكافئات موثقة.
