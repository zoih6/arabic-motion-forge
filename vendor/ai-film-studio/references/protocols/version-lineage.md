# Version Lineage — v1.1

## التسمية
`SC01_SH03_FR02_v002` = Scene / Shot / Frame / Version.

للأصول الأخرى:
- Character: `CHAR-LAYAN-01_v001`
- Style: `STYLE-01_v001`
- World: `WORLD-01_v001`
- Motion: `MOT-SC01_SH03_v001`
- Audio: `AUD-SC01_SH03_DLG_v001`
- Composite: `CMP-SC01_SH03_v001`

## Lineage
كل Version يسجل:
`parent_id`, `change_reason`, `changed_variables`, `created_by`, `created_at`, `status`.

## قاعدة الإصلاح
عند فشل توليد أصل معتمد: لا تعدّل الأصل نفسه. أنشئ `v002`، وسجل المتغير الوحيد الذي تغيّر، ثم اربطه بـ `parent_id=v001`.

## حالات الأصل
`DRAFT → REVIEW → APPROVED → SUPERSEDED` أو `DRAFT → FAIL → REPAIR → REVIEW`.
