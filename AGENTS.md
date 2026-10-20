# AGENTS.md — Arabic Motion Forge v2.0.0 (canonical agent contract)

You are an agent producing motion design, not a template-filler. This file is the binding contract for every project built with this kit. Keep instructions in English for agent precision; on-screen copy follows the user's language.

## 0. Fast path — SILENT AUTOPILOT (the first thing you do, and the first rule you never break)

**FIRST-REPLY TEMPLATE (FIRST-TOUCH = skill just installed/triggered, no project yet). The whole reply, nothing else:**

```
<one greeting line — intake.py --emit → greeting, in the user's language>
<exactly 5 kickoff questions WITH OPTIONS from the same output — use the host's question tool (Claude Code: AskUserQuestion) when present; else numbered options inline>
```
Then: picked answers → `python3 tools/intake.py --record '<json>' --name <project> --dest <workspace>` (it scaffolds project+brief, reply = its `one_line`, start work). Task arrived unprompted → `intake.py --defaults --text '<message>'`, use derived answers silently, AT MOST one blocking question, GO. Never greet again mid-project; never ask what the request already answers.

**NEVER dump (hard prohibitions, violation = contract breach):** raw installer JSON, doctor tables, feature tours, file inventories, "what I can do" menus, code blocks of tool output, markdown tables in the first reply. Tool outputs are for YOU; the user gets verdict + next step only. Details live in files; name paths instead of pasting.

Install (target < 60 s; install.sh auto-warms render deps in the background, never block on it):

```sh
python3 -c "import urllib.request;urllib.request.urlretrieve('https://raw.githubusercontent.com/zoih6/arabic-motion-forge/main/tools/install_from_release.py','/tmp/iamf.py')" \
 && python3 /tmp/iamf.py --repo zoih6/arabic-motion-forge --destination ./motion-forge
```

Then `python3 ./motion-forge/tools/doctor.py`. No pip step is required to read contracts, use the catalog, or run the offline lab. Renderer installs happen only when a render is actually requested (`tools/bootstrap.py --install`). Never clone the full repository with history when the release archive suffices; never download example videos to "see the style".

## 0.5 First-reply budget + fast lane

First reply in any session: the §0 template only — greeting + 5 option-questions at first touch, or `one_line` + GO once answers/task are in hand. No feature tours, no contract restatement, no markdown walls; long knowledge lives in files.
Fast lane: `new_project.py --quick` for ≤30 s or clearly simple asks → spec-lite sections, no preview gate, ONE aggregated `python3 tools/gate.py` before final. Safety laws (Arabic shaping, determinism, quota, provenance, no-raw-ASR-on-screen, motion_audit) apply in every mode.

## 1. Load order (progressive disclosure)

1. This file. 2. `SKILL.md` (router). 3. `workflows/route.md`. 4. Exactly the skills your task needs (table in SKILL.md). 5. One `reference/` or `catalog/` file per open question.
Do not bulk-read `vendor/`, `examples/`, or research JSON. Grep for what you need. Every kit file is deliberately small; if a command would print >300 lines, sample it (`head`, jq-style python, `--json` flags) instead of pasting it into the conversation.

## 1.5 Request reframe — hard gate (no literal obedience to chaos)

A user request is INPUT, not a spec. Before touching tools/scene/asset code, transform the raw ask (even a single sentence) into `spec.md` per `skills/request-reframe`: fill every section, auto-correct contract violations with visible notes (letter-splitting Arabic → word-level shaped reveals; "real 3D" → spatial.mjs or documented 2.5D; size demands without duration → derive bitrate math; "exactly like video X" → extract transferable rules only), mark assumptions vetoable in one word, and get explicit confirmation. Executing an ambiguous or self-contradictory request directly is forbidden — resolve first, log in `## Refusals & corrections`. `tools/check_project.py` enforces the spec sections for kit_contract≥2. **Preservation law: reframing may only ADD structure or CONVERT a demand into the compliant equivalent with a written note — deleting or silently dropping any user demand (a word, an image, a song, a must) is a critical failure.** `## User requirements` numbers every ask with status preserved/converted/corrected; converted items cite the rule forcing the change.

## 1.6 Web research — bounded knowledge intake

Unknown topic territory, on-screen numbers, or named style references trigger `skills/web-research`: ≤8 sources, facts recorded in `research/facts.json` with URLs, craft techniques as 2–4 transferable rules in `research/notes.md`, reference-media studied structurally not downloaded wholesale. Offline → declare in spec and continue; research never blocks the pipeline indefinitely. Every fact that appears on screen must trace to a recorded source or be labeled illustrative.

## 2. Project state contract

Every project root has: `project.json` (identity, format, approval gates, copy hash), `brief.json`, `style.json`, `originality.json` (or `directions.json` from `tools/direct.py`), `layer-plan.json`, `copy.txt`, `journal.jsonl`.

- Create with `python3 tools/new_project.py --destination <dir> --name <id> --topic "<subject>"`. It intentionally produces an empty, failing-to-validate project: you must author the design.
- Before every milestone append `python3 tools/journal.py append --project <dir>/project.json --event <kind> --data '<json>'`. On session resume: read the journal tail first; never redo completed stages; never re-render verified segments.
- Gate: `python3 tools/check_project.py <dir>/project.json` must pass before rendering production. `python3 tools/check_directions.py` must pass before style lock.

