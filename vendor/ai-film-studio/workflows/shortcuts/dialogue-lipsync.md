---
name: shortcut-dialogue-lipsync
description: حوار متحرك مع مزامنة شفاه
tier: 2
parent: workflows/M6c-dialogue-lipsync.md
duration: 5-10 min
---

# Shortcut: Dialogue / Lip-Sync

## Entry Conditions
- ✅ طلب: "حوار"، "شفاه متحركة"، "مزامنة كلام"
- ✅ صورة/شخصية موجودة
- ❌ لا تحتاج مشاهد أخرى

## Core Workflow (7 خطوات)

### 1. حدد الاستراتيجية (2 min)
ارجع لـ `workflows/M6c-dialogue-lipsync.md` § 4 استراتيجيات:

| الاستراتيجية | النموذج | متى |
|---|---|---|
| **Native Audio** | Veo 3, Sora | أبسط، 70-85% دقة |
| **Regenerate with Audio** | Hedra, Audio2Face | تحكم منفصل، 75-90% |
| **Dubbing Post** | ElevenLabs + manual sync | أعلى دقة، 90-95% |
| **Avoid** | voiceover_only | عندما الفم مغلق أو من الخلف |

### 2. اكتب النص (1 min)
- نص الحوار (عربي/إنجليزي)
- Direction: "هادئ، واثق، بطيء..."
- اللهجة

### 3. ولّد الصوت (2 min)
- ElevenLabs: voice clone + text → audio
- معالجة: Adobe Podcast enhance

### 4. ولّد الفيديو (2-5 min)
- حسب الاستراتيجية المختارة
- 3-5 محاولات
- اختر الأفضل

### 5. تحقق من المزامنة (1 min)
- هل الشفاه تتطابق؟
- هل الإيقاع صحيح؟
- هل الصوت واضح؟

### 6. Fallback (1 min، إذا فشلت)
- انتقل لاستراتيجية أقل (Voiceover Only)
- أو أضف subtitle_overlay

### 7. اخلط في Assembly (1 min)
- premiere/davinci: audio + video sync
- ducking: موسيقى تنخفض تحت الحوار

## Quality Gate
- **G6 (Text):** نص حرفي
- **G7 (Audio):** LUFS + lip-sync
- **Hard:** لا نص مشوّه

## Output
- فيديو مع حوار متزامن (MP4)
- dialogue audio file
- script reference

## Common Mistakes
- ❌ كلام سريع جدًا (صعب المزامنة)
- ❌ وجه جانبي (profile) — يفضل مستقيم
- ❌ إضاءة ضعيفة على الوجه
- ❌ تجاهل الـ fallback

## Next Step
- لإضافة موسيقى/sfx → `workflows/M6-audio.md`
- للدمج في فيلم → `workflows/M0-intake.md`
- للقياس → `quality/checklist.md`
