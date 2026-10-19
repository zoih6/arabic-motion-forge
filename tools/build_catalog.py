from pathlib import Path
import json,csv,re
R=Path(__file__).resolve().parents[1]
families={
'entrance':('الدخول','Slide In, Pop In, Scale Up, Scale Bounce, Spring In, Bounce In, Drop In, Fly In, Flip In, Spin In, Blur In, Fade In, Reveal In, Wipe In, Mask Reveal'),
'physics':('النابض والفيزياء','Spring Motion, Spring Overshoot, Overshoot & Settle, Bounce, Elastic, Inertial Bounce, Wobble, Wiggle, Jiggle, Recoil, Squash & Stretch, Follow Through, Secondary Motion, Damped Oscillation'),
'scrolling':('التمرير والانزلاق','Slide, Scroll, Vertical Scroll, Horizontal Scroll, Rolling Credits, Ticker, Marquee, Push, Pull, Drag, Slide Reveal, Parallax Scroll, Continuous Scroll'),
'reveal':('كشف النصوص','Typewriter, Write On, Character Reveal, Word Reveal, Line Reveal, Tracking Reveal, Mask Wipe, Matte Reveal, Stroke Reveal, Clipping Reveal, Split Reveal, Word-by-Word, Line-by-Line, Text Build'),
'kinetic':('الطباعة الحركية','Character Stagger, Word Stagger, Cascade, Wave, Ripple, Float, Drift, Tracking In, Tracking Out, Character Rotation, Character Lift, Baseline Wave, Text Scramble'),
'transitions':('الانتقالات','Match Cut, Whip Pan, Whip Transition, Push Transition, Wipe Transition, Zoom Transition, Spin Transition, Morph Transition, Mask Transition, Parallax Transition, Seamless Transition, Object Wipe'),
'paths':('الخطوط والأشكال','Line Draw, Trim Paths, Stroke Reveal, Underline Draw, Arrow Draw, Path Follow, Callout Animation, Circle Reveal, Circular Wipe, Shape Morph'),
'timing':('التوقيت والحركة','Keyframe Animation, Ease In, Ease Out, Ease In Out, Graph Editor, Speed Graph, Value Graph, Anticipation, Overshoot, Settle, Stagger, Hold, Motion Blur')}
# canonical mechanism -> (functions, truthful scope, design use)
mechanisms={
 'transform-track':(['track','matrix','layerState'],'implemented','حركة مكانية أو دوران أو حجم له سبب؛ ليست بديلًا عن بناء العنوان.'),
 'anticipation-settle':(['track','spring'],'implemented','تحضير قصير ثم الفعل ثم الاستقرار؛ overshoot محدود ومقصود.'),
 'spring':(['spring','springPresets'],'implemented','حل تحليلي لنابض؛ كتلة وتخميد وصلابة، مستقل عن الإطار السابق.'),
 'ballistic':(['ballistic'],'implemented','سقوط وارتداد تحت الجاذبية مع تناقص الطاقة؛ لا bounce موحد لكل شيء.'),
 'inertia':(['inertia','track'],'implemented','تباطؤ بعد دفع/سحب؛ مسار الإدخال مسجّل لا تفاعل حي في التصدير.'),
 'damped-oscillation':(['recoil','spring'],'implemented','ذبذبة متناقصة أو رد فعل محلي؛ لا اهتزاز دائم بلا معنى.'),
 'seeded-noise':(['noise','hash01'],'implemented','تذبذب مثبت البذرة، محدود السعة، لا عشوائية غير قابلة للإعادة.'),
 'squash-stretch':(['squashStretch'],'implemented','امتداد يحافظ تقريبًا على الحجم؛ يخص مادة مرنة، لا كل النصوص.'),
 'secondary':(['followThrough','track'],'implemented','حركة تابعة متأخرة لها توقيت مستقل وسبب ميكانيكي.'),
 'scroll':(['scrollOffset','track'],'implemented','تمرير محتوى داخل نافذة كشف، مع hold للقراءة عند الحاجة.'),
 'parallax':(['samplePerspective','layerState'],'implemented-2.5d','إسقاط عمق لطبقات مستوية؛ ليس renderer ثلاثي الأبعاد حجميًا.'),
 'alpha-matte':(['maskedSprite','rtlMatte'],'implemented','ألفا قناع مستقلة مضروبة في ألفا المحتوى؛ كشف العربية بعد تشكيلها.'),
 'luma-matte':(['lumaMatte','lumaAlpha'],'implemented-defined-color-model','سطوع Rec.709 موزون على قيم sRGB؛ ليست مطابقة لكل إعدادات ألوان AE.'),
 'iris':(['irisMatte'],'implemented','كشف دائري بقناع حقيقي؛ الحركة ليست scale للنص كله.'),
 'path-trim':(['pathMetrics','trimPath','strokePath'],'implemented','طول قوس مجزّأ، ورأس مؤشر على نهاية المسار نفسها؛ لا ظهور كامل للخط.'),
 'path-follow':(['pathMetrics','pathPoint'],'implemented','موقع ومماس من طول القوس؛ لا سرعة وهمية من بارامتر Bezier وحده.'),
 'contour-morph':(['morphContours','radialShape'],'implemented-with-correspondence','رؤوس متقابلة بنفس العدد والاتجاه؛ يرفض topology غير المدعوم بدل crossfade مزيف.'),
 'range-stagger':(['stagger','selectorWeight','safeTextUnits'],'implemented-with-arabic-guard','تتابع وحدات مستقلة؛ كلمات/سطور للعربية، وحروف منفصلة فقط عند سلامة البنية.'),
 'baseline-wave':(['waveOffset','safeTextUnits'],'implemented-with-arabic-guard','موجة على الكلمات أو الوحدات المعتمدة؛ لا تفكيك للحروف العربية المتصلة.'),
 'tracking':(['safeTextUnits','track'],'conditional','تباعد كلمات عربية أو أحرف ASCII؛ تغيير tracking بين حروف عربية متصلة محظور افتراضيًا.'),
 'typewriter':(['safeTextUnits','rtlMatte'],'conditional','ASCII يمكن بناء prefix له؛ العربية تستخدم كشف النص المشكّل مع تسمية صحيحة، لا ادعاء محرّك typewriter حرفي مطابق.'),
 'write-on':(['strokePath','trimPath'],'requires-authored-strokes','رسم قلم حقيقي فقط عند توفر مسارات ضربات مرتبة؛ outline الخط ليس مسار كتابة.'),
 'scramble':(['scrambleASCII'],'ascii-explicit-copy-permission','محظور على العربية وعلى النص المعتمد؛ يسمح ASCII فقط بتفويض تغيير مؤقت للنص.'),
 'blur':(['track'],'canvas-filter-adapter','تغيير نصف قطر blur فعلي؛ ليس motion blur ولا مبررًا لاستبدال الكشف الطباعي.'),
 'flip':(['samplePerspective'],'requires-verified-3d-adapter','Flip هندسي صحيح يحتاج plane projection/mesh مختبرًا؛ scaleX=cos مجرد تقريب ولا يُعتمد مكافئًا أصليًا.'),
 'match-cut':(['track'],'composition-recipe','تطابق موضع/شكل/معنى بين لقطتين؛ عقد continuity وليس فلترًا مستقلًا.'),
 'object-wipe':(['maskedSprite','track'],'composition-recipe','الساتر والقناع واللقطة التالية طبقات مستقلة مربوطة بهندسة مشتركة.'),
 'camera-transition':(['track','layerState','temporalAverage'],'composition-recipe','حركة كاميرا مدفوعة بعلاقة المشهدين مع محاذاة وطمس زمني عند السرعة.'),
 'keyframes':(['track'],'implemented','قبل/أثناء/بعد، حالات متعددة وhold؛ لا يبدأ الجميع وينتهي الجميع معًا.'),
 'easing':(['cubicBezier','eases','derivative'],'implemented','منحنى قيمة مختلف عن منحنى سرعة؛ قيمة السرعة مشتقة وليست نفس الرسم.'),
 'graph-editor':(['cubicBezier','derivative'],'diagnostic-lab-not-native-ae','مختبر منحنيات قيمة/سرعة قابل للضبط، وليس واجهة Adobe Graph Editor الأصلية.'),
 'hold':(['track'],'implemented','تثبيت حقيقي لا interpolation بطيء؛ له مدة قراءة محددة.'),
 'motion-blur':(['shutterTimes','temporalAverage'],'implemented-temporal-sampling','عينات زمنية داخل فترة الغالق مع متوسط RGBA؛ لا Gaussian ثابتًا. عدد العينات ونموذج اللون موثقان.'),
}
assignment={}
def put(key,names):
 for n in names.split('|'):assignment[n]=key