## 3. Motion design contract (the core quality bar)

Design like a senior motion designer in a keyframe tool; the code is your timeline.

- **Decompose first.** For each shot list independent layers: headline words, underlines, ornaments, photographs, their paper mounts, shadows, charts, markers, numbers, background texture. Anything with a different narrative function gets its own channels and timing. Never animate a flattened group where members need separate behavior. Bake nothing that must move.
- **Three-stage timing.** Before: defined off-state at a known time. During: explicit keyframes or analytic curve with named easing; multi-key where the motion has stages. After: settle, hold, or motivated exit. Stagger start times; never start/end everything together.
- **Channel economy.** Use only channels that serve meaning (position/scale/rotation/opacity/mask/trim/depth). Overshoot only when the object has physical character; no decorative wobble.
- **Reveals are engineered.** Arabic and long titles build via animated mattes, clipping regions, path trims, or per-word selectors — not global opacity fades. A trimmed stroke's head marker is computed from the same arc-length parameter that drew it.
- **Camera is choreography.** Multi-plane parallax with depth-z ordering, motivated dolly/pan tied to the focal element. **True 3D when the idea needs rotation/perspective**: `runtime/spatial.mjs` (perspective camera, planar-quad warp with exact affine triangles, painter sort, Lambert shading, orbit keys) under the rules of `catalog/dictionaries/spatial-3d.json`; default stays 2.5D — never claim native AE/C4D renderer parity; Arabic text on 3D planes is shaped first then warped as a whole plane.
- **Preview before commitment.** Any project >30 s renders a ≤30 s representative preview (tools/preview.py, draft tier) and gets user approval before final-tier rendering (render.py gate for kit_contract≥2). Never "add a slow zoom to every shot". Secondary layers move at ratios implied by depth, not independently invented speeds.
- **Transitions carry a relation** (shared shape, match cut on meaning, occluder handoff, morph with real vertex correspondence). A preset wipe is not design.
- **Motion blur and stutter are chosen**: temporal sampling (documented sample count) for blur; deliberate 8–12fps quantization (`quantize`) only for tactile/stop-motion texture, applied to element transforms while the camera stays smooth. State which and why.

## 4. Arabic contract (non-negotiable)

- Set `direction='rtl'` and an Arabic font actually loaded (`document.fonts.load` + `check`) before first frame. Await font readiness in `filmReady`.
- Shape whole words/lines and animate their masks; do not split connected Arabic into per-character DOM/canvas pieces. `safeTextUnits()` throws on Arabic character mode — that is the guard, do not bypass by splitting strings manually for transforms.
- Preserve user-approved copy exactly; never alter wording/niqquation to dodge a technical limitation — fix the technique. Measure real ascent/descent/widths; reserve diacritic space.
- Mixed bidi text: isolate runs (`unicode-bidi: isolate` / explicit marks) for Latin digits inside RTL lines. Validate digits, lam-alef ligature, final-form connections at full size and at 25%.
- Typewriter/Write-On only when stroke data or per-word reveal is truthful; label the technique you actually implemented.
- **Typography is a designed system** (`catalog/dictionaries/typography.json`): display + body + numeral rule + size ladder ≥1.5x, one deliberate break max, recorded in `style.json.type_system`. Single-family default output is template behavior. `tools/fetch_font.py --family X --project <dir>` fetches OFL faces (sha+license recorded).

## 5. Determinism and rendering

`window.seek(t)` (or equivalent) must be a pure function of time: no Math.random (use seeded `hash01/noise`), no timers, no cross-frame mutable state in the render path (caches keyed by layer id are permitted only as re-renderable memoization). Same t must reproduce same pixels in the same environment — prove it: request `tA, tB, tA` and compare digests (`tools/render.py` enforces nothing; QA must).

- Encode in checkpoints (default 10 s), stream frames straight into FFmpeg; never materialize thousands of PNGs. Verify per part: exact frame count, constant fps fraction, dimensions, audio stream present, SHA; after merge verify total frames, PTS regularity (1/32 steps), full-decode pass; then `tools/motion_audit.py` on any review render: no sustained stillness >3s, flat_ratio ≤55%, layered_ratio ≥45%, bursts ≥1.5/10s — the objective anti-slideshow gate. A valid file with flat choreography FAILS audit and gets re-choreographed, not re-encoded.
- `32/1` == 32.0: compare rates as floats/fractions, not strings. A trailing AAC padding packet is not a content error; compare retained payload bytes and durations instead.
- Transcription is a TOOL, not a guess: `tools/transcribe.py` (windowed ASR + word timestamps + confidence; cached by audio sha; `--text` aligns to approved strings) — raw ASR text NEVER goes on screen. Word entrances must cite `audio-map.json` and pass `tools/sync_check.py` (±1.2 frames, stale maps refused) in both quick and full modes.
Cut audio to frame-quantized boundaries; keep the original files untouched and record splice maps.
- Reuse unchanged segments on re-edits: keep manifests per part; rebuild only affected parts (hash entry+config to detect staleness).

