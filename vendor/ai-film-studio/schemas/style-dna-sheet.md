# ورقة Style DNA — [PROJECT_NAME]

> انسخ هذا القالب واملأه بعد تحليل مراجع المستخدم.
> المصدر المنهجي: `workflows/M11a-reference-analyst.md`

**المراجع المحللة:** [عدد] صورة
**تاريخ التحليل:** [YYYY-MM-DD]
**حالة الـDNA:** مسودة / معتمد

---

## 1. Color Palette

| الدور | Hex | الملاحظة |
|---|---|---|
| Background | `#______` | warm / cool / dark / light |
| Hero Typography | `#______` | |
| Accent / Punch | `#______` | |
| Supporting / Neutral | `#______` | |
| Depth / Shadow | `#______` | |

**Color Temperature:** warm / cool / neutral / high-contrast

> ⚠️ إن لم تستطع قراءة القيمة بدقة، اكتب نطاقًا وعلّمه «تقريبي». لا تخترع.

**الأدوار الناقصة في المراجع:** [اذكر، أو «لا شيء»]

---

## 2. Typography DNA

| الحقل | القيمة |
|---|---|
| Weight | ultrablack / bold / medium / light |
| Width | condensed / normal / extended |
| Category | sans-serif / serif / display / handwritten / kufi / naskh |
| Hero Word Coverage | ____% من عرض الكادر |
| Supporting Coverage | ____% |
| Letter Spacing Feel | tight / normal / wide |
| Aesthetic Label | editorial / minimal / expressive / corporate / street / luxury |

### للعربية
| الحقل | القيمة |
|---|---|
| العائلة المقترحة (Hero) | Cairo / Tajawal / Alexandria / IBM Plex Sans Arabic / Reem Kufi / Amiri |
| العائلة المقترحة (Supporting) | |
| الوزن | 200–1000 |
| الترخيص | OFL / تجاري — **تحقّق** |
| Middle Eastern text engine | ⚠️ يجب تفعيله في After Effects |

---

## 3. Composition DNA

| الحقل | القيمة |
|---|---|
| Layout Type | centered / asymmetric / grid-based / editorial / dynamic |
| Negative Space | minimal / moderate / heavy |
| Subject Position | center / left / right / absent |
| Typography Placement | behind subject / in front / full frame / corner-anchored |
| Depth Layer Count | flat=1 / layered=2 / multi-layer=3+ |
| Visual Dominant | typography / subject / graphic element |

---

## 4. Motion DNA — ⚠️ مُستدل لا مُستخرج

| الحقل | القيمة | الدليل البصري |
|---|---|---|
| Energy Level | calm / moderate / high / explosive | [ما الذي استُدل منه] |
| Motion Style | smooth-cinematic / punchy-editorial / liquid / mechanical / organic | |
| Transition Feel | soft / sharp / whip / morph / hard-cut | |
| Pacing | slow / medium / fast / variable | |

---

## 5. Easing Standard — مشتق من مستوى الطاقة

| الطاقة | Hero | Supporting | Punch |
|---|---|---|---|
| calm / moderate | `cubic-bezier(0.4, 0, 0.2, 1)` | `cubic-bezier(0, 0, 0.2, 1)` | — |
| high | `cubic-bezier(0.22, 1, 0.36, 1)` | `cubic-bezier(0, 0, 0.2, 1)` | `cubic-bezier(0.68, -0.55, 0.27, 1.55)` |
| explosive | `cubic-bezier(0.16, 1, 0.3, 1)` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | `cubic-bezier(0.68, -0.55, 0.27, 1.55)` |

**المعتمد لهذا المشروع:**
- Hero: `cubic-bezier(________)`
- Supporting: `cubic-bezier(________)`
- Punch: `cubic-bezier(________)`

---

## 6. Graphic Element DNA

| الحقل | القيمة |
|---|---|
| Shape Language | geometric / organic / minimal / decorative |
| Line Usage | none / minimal / moderate / heavy |
| Texture | flat / grain / glow / shadow / clean |
| Layout Aesthetic | magazine / social-native / luxury / street / corporate |

---

## 7. Style DNA Summary

> [2–3 جمل تصف النظام البصري كتوجيه إبداعي يحكم كل المشاهد]

---

## 8. اختبار الجودة الخماسي

| الاختبار | السؤال | النتيجة |
|---|---|---|
| الاختلاف | هل يميّز هذا المشروع عن غيره؟ | ✅ / ❌ |
| القابلية للتنفيذ | هل كل حقل قابل للتحويل إلى قيمة رقمية أو برومبت؟ | ✅ / ❌ |
| التتبع | هل كل حقل مشتق من مرجع فعلي؟ | ✅ / ❌ |
| الاتساق | هل الحقول متسقة (لا خط light + طاقة explosive)؟ | ✅ / ❌ |
| الاكتفاء | هل يكفي لإنتاج 10 لقطات متسقة؟ | ✅ / ❌ |

---

## 9. تغطية المراجع

| المحور | مغطى؟ | المصدر | الملاحظة |
|---|---|---|---|
| اللون | ✅ / ⚠️ / ❌ | | |
| التكوين | | | |
| الطباعة | | | |
| الإضاءة | | | |
| الحركة | | | |

**المحاور الناقصة:** [اذكر]
**توصية:** بحث مكمّل عبر `workflows/M11b-visual-research.md` للمحاور: [____]

---

## 10. التناقضات المكتشفة

| التناقض | الحل |
|---|---|
| [مثال: خط light + طاقة explosive] | [القرار والمبرر] |

---

## 11. من الـDNA إلى التنفيذ

### قرار النموذج
| الغرض | الأداة | السبب |
|---|---|---|
| خلفيات | Nano Banana 2 | 9:16 أصلي |
| نصوص | After Effects text layers | طبقة حقيقية، لا بكسلات |
| عناصر رسومية | GPT Image 2 + chroma key | دقة الشكل |
| خلفية متحركة (اختياري) | Omni Flash | 10s متصلة |

### ما لا يُولَّد
- [ ] النصوص — طبقات نصية حقيقية
- [ ] الشعارات — من الملف الأصلي
- [ ] الواجهات — لقطات حقيقية

### المنطقة الآمنة المعتمدة
```
علوي:   ____% (12% موصى به للعناصر الحرجة)
سفلي:   ____% (25% موصى به للعناصر الحرجة)
جانبي:  ____% (15% من جانب أيقونات المنصة)
```