put('transform-track','Slide In|Scale Up|Spin In|Slide|Push|Pull')
put('anticipation-settle','Pop In|Scale Bounce|Anticipation|Overshoot|Settle')
put('spring','Spring In|Spring Motion|Spring Overshoot|Overshoot & Settle|Elastic')
put('ballistic','Bounce In|Drop In|Bounce')
put('inertia','Inertial Bounce|Drag')
put('damped-oscillation','Wobble|Jiggle|Recoil|Damped Oscillation')
put('seeded-noise','Wiggle|Drift|Float')
put('squash-stretch','Squash & Stretch')
put('secondary','Follow Through|Secondary Motion')
put('scroll','Scroll|Vertical Scroll|Horizontal Scroll|Rolling Credits|Ticker|Marquee|Continuous Scroll')
put('parallax','Parallax Scroll')
put('alpha-matte','Reveal In|Wipe In|Mask Reveal|Slide Reveal|Character Reveal|Word Reveal|Line Reveal|Mask Wipe|Matte Reveal|Clipping Reveal|Split Reveal|Text Build|Wipe Transition|Mask Transition')
put('iris','Circle Reveal|Circular Wipe')
put('path-trim','Stroke Reveal|Line Draw|Trim Paths|Underline Draw|Arrow Draw|Callout Animation')
put('path-follow','Fly In|Path Follow')
put('contour-morph','Shape Morph|Morph Transition')
put('range-stagger','Word-by-Word|Line-by-Line|Character Stagger|Word Stagger|Cascade|Character Rotation|Character Lift|Stagger')
put('baseline-wave','Wave|Ripple|Baseline Wave')
put('tracking','Tracking Reveal|Tracking In|Tracking Out')
put('typewriter','Typewriter')
put('write-on','Write On')
put('scramble','Text Scramble')
put('blur','Blur In')
put('transform-track','Fade In')
put('flip','Flip In')
put('match-cut','Match Cut|Seamless Transition')
put('object-wipe','Object Wipe')
put('camera-transition','Whip Pan|Whip Transition|Push Transition|Zoom Transition|Spin Transition|Parallax Transition')
put('keyframes','Keyframe Animation')
put('easing','Ease In|Ease Out|Ease In Out')
put('graph-editor','Graph Editor|Speed Graph|Value Graph')
put('hold','Hold')
put('motion-blur','Motion Blur')
shown={'Slide In','Pop In','Spring In','Spring Motion','Overshoot & Settle','Bounce','Squash & Stretch','Secondary Motion','Vertical Scroll','Horizontal Scroll','Parallax Scroll','Mask Reveal','Matte Reveal','Split Reveal','Word Stagger','Baseline Wave','Match Cut','Whip Pan','Object Wipe','Line Draw','Trim Paths','Arrow Draw','Path Follow','Shape Morph','Keyframe Animation','Ease In Out','Anticipation','Stagger','Hold','Motion Blur','Value Graph','Speed Graph'}
rows=[]
for fam,(ar,names) in families.items():
 for term in names.split(', '):
  assert term in assignment,term
  key=assignment[term];functions,status,purpose=mechanisms[key]
  rows.append({'id':fam+'/'+re.sub('[^a-z0-9]+','-',term.lower()).strip('-'),'family':fam,'family_ar':ar,'term':term,'canonical_mechanism':key,'status':status,'runtime_functions':functions,'recipe':'reference/recipes/'+key+'.md','arabic_unit':'word/line/full-shaped-surface; connected character transforms blocked by default','purpose_ar':purpose,'demo_coverage':'representative-or-combined' if term in shown else 'catalog-and-lab-or-conditional-only','proof':'tests/core.test.mjs + tests/browser_checks.py; consult research/test-report.json for actual results, not blanket support'} )
