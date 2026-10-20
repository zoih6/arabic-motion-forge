# قاموس الحركات التنفيذي

104 مدخلًا مصنّفًا؛ 103 تسمية فريدة؛ 33 آلية/عقدًا مرجعيًا. ليست هذه أعداد أدوات مستقلة أو ادعاء بدعم كل تقنية على العربية.

الرمز conditional أو requires يعني شرطًا غير قابل للتجاوز. الفيديو القصير يغطي الفئات الثماني، لا كل مدخل منفردًا.

## الدخول

| الاسم | الآلية | الحالة |
|---|---|---|
| Slide In | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Pop In | [anticipation-settle](../reference/recipes/anticipation-settle.md) | implemented |
| Scale Up | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Scale Bounce | [anticipation-settle](../reference/recipes/anticipation-settle.md) | implemented |
| Spring In | [spring](../reference/recipes/spring.md) | implemented |
| Bounce In | [ballistic](../reference/recipes/ballistic.md) | implemented |
| Drop In | [ballistic](../reference/recipes/ballistic.md) | implemented |
| Fly In | [path-follow](../reference/recipes/path-follow.md) | implemented |
| Flip In | [flip](../reference/recipes/flip.md) | requires-verified-3d-adapter |
| Spin In | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Blur In | [blur](../reference/recipes/blur.md) | canvas-filter-adapter |
| Fade In | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Reveal In | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Wipe In | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Mask Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |

## النابض والفيزياء

| الاسم | الآلية | الحالة |
|---|---|---|
| Spring Motion | [spring](../reference/recipes/spring.md) | implemented |
| Spring Overshoot | [spring](../reference/recipes/spring.md) | implemented |
| Overshoot & Settle | [spring](../reference/recipes/spring.md) | implemented |
| Bounce | [ballistic](../reference/recipes/ballistic.md) | implemented |
| Elastic | [spring](../reference/recipes/spring.md) | implemented |
| Inertial Bounce | [inertia](../reference/recipes/inertia.md) | implemented |
| Wobble | [damped-oscillation](../reference/recipes/damped-oscillation.md) | implemented |
| Wiggle | [seeded-noise](../reference/recipes/seeded-noise.md) | implemented |
| Jiggle | [damped-oscillation](../reference/recipes/damped-oscillation.md) | implemented |
| Recoil | [damped-oscillation](../reference/recipes/damped-oscillation.md) | implemented |
| Squash & Stretch | [squash-stretch](../reference/recipes/squash-stretch.md) | implemented |
| Follow Through | [secondary](../reference/recipes/secondary.md) | implemented |
| Secondary Motion | [secondary](../reference/recipes/secondary.md) | implemented |
| Damped Oscillation | [damped-oscillation](../reference/recipes/damped-oscillation.md) | implemented |

## التمرير والانزلاق

| الاسم | الآلية | الحالة |
|---|---|---|
| Slide | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Scroll | [scroll](../reference/recipes/scroll.md) | implemented |
| Vertical Scroll | [scroll](../reference/recipes/scroll.md) | implemented |
| Horizontal Scroll | [scroll](../reference/recipes/scroll.md) | implemented |
| Rolling Credits | [scroll](../reference/recipes/scroll.md) | implemented |
| Ticker | [scroll](../reference/recipes/scroll.md) | implemented |
| Marquee | [scroll](../reference/recipes/scroll.md) | implemented |
| Push | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Pull | [transform-track](../reference/recipes/transform-track.md) | implemented |
| Drag | [inertia](../reference/recipes/inertia.md) | implemented |
| Slide Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Parallax Scroll | [parallax](../reference/recipes/parallax.md) | implemented-2.5d |
| Continuous Scroll | [scroll](../reference/recipes/scroll.md) | implemented |

## كشف النصوص

| الاسم | الآلية | الحالة |
|---|---|---|
| Typewriter | [typewriter](../reference/recipes/typewriter.md) | conditional |
| Write On | [write-on](../reference/recipes/write-on.md) | requires-authored-strokes |
| Character Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Word Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Line Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Tracking Reveal | [tracking](../reference/recipes/tracking.md) | conditional |
| Mask Wipe | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Matte Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Stroke Reveal | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Clipping Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Split Reveal | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Word-by-Word | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Line-by-Line | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Text Build | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |

## الطباعة الحركية

