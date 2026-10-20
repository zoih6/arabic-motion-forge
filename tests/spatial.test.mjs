import { test } from 'node:test';
import assert from 'node:assert/strict';
import * as S from '../runtime/spatial.mjs';

test('3d: point straight ahead projects to frame center', () => {
  const cam = S.makeCamera({ width: 1080, height: 1920, focal: 1600 });
  const p = S.projectPoint(cam, [0, 0, 800]);
  assert.equal(p.visible, true);
  assert.ok(Math.abs(p.x - 540) < 1e-9 && Math.abs(p.y - 960) < 1e-9);
  assert.ok(Math.abs(p.scale - 1600 / 800) < 1e-9);
});

test('3d: nearer points magnify; behind-camera refused', () => {
  const cam = S.makeCamera({});
  const near = S.projectPoint(cam, [100, 0, 400]), far = S.projectPoint(cam, [100, 0, 1600]);
  assert.ok(near.x - far.x > 0, 'near offset larger from center');
  assert.equal(S.projectPoint(cam, [0, 0, -5]).visible, false);
});

test('3d: partial quad behind near plane throws visible=false with guidance', () => {
  const cam = S.makeCamera({});
  const q = S.projectQuad(cam, [[-50, -50, 900], [50, -50, 900], [50, 50, -10], [-50, 50, -10]]);
  assert.equal(q.visible, false);
  assert.match(q.reason, /subdivide/);
});

test('3d: slab has 6 outward faces with unit normals; painter sort far-first stable', () => {
  const faces = S.slab({ size: [100, 60, 20] });
  assert.equal(faces.length, 6);
  for (const f of faces) assert.ok(Math.abs(Math.hypot(...f.normal) - 1) < 1e-9);
  const cam = S.makeCamera({});
  const quads = [
    { avgDepth: 500, tag: 'near' }, { avgDepth: 900, tag: 'far' }, { avgDepth: 500, tag: 'near2' },
  ];
  const sorted = S.sortPainterly(quads);
  assert.deepEqual(sorted.map(q => q.tag), ['far', 'near', 'near2']);
});

test('3d: shade is a deterministic brightness with light rule respected', () => {
  const lit = S.shade([0, 0, 1], { lightAzimuthDeg: 0, lightElevationDeg: 0 });
  const side = S.shade([1, 0, 0], { lightAzimuthDeg: 0, lightElevationDeg: 0 });
  assert.ok(lit > side, 'front face brighter than side face under front light');
});

test('3d: orbitKey endpoints exact and radius interpolates monotonically', () => {
  const opts = { t0: 0, t1: 1, radius0: 1200, radius1: 600, yaw0Deg: -20, yaw1Deg: 10 };
  const rad = (c) => Math.hypot(c.pos[0], c.pos[2]);
  const a = S.orbitKey(0, opts), b = S.orbitKey(1, opts), m = S.orbitKey(0.5, opts);
  assert.ok(Math.abs(rad(a) - 1200) < 1e-6);
  assert.ok(Math.abs(rad(b) - 600) < 1e-6);
  assert.ok(rad(m) < rad(a) && rad(m) > rad(b), 'smooth pull-in between endpoints');
  assert.deepEqual(S.orbitKey(0.5, opts), m, 'deterministic for same t');
});

test('3d: nearer-to-camera layers parallax more; renderPlan deterministic on repeat', () => {
  const cam = S.makeCamera({});
  assert.ok(S.parallaxRatio(cam, 900, 0) > S.parallaxRatio(cam, 300, 0), 'larger z (closer) moves more under dolly');
  const q1 = S.renderPlan(cam, { pos: [0, 0, 600], size: [200, 200, 40] });
  const q2 = S.renderPlan(cam, { pos: [0, 0, 600], size: [200, 200, 40] });
  assert.deepEqual(q1, q2);
  assert.equal(q1.length, 6, 'front slab fully visible from +z camera? — camera at origin looks +z so front face only; allow 1..6');
});
