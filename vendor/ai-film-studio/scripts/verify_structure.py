#!/usr/bin/env python3
"""
فاحص مهارة ai-film-studio v2.0.1
يفحص:
  1. سلامة البنية (الهيكل الجديد: workflows/, schemas/, references/, quality/, scripts/, examples/)
  2. صحة YAML frontmatter في SKILL.md
  3. سلامة الروابط الداخلية
  4. توثيق القيود والمفاهيم الحرجة
  5. الـ Hard Gates (G4, G8)
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FAIL, WARN = [], []
def fail(m): FAIL.append(m)
def warn(m): WARN.append(m)
def ok(m):   print(f"  ✓ {m}")

# ── 1. البنية (الهيكل الجديد v2.0.1) ───────────────────────
print("\n[1] فحص البنية (v2.0.1 Agent Skills Standard)")
REQUIRED = [
    # tier 1
    "SKILL.md", "README.md", "CHANGELOG.md",
    # tier 2: workflows
    "workflows/intent-router.md", "workflows/README.md",
    "workflows/M0-intake.md", "workflows/M1a-creative-direction.md",
    "workflows/M1b-concept-expansion.md", "workflows/M1c-research-lab.md",
    "workflows/M2-narrative.md", "workflows/M3a-shot-design.md",
    "workflows/M3b-shot-list.md", "workflows/M4a-continuity.md",
    "workflows/M4b-character-world.md", "workflows/M4c-continuity-qc.md",
    "workflows/M4d-transitions.md", "workflows/M4e-reference-orchestration.md", "workflows/M5a-graphics.md",
    "workflows/M5b-text-motion.md", "workflows/M6-audio.md",
    "workflows/M6b-sound-design.md", "workflows/M6c-dialogue-lipsync.md",
    "workflows/M7a-prompt-architecture.md", "workflows/M7b-image-prompts.md",
    "workflows/M8a-motion-prompts.md", "workflows/M8b-motion-direction.md",
    "workflows/M8c-animation-ready.md", "workflows/M8d-motion-graphics.md",
    "workflows/M9a-executive-producer.md", "workflows/M9b-quality-gates.md",
    "workflows/M9c-preflight.md", "workflows/M9d-localization.md",
    "workflows/M10a-production-architecture.md", "workflows/M10b-hybrid-assembly.md",
    "workflows/M10c-edit-color.md", "workflows/M11a-reference-analyst.md",
    "workflows/M11b-visual-research.md",
    # shortcuts
    "workflows/shortcuts/concept-only.md", "workflows/shortcuts/single-prompt.md",
    "workflows/shortcuts/image-generation.md", "workflows/shortcuts/image-to-video.md",
    "workflows/shortcuts/motion-graphics.md", "workflows/shortcuts/dialogue-lipsync.md",
    "workflows/shortcuts/repair.md",
    # tier 3: schemas
    "schemas/README.md", "schemas/production-blueprint.md",
    "schemas/image-prompts-package.md", "schemas/motion-prompts-package.md",
    "schemas/audio-package.md", "schemas/assembly-guide.md",
    "schemas/concept-deck.md", "schemas/style-dna-sheet.md",
    "schemas/state/project-memory.md", "schemas/state/continuity-bible.md",
    "schemas/state/frame-chain.md", "schemas/state/asset-registry.md",
    "schemas/state/decision-log.md", "schemas/state/risk-register.md",
    "schemas/state/quality-gates-log.md",
    # tier 3: references
    "references/README.md", "references/protocols/agent-contract.md",
    "references/protocols/output-protocol.md", "references/protocols/decision-policy.md",
    "references/protocols/production-state-machine.md", "references/protocols/interaction-flow.md",
    "references/protocols/version-lineage.md",
    "references/specs/prompt-architecture.md", "references/specs/continuity-bible-schema.md",
    "references/specs/transition-types.md", "references/specs/audio-decision-tree.md",
    "references/specs/text-execution-matrix.md", "references/specs/model-matrix.md",
    "references/specs/model-adapters.md", "references/specs/prompt-compiler.md",
    "references/specs/shot-contract.md", "references/specs/scene-shot-dna.md",
    "references/specs/prompt-patterns.md", "references/specs/prompt-quality-gate.md",
    "references/specs/copywriting-and-text-in-images.md",
    "references/knowledge/failure-modes.md", "references/knowledge/context-assembly.md",
    "references/knowledge/memory-schema.md", "references/knowledge/memory-lifecycle.md",
    "references/knowledge/memory-context-policy.md", "references/knowledge/project-memory.md",
    "references/knowledge/session-continuation.md",
    # tier 3: quality
    "quality/quality-gates.md", "quality/checklist.md", "quality/self-audit.md",
    # ── v3.0.0: المحركات ──
    "workflows/engines/README.md",
    "workflows/engines/E1-documentary-engine.md",
    "workflows/engines/E2-commercial-engine.md",
    "workflows/engines/E3-hybrid-commercial.md",
    "workflows/engines/E4-series-engine.md",
    "workflows/engines/E5-bulk-production-pipeline.md",
    # ── v3.0.0: مكتبة الأنماط ──
    "styles/README.md", "styles/index.md", "styles/style-pack-template.md", "styles/oversized-ink-editorial.md",
    "styles/locks/README.md",
    # ── v3.0.0: مراجع جديدة ──
    "references/specs/beat-architecture.md",
    "references/specs/idea-engine.md",
    "references/specs/product-truth.md",
    "references/specs/entity-ledger.md",
    "references/specs/model-dialects.md",
    "references/specs/thumbnail-dna.md",
    "references/specs/platform-specs.md",
    "references/specs/brief-spec.md",
    "references/knowledge/narrative-writing-dna.md",
    "references/knowledge/voice-system.md",
    "references/knowledge/series-architecture.md",
    "references/knowledge/truth-and-safety.md",
    "references/protocols/discovery-protocol.md",
    "references/protocols/style-lock-protocol.md",
    "references/protocols/engine-interop.md",
    "references/research/README.md",
    "references/research/search-playbook.md",
    "references/research/reference-mining.md",
    "references/research/fact-verification.md",
    "references/research/trend-research.md",
    "references/research/query-library.md",
    # ── v3.0.0: مخططات إخراج ──
    "schemas/brief.md", "schemas/beat-table.md", "schemas/shot-card.md", "schemas/production-sheet.md",
    "schemas/product-sheet.md", "schemas/edit-sheet.md", "schemas/end-card.md",
    "schemas/thumbnail-pack.md", "schemas/delivery-pack.md",
    "schemas/series-bible.md", "schemas/prompts-txt.md",
    # ── v3.0.0: جودة ──
    "quality/gates-extended.md", "quality/pre-flight-checklist.md",
    "quality/ten-second-test.md",
    # ── v3.0.0: مسارات سريعة وأمثلة ووثائق ──
    "workflows/adaptive-production-sheet.md",
    "workflows/shortcuts/thumbnail.md", "workflows/shortcuts/series.md",
    "workflows/shortcuts/documentary.md", "workflows/shortcuts/product-shot.md",
    "examples/paper-collage-documentary.md", "examples/commercial-15s-lock-b.md",
    "docs/architecture.md", "docs/gap-analysis-v3.md", "docs/migration-v2-to-v3.md",
    "CREDITS.md", "LICENSE", "CONTRIBUTING.md",
    # scripts
    "scripts/verify_structure.py", "scripts/verify_functional.py",
    "scripts/verify_motion.py", "scripts/verify_example.py", "scripts/verify_all.sh",
    "scripts/prompt_compiler.py", "scripts/test_prompt_compiler.py", "scripts/verify_production_sheet.py", "scripts/verify_style_k.py",
    # examples
    "examples/coffee-short.md", "examples/energy-drink-ad.md",
]
for r in REQUIRED:
    p = ROOT / r
    if not p.exists():
        fail(f"ملف مفقود: {r}")
    elif p.stat().st_size < (100 if str(p.relative_to(ROOT)).startswith("schemas/state/") else 200):
        fail(f"ملف شبه فارغ: {r} ({p.stat().st_size} بايت)")
    else:
        ok(f"{r} ({p.stat().st_size:,} بايت)")

# ── 2. YAML frontmatter في SKILL.md ────────────────────────
print("\n[2] فحص YAML frontmatter في SKILL.md")
sk = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", sk, re.S)
if not m:
    fail("SKILL.md لا يبدأ بـ YAML frontmatter")
else:
    fm = m.group(1)
    for field in ["name:", "description:"]:
        if field not in fm:
            fail(f"حقل مفقود في frontmatter: {field}")
        else:
            ok(f"حقل {field.rstrip(':')} موجود")
    name = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.*)$", fm, re.M)
    if name and name.group(1).strip() != "ai-film-studio":
        warn(f"اسم المهارة '{name.group(1).strip()}' لا يطابق اسم المجلد")
    desc_len = 0
    if desc:
        desc_value = desc.group(1).strip()
        if desc_value in {"|", ">"}:
            desc_body = re.split(r"^[A-Za-z_][\w-]*:", fm[desc.end():], maxsplit=1, flags=re.M)[0]
            desc_len = len(desc_body.strip())
        else:
            desc_len = len(desc_value)
    if desc and desc_len < 100:
        warn("الوصف قصير — قد لا يُفعَّل التوجيه التلقائي بشكل موثوق")
    else:
        ok(f"طول الوصف {desc_len} حرفًا (كافٍ للتوجيه)")

# فحص أن SKILL.md ≤ 200 سطر (Progressive Disclosure)
sk_lines = sk.count("\n")
if sk_lines > 250:
    warn(f"SKILL.md طويل ({sk_lines} سطر) — يُفضَّل ≤ 200 سطر لـ tier 1")
else:
    ok(f"SKILL.md = {sk_lines} سطر (≤ 250، مناسب لـ tier 1)")

# ── 3. الروابط الداخلية ────────────────────────────────────
print("\n[3] فحص الروابط الداخلية")
all_md = list(ROOT.rglob("*.md"))
refs = set()
for p in all_md:
    if '.git' in str(p): continue
    content = p.read_text(encoding="utf-8")
    # ملفات التاريخ والتحليل المقارن تحمل واسمًا صريحًا يسمح بمراجع مستودعات سابقة
    if "verify_links: allow-legacy" in content[:400]:
        continue
    # مطابقة المسارات في backticks (الهيكل الجديد فقط)
    for r in re.findall(r"`((?:workflows|schemas|references/[a-z]+|quality|examples|scripts)/[^`]+?\.md)`", content):
        refs.add(r)

# تجاهل CHANGELOG (تاريخ، يحوي إشارات قديمة متعمدة)
missing = []
for r in sorted(refs):
    # تجاهل المراجع ذات النمط (مثل M*.md)
    if '*' in r or '?' in r:
        continue
    if not (ROOT / r).exists():
        missing.append(r)

if missing:
    for mm in missing[:20]: fail(f"مرجع محتمل مفقود: {mm}")
    if len(missing) > 20: fail(f"... و {len(missing) - 20} مرجع إضافي")
else:
    ok(f"{len(refs)} مرجع محتمل، كلها صالحة")

# ── 4. المفاهيم الحرجة (v2.0) ──────────────────────────────
print("\n[4] فحص المفاهيم الحرجة (v2.0)")
CORPUS = "\n".join(p.read_text(encoding="utf-8") for p in all_md)
MUST = [
    ("10-Layer",                "10-Layer A-J architecture"),
    ("A-J",                     "طبقات A-J"),
    ("Continuity Bible",        "Continuity Bible"),
    ("Frame Chain",             "Frame Chain"),
    ("Quality Gate",            "Quality Gate"),
    ("Single Locked",           "Single Locked Visual Plane"),
    ("5 Output",                "5 Output Packages"),
    ("M0",                      "مرحلة M0"),
    ("M11",                     "مرحلة M11"),
    ("G4",                      "Quality Gate G4"),
    ("G8",                      "Quality Gate G8"),
    ("Hard Gate",               "Hard Gates مذكورة"),
    ("backward",                "Backward compatibility"),
    ("progressive",             "Progressive Disclosure"),
    ("tier",                    "tier concept"),
    ("seedance",                "Seedance model"),
    ("midjourney",              "Midjourney model"),
    ("ElevenLabs",              "ElevenLabs"),
    ("Suno",                    "Suno music"),
    ("Hedra",                   "Hedra lip-sync"),
    ("Veo 3",                   "Veo 3"),
    ("-14 LUFS",                "Master LUFS YouTube"),
    ("post_overlay",            "post_overlay strategy"),
    ("brand_orange",            "color hex format"),
]
for needle, label in MUST:
    if needle.lower() in CORPUS.lower(): ok(label)
    else: warn(f"مفهوم مذكور بشكل مختلف: {label} ('{needle}')")

# ── 5. النماذج والقيود الموثقة ─────────────────────────────
print("\n[5] فحص النماذج والقيود الموثقة")
MODELS = [
    ("bytedance/seedream-4",    "Seedream 4 image"),
    ("bytedance/seedance-2.0",  "Seedance 2.0 video"),
    ("midjourney-v6",           "Midjourney v6"),
    ("kling-2.1",               "Kling 2.1"),
    ("runwayml/gen4",           "Runway Gen-4"),
    ("stability/sdxl",          "SDXL"),
    ("gemini-3",                "Gemini 3"),
    ("ElevenLabs",              "ElevenLabs TTS"),
    ("Suno",                    "Suno v3.5"),
    ("Hedra",                   "Hedra lip-sync"),
]
for needle, label in MODELS:
    if needle in CORPUS: ok(f"نموذج: {label}")
    else: warn(f"نموذج غير مذكور: {label}")

# ── 6. النتيجة ────────────────────────────────────────────
print("\n" + "="*64)
if FAIL:
    print(f"❌ فشل: {len(FAIL)}")
    for f in FAIL[:20]: print(f"   • {f}")
    if len(FAIL) > 20: print(f"   ... و {len(FAIL) - 20} خطأ إضافي")
    sys.exit(1)
print(f"✅ كل الفحوص البنيوية نجحت ({len(REQUIRED)} ملف مطلوب)")
if WARN:
    print(f"⚠️  تحذيرات: {len(WARN)}")
    for w in WARN[:5]: print(f"   • {w}")
print("="*64)
