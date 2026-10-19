# CREDITS — AI Film Studio

<div align="center">

**Designed & Built by**

# Waseem Alzobiri

*هندسة الأنظمة · هندسة التوجيهات · معمارية الـ Workflows*

</div>

---

## 👤 المالك والمنشئ

| | |
|---|---|
| **الاسم** | Waseem Alzobiri — وسيم الزبيري |
| **الدور** | تصميم وبناء النظام الكامل |
| **المستودع** | [github.com/zoih6/ai-film-studio](https://github.com/zoih6/ai-film-studio) |
| **الترخيص** | MIT |

> **"صُمّم وبُني بواسطة Waseem Alzobiri"**
> *Designed & Built by Waseem Alzobiri*

---

## 🧬 نسب النظام (Lineage)

هذا المستودع هو **النسخة النهائية الموحّدة** لثلاثة أنظمة سابقة طوّرها نفس المنشئ.
كل المحتوى منها مدمج ومطوّر هنا:

| المستودع السابق | ما أُخذ منه | الحالة |
|---|---|---|
| **AI Film Studio v2.1.0** | العمود الفقري M0–M11 (31 workflow)، 10-Layer Prompt Architecture (A–J)، 8 Quality Gates، Memory Conflict Contract، Orchestration Runtime | ✅ مدمج وموسّع |
| **VOX Paper Engine** | محرك الوثائقيات الورقية، DNA الكتابة السردية، حساب الـ Beats، نظام الصوت، حمض الثامبنيل، آلة الحالات التسع، الأقفال النصية الحرفية | ✅ مدمج في `workflows/engines/E1` + `styles/` |
| **VOX Commercial Director** | طاقم 9 أدوار، 10 مراحل إعلانية، محرك الأفكار (12 عدسة)، 8 عوالم بصرية، Product Reference (IMG-00)، بوابات الجودة الست، نمط الهجين | ✅ مدمج في `workflows/engines/E2` + `styles/locks/` |
| **VOX Commercial Director Skill v3.0.0** | Brief بـ 12 حقلًا، مستويات حقيقة المنتج T1–T4، منحنى الطاقة، جداول الزمن، End Card، مصفوفة A/B، Edit Sheet | ✅ مدمج في `schemas/` + `references/specs/` |

### التطور مقابل النسخ السابقة

| الإضافة في v3.0.0 | الأصل |
|---|---|
| 5 محركات متخصصة (E1–E5) | جديد بالكامل |
| 10 عوالم بصرية بأقفال حرفية (LOCK A–J) | تطوير من 8 أقفال |
| LOCK I — Flat Vector Explainer (نمط VOX المسطح) | **جديد بالكامل** |
| LOCK J — Arabic Calligraphic | **جديد بالكامل** |
| أدوات البحث والتحقق (`references/research/`) | **جديد بالكامل** |
| 12 بوابة جودة (كانت 8) | تطوير |
| 23 مخطط إخراج (كانت 13) | تطوير |
| بروتوكول الأقفال النصية | **جديد بالكامل** |
| بروتوكول الاكتشاف (Discovery) | تطوير من النسخ التجارية |
| 9 سكربتات فحص (كانت 5) | تطوير |

---

## 🙏 شكر وتقدير

- **نماذج التوليد** التي اختُبرت عليها المنهجية: Veo, Kling, Runway, Sora, Midjourney, Flux, Nano Banana, GPT Image, Ideogram, Imagen, Seedance, Hailuo, ElevenLabs.
- **المرجعيات المهنية** التي استُلهمت منها الأطر: منهجية الاستوديوهات الوثائقية التحريرية،
  منهجيات وكالات الإعلان الكبرى (Big Idea / Creative Brief / Pre-flight)،
  وأدبيات الـ cinematography (حركة الكاميرا، الإضاءة، المناطق الآمنة).
- **المعيار المعتمد:** Agent Skills Standard — Progressive Disclosure (3 tiers).

---

## 📜 إشعار الاستخدام

- الكود والنصوص مرخّصة تحت **MIT** — استخدمها بحرية تجاريًا وشخصيًا.
- عند إعادة النشر أو التفرّع (fork)، **يُرجى الإبقاء على إسناد المنشئ** (Waseem Alzobiri).
- الأقفال النصية في `styles/locks/` **لا تُعدّل** — تعديلها يكسر ثبات الأسلوب الذي صُمّمت لحمايته.
  إن أردت تعديلها، أنشئ قفلًا جديدًا (LOCK K+) ولا تستبدل الموجود.

---

<div align="center">

**AI Film Studio v3.0.0** · Designed & Built by **Waseem Alzobiri** · MIT License

</div>
