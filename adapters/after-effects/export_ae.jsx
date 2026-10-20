// Arabic Motion Forge -> After Effects bridge TEMPLATE (ExtendScript ES3).
// Consumes a sidecar data object injected by tools/export_ae.py (window.AMF_AE_PLAN),
// building comps, null-parented layers and keyframes with eased interpolation.
// Honest scope: geometry+timing+easing transfer; expressions/footage paths re-link in AE.
(function amfBuild() {
  var plan = window.AMF_AE_PLAN || (app && app.AMF_AE_PLAN);
  if (!plan) { alert('AMF_AE_PLAN missing — run tools/export_ae.py to inject the plan JSON.'); return; }
  app.beginUndoGroup('AMF import');
  var comp = app.project.items.addComp(plan.name || 'AMF film', plan.width, plan.height, 1, plan.duration);
  for (var s = 0; s < plan.scenes.length; s++) {
    var scene = plan.scenes[s];
    for (var l = 0; l < scene.layers.length; l++) {
      var lay = scene.layers[l];
      var layer;
      if (lay.kind === 'text') {
        layer = comp.layers.addText(lay.text || '');
      } else {
        var solid = comp.layers.addSolid([0.5, 0.5, 0.5], lay.id || ('L' + l), plan.width, plan.height, 1);
        layer = solid;
      }
      if (lay.in !== undefined) layer.inPoint = lay.in;
      if (lay.out !== undefined) layer.outPoint = Math.min(lay.out, plan.duration);
      var tracks = lay.tracks || {};
      var t, v, i, kf;
      function setProp(prop, keyframes) {
        for (var k = 0; k < keyframes.length; k++) {
          var e = keyframes[k];
          var setOpts = (e.ease === 'hold') ? ExtendEnum.EaseType.HOLDKEYFRAME
            : (e.ease === 'in') ? ExtendEnum.EaseType.TIME_EASE_IN | ExtendEnum.EaseType.VALUE_EASE_IN
            : (e.ease === 'out') ? ExtendEnum.EaseType.TIME_EASE_OUT | ExtendEnum.EaseType.VALUE_EASE_OUT
            : (e.ease === 'both' || e.ease === 'inOut') ? (ExtendEnum.EaseType.TIME_EASE_IN | ExtendEnum.EaseType.VALUE_EASE_IN | ExtendEnum.EaseType.TIME_EASE_OUT | ExtendEnum.EaseType.VALUE_EASE_OUT)
            : 0;
          prop.setValueAtTime(e.t, e.v);
          if (setOpts) {
            try { prop.setInterpolationTypeAtKey(prop.nearestKeysToTime(e.t)[0], ExtendEnum.InterpolationType.BEZIERINTERP, setOpts); } catch (err) {}
          }
        }
      }
      if (tracks.position) setProp(layer.property('Position').property(1), tracks.position);
      if (tracks.opacity) setProp(layer.property('Opacity'), tracks.opacity.map(function (e) { return { t: e.t, v: e.v, ease: e.ease }; }));
      if (tracks.scale) setProp(layer.property('Scale'), tracks.scale);
      if (tracks.rotation) setProp(layer.property('Rotation'), tracks.rotation);
    }
  }
  comp.workAreaStart = 0; comp.workAreaDuration = plan.duration;
  app.endUndoGroup();
  alert('AMF: ' + plan.scenes.length + ' scenes / layers built. Re-link footage and Arabic glyph source files, then RAM preview.');
})();