(R/'catalog/motions.json').write_text(json.dumps({'version':'1.0.0','entries':rows,'mechanisms':{k:{'functions':v[0],'status':v[1],'purpose_ar':v[2]} for k,v in mechanisms.items()}},ensure_ascii=False,indent=2))
with (R/'catalog/motions.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['family','family_ar','term','mechanism','status','recipe','demo_coverage']);w.writerows([[x[k] for k in ['family','family_ar','term','canonical_mechanism','status','recipe','demo_coverage']] for x in rows])
folder=R/'reference/recipes';folder.mkdir(parents=True,exist_ok=True)
for key,(fn,status,purpose) in mechanisms.items():
 terms=sorted({x['term'] for x in rows if x['canonical_mechanism']==key})
 text=f'# {key}\n\n**الحالة:** `{status}`\n\n{purpose}\n\nالمسميات المرتبطة: '+', '.join(terms)+'\n\n## آلية التنفيذ\n\nالدوال العامة: '+', '.join('`'+x+'`' for x in fn)+'. اقرأ عقودها في `runtime/core.mjs` و`runtime/canvas.mjs`. لا يوجد في هذه الوصفة تكوين مشهد جاهز أو هوية بصرية.\n\n## عقد التوقيت\n\n- Before: حالة واضحة خارج زمن الفعل، لا عنصر ظاهر بالخطأ.\n- Active: مفاتيح أو دالة مستمرة مع easing مختار؛ اجعل المحتوى المؤكد مقروءًا.\n- Settle: يصل العنصر إلى القيمة النهائية دون قفزة، أو يثبت في hold صريح.\n- Secondary: ابدأ التسطير والمؤشر أو الظل في توقيت مستقل إذا خدم المعنى.\n\n## اختبار القبول\n\nاختبر الأزمنة قبل البداية، داخل الحركة، وعند الاستقرار، ثم اطلبها بترتيب مختلف. راجع نهاية المسار/الـ matte وحدود النص والاتصال العربي. لا تعتبر وجود اسم الدالة دليلًا على صلاحية كل فرع؛ راجع القيود والحالة أعلاه ونتيجة الاختبارات.\n\n## رفض الاستخدام السطحي\n\nلا تطبق هذه الحركة على مجموعة كاملة إذا احتاجت عناصرها إلى بناء مستقل. لا تعدّل النص أو الخط المعتمد لتجاوز عيب تقني. لا تدّعِ أن الآلية هي أداة AE الأصلية.\n'
 if key=='spring':text+='\n```js\nconst x = lerp(-80, 0, spring(t - 0.4, springPresets.heavy));\nconst underline = smooth((t - 0.8) / 0.65); // مستقل عن موضع الكلمة\n```\n'
 elif key=='alpha-matte':text+='\n```js\nconst shaped = textSprite("المعنى أولاً", {size: 160, direction: "rtl"});\nconst mask = rtlMatte(shaped, smooth((t - 0.25) / 0.9), {bands: 3, slant: 22, target: reusableSurface});\nctx.drawImage(mask, x, y); // تبقى حروف المصدر متصلة\n```\n'
 elif key=='path-trim':text+='\n```js\nconst path = pathMetrics(cubicPath(a,b,c,d));\nconst progress = smooth((t - 0.65) / 1.2);\nstrokePath(ctx, path, progress, {head:true});\nconst tip = pathPoint(path, progress); // هو نفس رأس الرسم، لا نقطة تخمينية\n```\n'
 elif key=='motion-blur':text+='\n```js\ntemporalAverage(layerCanvas, t, 32, 4, drawMovingLayer, {angle:180});\n// عينات shutter زمنية فعلية. اللون متوسط premultiplied sRGB، وليس ادعاء تطابق جميع مساحات ألوان AE.\n```\n'
 (folder/(key+'.md')).write_text(text)
md=['# قاموس الحركات التنفيذي','',f'{len(rows)} مدخلًا مصنّفًا؛ {len(set(x["term"] for x in rows))} تسمية فريدة؛ {len(mechanisms)} آلية/عقدًا مرجعيًا. ليست هذه أعداد أدوات مستقلة أو ادعاء بدعم كل تقنية على العربية.','', 'الرمز conditional أو requires يعني شرطًا غير قابل للتجاوز. الفيديو القصير يغطي الفئات الثماني، لا كل مدخل منفردًا.','']
for fam,(ar,_) in families.items():
 md.extend(['## '+ar,'','| الاسم | الآلية | الحالة |','|---|---|---|'])
 for x in rows:
  if x['family']==fam:md.append(f'| {x["term"]} | [{x["canonical_mechanism"]}](../{x["recipe"]}) | {x["status"]} |')
 md.append('')
(R/'catalog/README.md').write_text('\n'.join(md))
print('CATALOG',len(rows),'entries',len(set(x['term'] for x in rows)),'unique labels',len(mechanisms),'canonical mechanisms')