| الاسم | الآلية | الحالة |
|---|---|---|
| Character Stagger | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Word Stagger | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Cascade | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Wave | [baseline-wave](../reference/recipes/baseline-wave.md) | implemented-with-arabic-guard |
| Ripple | [baseline-wave](../reference/recipes/baseline-wave.md) | implemented-with-arabic-guard |
| Float | [seeded-noise](../reference/recipes/seeded-noise.md) | implemented |
| Drift | [seeded-noise](../reference/recipes/seeded-noise.md) | implemented |
| Tracking In | [tracking](../reference/recipes/tracking.md) | conditional |
| Tracking Out | [tracking](../reference/recipes/tracking.md) | conditional |
| Character Rotation | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Character Lift | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Baseline Wave | [baseline-wave](../reference/recipes/baseline-wave.md) | implemented-with-arabic-guard |
| Text Scramble | [scramble](../reference/recipes/scramble.md) | ascii-explicit-copy-permission |

## الانتقالات

| الاسم | الآلية | الحالة |
|---|---|---|
| Match Cut | [match-cut](../reference/recipes/match-cut.md) | composition-recipe |
| Whip Pan | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Whip Transition | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Push Transition | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Wipe Transition | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Zoom Transition | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Spin Transition | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Morph Transition | [contour-morph](../reference/recipes/contour-morph.md) | implemented-with-correspondence |
| Mask Transition | [alpha-matte](../reference/recipes/alpha-matte.md) | implemented |
| Parallax Transition | [camera-transition](../reference/recipes/camera-transition.md) | composition-recipe |
| Seamless Transition | [match-cut](../reference/recipes/match-cut.md) | composition-recipe |
| Object Wipe | [object-wipe](../reference/recipes/object-wipe.md) | composition-recipe |

## الخطوط والأشكال

| الاسم | الآلية | الحالة |
|---|---|---|
| Line Draw | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Trim Paths | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Stroke Reveal | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Underline Draw | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Arrow Draw | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Path Follow | [path-follow](../reference/recipes/path-follow.md) | implemented |
| Callout Animation | [path-trim](../reference/recipes/path-trim.md) | implemented |
| Circle Reveal | [iris](../reference/recipes/iris.md) | implemented |
| Circular Wipe | [iris](../reference/recipes/iris.md) | implemented |
| Shape Morph | [contour-morph](../reference/recipes/contour-morph.md) | implemented-with-correspondence |

## التوقيت والحركة

| الاسم | الآلية | الحالة |
|---|---|---|
| Keyframe Animation | [keyframes](../reference/recipes/keyframes.md) | implemented |
| Ease In | [easing](../reference/recipes/easing.md) | implemented |
| Ease Out | [easing](../reference/recipes/easing.md) | implemented |
| Ease In Out | [easing](../reference/recipes/easing.md) | implemented |
| Graph Editor | [graph-editor](../reference/recipes/graph-editor.md) | diagnostic-lab-not-native-ae |
| Speed Graph | [graph-editor](../reference/recipes/graph-editor.md) | diagnostic-lab-not-native-ae |
| Value Graph | [graph-editor](../reference/recipes/graph-editor.md) | diagnostic-lab-not-native-ae |
| Anticipation | [anticipation-settle](../reference/recipes/anticipation-settle.md) | implemented |
| Overshoot | [anticipation-settle](../reference/recipes/anticipation-settle.md) | implemented |
| Settle | [anticipation-settle](../reference/recipes/anticipation-settle.md) | implemented |
| Stagger | [range-stagger](../reference/recipes/range-stagger.md) | implemented-with-arabic-guard |
| Hold | [hold](../reference/recipes/hold.md) | implemented |
| Motion Blur | [motion-blur](../reference/recipes/motion-blur.md) | implemented-temporal-sampling |

## Dictionaries (v2)

| File | Role |
|---|---|
| `dictionaries/direction-axes.json` | Inspiration-engine fuel: 8 axes × 5–6 options + palette sets + anti-patterns |
| `dictionaries/easings.json` | Every curve by implementation status (implemented / recipe / adapter / diagnostic) with use/avoid rules |
| `dictionaries/camera.json` | Depth-projection model, camera-move legality, verification list |
| `dictionaries/continuity.json` | 10 machine-checkable continuity rules QA enforces by id |
| `dictionaries/styles.json` | Reference study notes (Vox, Kurzgesagt, Ordinary Folk, Carbon…) with never-copy lines |
| `compatibility-baseline.json` | v1 public surface (371 paths, runtime exports+hashes, kit fields) enforced by `tools/compat_check.py` |
