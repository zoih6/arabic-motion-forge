# Scene DNA + Shot DNA — AI Film Studio v1.2

## الهدف
فصل الثوابت التي يجب أن تستمر عبر المشهد عن المتغيرات الخاصة بكل لقطة.

## Scene DNA
يمثل الهوية المستقرة للمشهد:
- `scene_id`
- world/location
- time/season
- lighting regime
- palette/material language
- character IDs + wardrobe
- prop IDs
- visual grammar
- text/graphic language
- audio atmosphere
- continuity anchors

## Shot DNA
يمثل ما يتغير داخل اللقطة:
- `shot_id`
- narrative beat
- framing/shot size
- camera position
- dominant camera movement
- dominant subject action
- expression/body language
- start state
- end state
- duration
- local effects
- local dialogue/audio

## Inheritance Rule
كل Shot يرث Scene DNA تلقائيًا ما لم توجد Override صريحة.

```text
PROJECT DNA
   ↓
SCENE DNA
   ↓ inherited
SHOT DNA
   ↓ compiled
IMAGE / VIDEO / AUDIO PROMPT
```

## Override Rule
لا تغيّر الثوابت بصمت. أي تغيير في الهوية أو العالم أو الضوء أو الملابس أو props يُسجل كـ `OVERRIDE` ويؤثر على اللقطات اللاحقة فقط بعد اعتماد واضح.

## Variable Isolation
عند التكرار، غيّر متغيرًا رئيسيًا واحدًا في كل محاولة متى أمكن:
- camera
- performance
- composition
- lighting
- environment
- prompt/model strategy

## Continuity Anchors
لكل مشهد حد أدنى من 3 anchors قابلة للفحص، مثل:
- identity anchor
- wardrobe/prop anchor
- lighting/composition anchor

## Prompt Compiler Input
لا يُكتب البرومبت من الصفر لكل لقطة. يُجمع من:
`Scene DNA + Shot DNA + Reference Roles + Model Syntax + Output Constraints`.