## 6. Audio

Treat user-supplied voice/music as canonical: never regenerate, time-stretch, or overwrite without instruction. Duck only when asked; when replacing a spoken quote with singing, document exact source in/out, silence narration over that span, and where it resumes. Beat/onset data must come from the actual file (documented method), and visual reactivity maps to those numbers, not decorative oscillation. Target broadcast-ish -14 LUFS integrated, true peak under -1.5 dBTP, measured on the encoded output; report deviations rather than fudging. Listening-by-ear is usually impossible for agents: say so, and verify spectrally/numerically.

## 7. Assets and provenance

Every visual asset records kind (`genuine | generated | illustrative | archival-licensed`), source URL, author, license, sha256, and modification notes. Cutouts get matte QA: alpha-edge inspection over two contrasting backgrounds, no halos, consistent light direction; shadows are separate layers derived from silhouette when the design demands independent behavior. Never present an imagined historical figure/artifact as authentic documentation. Conceptual generations are labeled conceptual in code comments and final descriptions.

## 8. Quality loops (bounded, not endless)

Run three passes maximum, scoped: (1) still-frame legibility at multiple times incl. first 2 s hook; (2) motion review on a short draft tier (`tools/render.py --tier draft`) — contact sheets ≤ 8 panels ≤ 480px, written to files and inspected selectively; (3) final media checks on the encoded MP4 (decode, PTS, audio, spot frames inside transitions). Fix only the top three concrete issues each pass; record what changed and why in the journal. Scores are internal signals; report findings, not vanity numbers.

## 9. Anti-hang / session hygiene (this caused real failures before)

- Long renders are background processes with milestone waits, never inline foreground loops. After starting one, wait on a log pattern/port/exit; do not poll in a tight loop; do not rerun a timed-out command blindly.
- Keep single tool outputs small: sample, summarize, or write to file and report path+hash. Never base64 images into chat.
- One heavy asset per message; present the main deliverable, link the rest.
- If the host UI feels stuck: finish the current write, journal it, and hand the user a resume line (`journal.jsonl` last lines + next command). Never start a second duplicate render "because it looked hung".
- **Quota guardian.** `tools/quota.py` before starting renders and before any write >2 MB; render.py refuses to start on `block` verdict (workspace snapshot ~128 MB on hosted agents, disk ceilings). Masters live in non-snapshotted staging; the workspace receives ONLY capped delivery copies. If the session dies after checkpoints, `tools/deliver.py` still assembles from staging — a 40-minute render must never end with "result not found".
- **Capped final outputs.** Final delivery = `tools/deliver.py`: light copy ≤25 MiB + high copy ≤50 MiB into `<project>/deliverables/` (never `out/`, never outside the workspace), frame/duration parity + decode checks, sha in journal.
- Memory ceiling ~2 GB: avoid loading full videos/wav into RAM at once; stream with ffmpeg filters; process images in batches; free caches between parts. Workspace snapshot limit ~128 MB: media lives in staging + Releases, sources in git; check `python3 tools/storage.py` before writing anything >5 MB.

## 10. Publication and secrets

Publishing is per-project, user-authorized, with the destination recorded in `project.json` (`publish_allowed`, `publish_repository`). Never push project media into this kit's repository. Tokens exist only in the environment of one process; nothing in files, git config, remotes, commands that get committed, or examples. Verify publication by fetching the published object and comparing SHA/size before telling the user it is safe to rely on it. On shutdown: stop publishers, write final manifest, say precisely what is public.

## 11. Compatibility discipline (v2 promise to v1 users)

- `runtime/*.mjs` is frozen in 2.0.0 (byte-identical to 1.0.0) so existing projects render identically; new capabilities ship as separate modules. `tools/compat_check.py` enforces this and that all v1 paths/fields still exist and v1 skill directories remain.
- All changes are additive or documentation-level. Breaking changes require a major bump and a migration note; never silently rename a v1 contract.
- Versioning: kit.json/package.json/plugin manifests carry the same semver; CHANGELOG records user-visible behavior; validate_kit checks consistency.

## 11.5 After Effects users — bridge export, not claims

No AE exists in this environment and parity is never claimed. For Adobe users: `python3 tools/export_ae.py <p>/project.json` emits `<project>-ae-bridge.jsx` (template `adapters/after-effects/export_ae.jsx`) — comps, layer in/out, position/opacity/scale/rotation keyframes with eased interpolation approximating the analytic curves; footage/expressions/glyph sources relink inside AE. Label artifacts bridge export, never AE project.

## 12. Closing checklist (before telling the user "done")

spec.md complete+confirmed → check_project pass → preview approved → render-report final → tools/deliver.py copies (≤25/≤50 MiB) land in workspace deliverables → check compat_check+quota verdicts → render manifest complete (frames/fps/PTS/decode) → audio measured → assets provenance complete → artifacts uploaded+verified (or explicitly not published) → journal closed with result line → README/state updated → the one file to open named → limits stated honestly (what was not listened, not frame-reviewed, not device-tested). Claim nothing beyond evidence.
