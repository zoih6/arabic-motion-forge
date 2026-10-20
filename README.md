# Arabic Motion Forge

**An agent operating system for original Arabic motion design — layered choreography, Arabic-safe typography, deterministic rendering, crash-safe sessions.** Not a template pack: every project is authored from the brief; the kit guarantees the machinery, the quality contract and the evidence.

v2.3.0: creative ideation engine (hooks, wild cards, cliché blacklist), motion-focused web-research registry, true ASR tool with approved-copy alignment + sync verifier, objective motion audit (anti-slideshow), typography system dictionary + OFL font fetcher, AE bridge export, quick mode + one-command gate aggregator. v2.2.0: spec-reframe gate (chaotic one-line requests are professionally rewritten, never executed literally), bounded web-research agent, inspiration engine + 6 dictionaries, **true-3D runtime module**, mandatory ≤30 s approval preview before long renders, workspace quota guardian, capped delivery (light ≤25 MiB / hi ≤50 MiB) landing in the workspace — never an `out/` folder. `runtime/core|canvas` remain byte-frozen from v1 — old projects render identically (`tools/compat_check.py` proves it on every build).

## Install from a link (< 60 s, self-preparing, verified)

The one-liner installs AND silently warms render dependencies — expect a single READY line, not a tutorial.

```sh
curl -fsSL https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/install.sh | sh
python3 ./motion-forge/tools/doctor.py
```

Any agent anywhere: fetch `AGENTS.md` + `SKILL.md` from this repo root and follow §0. Pinned older version: `--tag v1.0.0` on `tools/install_from_release.py`. Renderer deps (Chromium/FFmpeg) only when you actually render: `tools/bootstrap.py --install`.

## What a film gets from this kit

- **Layered motion, not flat slides** — per AGENTS.md §3: element decomposition, three-stage timing, mattes/trim reveals, multi-plane camera with depth-projection rules, motion-blur policy; every mechanism has a tested contract in `catalog/` (104 entries / 33 mechanisms) and dictionaries (`catalog/dictionaries/`: easings, camera, continuity, styles, direction axes).
- **Arabic correctness** — whole-word shaping, real metrics, bidi isolation, copy-hash lock; guards throw on the shortcuts that break scripts.
- **Originality gate** — `tools/direct.py` generates three structurally distinct concept directions from the topic; `tools/check_directions.py` refuses style-lock until rationales are real and fingerprints avoid the kit example and your prior projects.
- **3D when it matters** — `runtime/spatial.mjs`: real perspective camera, planar-quad texturing with exact affine triangles, stable painter sort, Lambert shading, deterministic orbit keys; rules + honesty bounds in `catalog/dictionaries/spatial-3d.json`. Default stays 2.5D; no fake C4D claims.
- **Deterministic renders** — `seek(t)` purity, 10 s checkpoints streamed into FFmpeg, frame-count/PTS/decode asserts, per-part sha; `--tier draft` for motion review at half cost.
- **Evidence, not vibes** — quality loops bounded to 3 passes with reported numbers; publication verified by anonymous fetch + sha compare; nothing is claimed that the environment cannot prove (no Adobe AE here — Canvas equivalents are labeled as equivalents).
- **Sessions that don't die** — `journal.jsonl` milestones; resume = two reads, never re-asking, never re-rendering verified parts; strict output-size and memory discipline (AGENTS.md §9, `skills/performance`).

## Layout

```
AGENTS.md                canonical agent contract (English)      skills/            16 spec-compliant skills
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
