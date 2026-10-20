/**
 * runtime/spatial.mjs — additive true-3D layer engine for deterministic 2D-canvas compositing (v2.2).
 * Frozen modules (core/canvas) are untouched; this file is the 3D upgrade path:
 * real perspective camera, planar-quad rendering via exact affine triangles, painter depth sort,
 * Lambert-lite shading, orbit/dolly keyframe helpers. No WebGL, no ray tracing, no AE-C4D claim —
 * every behavior is a documented equivalence (see catalog/dictionaries/spatial-3d.json).
 * Pure functions of (state, t); safe for seek(t) determinism.
 */

const DEG = Math.PI / 180;
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const sstep = (x) => { x = clamp(x, 0, 1); return x * x * (3 - 2 * x); };

/** Camera state: position, yaw around Y (screen-right axis), pitch around X, roll around Z. All degrees. */
export function makeCamera({ width = 1080, height = 1920, focal = 1750, near = 0.001, pos = [0, 0, 0], yawDeg = 0, pitchDeg = 0, rollDeg = 0 } = {}) {
  if (!(focal > 0) || !(near >= 0)) throw new Error('spatial: focal must be >0 and near>=0');
  return { width, height, focal, near, pos: pos.slice(), yawDeg, pitchDeg, rollDeg };
}

/** Replace camera pose immutably (returns a new camera). */
export function setCamera(cam, { pos, yawDeg, pitchDeg, rollDeg } = {}) {
  return makeCamera({
    width: cam.width, height: cam.height, focal: cam.focal, near: cam.near,
    pos: pos ?? cam.pos,
    yawDeg: yawDeg ?? cam.yawDeg, pitchDeg: pitchDeg ?? cam.pitchDeg, rollDeg: rollDeg ?? cam.rollDeg,
  });
}

export function worldToCam(cam, p) {
  const yaw = -cam.yawDeg * DEG, pitch = -cam.pitchDeg * DEG, roll = -cam.rollDeg * DEG;
  let x = p[0] - cam.pos[0], y = p[1] - cam.pos[1], z = p[2] - cam.pos[2];
  // yaw (Y-axis)
  let cy = Math.cos(yaw), sy = Math.sin(yaw);
  let x1 = x * cy + z * sy, z1 = -x * sy + z * cy;
  // pitch (X-axis)
  let cp = Math.cos(pitch), sp = Math.sin(pitch);
  let y2 = y * cp - z1 * sp, z2 = y * sp + z1 * cp;
  // roll (Z-axis)
  let cr = Math.cos(roll), sr = Math.sin(roll);
  let x3 = x1 * cr - y2 * sr, y3 = x1 * sr + y2 * cr;
  return [x3, y3, z2];
}

/** Project a world point. visible=false when behind near plane. Screen y grows downward: world +y is up. */
export function projectPoint(cam, p) {
  const [x, y, z] = worldToCam(cam, p);
  if (z <= cam.near) return { x: 0, y: 0, scale: 0, depth: z, visible: false };
  const s = cam.focal / z;
  return { x: cam.width / 2 + x * s, y: cam.height / 2 - y * s, scale: s, depth: z, visible: true };
}

/** Project a planar quad (4 world points, CCW in object space). offscreen when fully outside frame. */
export function projectQuad(cam, pts) {
  const proj = pts.map((p) => projectPoint(cam, p));
  const anyBehind = proj.some((q) => !q.visible);
  if (anyBehind) {
    // clip-free policy: refuse partial quads (they shear wildly); caller must subdivide or move camera.
    return { points: null, avgDepth: NaN, visible: false, reason: 'vertex-behind-camera: subdivide the quad or raise near/focal' };
  }
  const xs = proj.map(q => q.x), ys = proj.map(q => q.y);
  const offscreen = Math.max(...xs) < 0 || Math.min(...xs) > cam.width || Math.max(...ys) < 0 || Math.min(...ys) > cam.height;
  const avgDepth = proj.reduce((a, q) => a + q.depth, 0) / 4;
  return { points: proj.map(q => [q.x, q.y]), avgDepth, visible: true, offscreen };
}

/** Painter's algorithm: far first, stable on ties (keeps seek determinism). */
export function sortPainterly(quads) {
  return quads.map((q, i) => [q, i]).sort((a, b) => (b[0].avgDepth - a[0].avgDepth) || (a[1] - b[1])).map(x => x[0]);
}

export function faceNormal(pts) {
  const u = [pts[1][0] - pts[0][0], pts[1][1] - pts[0][1], pts[1][2] - pts[0][2]];
  const v = [pts[3][0] - pts[0][0], pts[3][1] - pts[0][1], pts[3][2] - pts[0][2]];
  const n = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]];
  const L = Math.hypot(n[0], n[1], n[2]) || 1;
  return [n[0] / L, n[1] / L, n[2] / L];
}

/** Lambert-lite with fixed azimuth key light. Returns 0..1.4 brightness multiplier. */
export function shade(normal, { lightAzimuthDeg = 35, lightElevationDeg = 28, ambient = 0.55 } = {}) {
  const az = lightAzimuthDeg * DEG, el = lightElevationDeg * DEG;
  const L = [Math.cos(el) * Math.sin(az), Math.sin(el), Math.cos(el) * Math.cos(az)];
  const d = Math.abs(normal[0] * L[0] + normal[1] * L[1] + normal[2] * L[2]);
  return clamp(ambient + (1.4 - ambient) * d, 0, 1.4);
}

/** Axis-aligned box (slab) centered at c with sizes s=[w,h,d]; 6 quads facing outward + per-face normals. */
export function slab({ size = [100, 100, 20], center = [0, 0, 0] } = {}) {
  const [w, h, d] = size.map(v => v / 2);
  const [cx, cy, cz] = center;
  const P = (x, y, z) => [cx + x, cy + y, cz + z];
  const faces = [
    { name: 'front', pts: [P(-w, -h, d), P(w, -h, d), P(w, h, d), P(-w, h, d)] },
    { name: 'back', pts: [P(w, -h, -d), P(-w, -h, -d), P(-w, h, -d), P(w, h, -d)] },
    { name: 'right', pts: [P(w, -h, d), P(w, -h, -d), P(w, h, -d), P(w, h, d)] },
    { name: 'left', pts: [P(-w, -h, -d), P(-w, -h, d), P(-w, h, d), P(-w, h, -d)] },
    { name: 'top', pts: [P(-w, h, d), P(w, h, d), P(w, h, -d), P(-w, h, -d)] },
    { name: 'bottom', pts: [P(-w, -h, -d), P(w, -h, -d), P(w, -h, d), P(-w, -h, d)] },
  ];
  return faces.map(f => ({ ...f, normal: faceNormal(f.pts) }));
}

/** Depth parallax ratio vs a reference plane — camera.json rule in code form. */
export function parallaxRatio(cam, z, zRef) {
  const k = (zz) => cam.focal / (cam.focal - zz);
  return k(z) / k(zRef);
}

/** Deterministic camera keyframe: yaw/pitch/dolly between states with smoothstep (or provided ease). */
export function orbitKey(t, { t0 = 0, t1 = 1, center = [0, 0, 0], radius0 = 900, radius1 = 700, yaw0Deg = -18, yaw1Deg = 6, pitch0Deg = 8, pitch1Deg = 3, ease = sstep } = {}) {
  const u = ease(clamp((t - t0) / (t1 - t0 || 1), 0, 1));
  const yaw = (yaw0Deg + (yaw1Deg - yaw0Deg) * u), pitch = (pitch0Deg + (pitch1Deg - pitch0Deg) * u);
  const r = radius0 + (radius1 - radius0) * u;
  const a = yaw * DEG;
  return setCamera(makeCamera({}), {
    pos: [center[0] + Math.sin(a) * r, center[1] + (pitch * DEG) * 400, center[2] + Math.cos(a) * r],
    yawDeg: -yaw, pitchDeg: -pitch,
  });
}

/** Compose: every face of an object under a per-object transform (translate/rot/scale), projected + shaded + sorted. */
export function renderPlan(cam, { pos = [0, 0, 0], rotYDeg = 0, rotXDeg = 0, size = [100, 100, 20] }, { light, tint } = {}) {
  const out = [];
  const ry = rotYDeg * DEG, rx = rotXDeg * DEG;
  const xf = (p) => {
    let [x, y, z] = [p[0] * size[0] / 100, p[1] * size[1] / 100, p[2] * size[2] / 100];
    let c = Math.cos(ry), s = Math.sin(ry); [x, z] = [x * c + z * s, -x * s + z * c];
    c = Math.cos(rx); s = Math.sin(rx); [y, z] = [y * c - z * s, y * s + z * c];
    return [x + pos[0], y + pos[1], z + pos[2]];
  };
  for (const f of slab({ size: [100, 100, 100], center: [0, 0, 0] })) {
    const pts = f.pts.map(xf);
    const q = projectQuad(cam, pts);
    if (!q.visible || q.offscreen) continue;
    const n = f.normal.map((v) => v); // transform normal like direction
    let [nx, ny, nz] = n; let c = Math.cos(ry), s = Math.sin(ry); [nx, nz] = [nx * c + nz * s, -nx * s + nz * c];
    c = Math.cos(rx); s = Math.sin(rx); [ny, nz] = [ny * c - nz * s, ny * s + nz * c];
    out.push({ ...q, face: f.name, shade: shade([nx, ny, nz], light || {}), tint });
  }
  return sortPainterly(out);
}

/**
 * Exact planar texture warp for canvas: draw img into any convex quad by two clipped affine triangles.
 * ctx2d required (browser); pure geometry testable in node via triTransforms().
 */
export function triTransforms(srcSize, quadScreen, uv = [[0, 0], [1, 0], [1, 1], [0, 1]]) {
  const solve = (triSrc, triDst) => {
    const [a, b, c, d, e, f, g, h] = [
      triSrc[1][0] - triSrc[0][0], triSrc[2][0] - triSrc[0][0],
      triSrc[1][1] - triSrc[0][1], triSrc[2][1] - triSrc[0][1],
      triDst[1][0] - triDst[0][0], triDst[2][0] - triDst[0][0],
      triDst[1][1] - triDst[0][1], triDst[2][1] - triDst[0][1],
    ];
    const det = a * f - b * e;
    if (Math.abs(det) < 1e-9) throw new Error('spatial: degenerate triangle');
    const m11 = (c * d - a * f) ? (e * b - d * a) / (a * f - b * e) : 0; // computed below explicitly
    void m11;
    const ia = f / det, ib = -b / det, ic = -e / det, id = a / det;
    const sx = triSrc[0][0], sy = triSrc[0][1];
    return {
      a: ia * d + ib * g, b: ia * e + ib * h,
      c: ic * d + id * g, d: ic * e + id * h,
      e: triDst[0][0] - (sx * (ia * d + ib * g) + sy * (ic * d + id * g)),
      f: triDst[0][1] - (sx * (ia * e + ib * h) + sy * (ic * e + id * h)),
    };
  };
  const S = srcSize, P = quadScreen;
  const t1 = solve([[0, 0], [S[0], 0], [0, S[1]]], [P[0], P[1], P[3]]);
  const t2 = solve([[0, 0], [S[0], S[1]], [S[0], 0]], [P[0], P[2], P[1]]);
  void uv;
  return [t1, t2];
}

export function drawPlanar(ctx, img, quadScreen) {
  const S = [img.naturalWidth || img.width, img.naturalHeight || img.height];
  const [t1, t2] = triTransforms(S, quadScreen);
  const clip = (tri) => { ctx.save(); ctx.beginPath(); ctx.moveTo(tri[0], tri[1]); ctx.lineTo(tri[2], tri[3]); ctx.lineTo(tri[4], tri[5]); ctx.closePath(); ctx.clip(); };
  clip([quadScreen[0][0], quadScreen[0][1], quadScreen[1][0], quadScreen[1][1], quadScreen[3][0], quadScreen[3][1]]);
  ctx.setTransform(t1.a, t1.b, t1.c, t1.d, t1.e, t1.f); ctx.drawImage(img, 0, 0); ctx.restore();
  clip([quadScreen[0][0], quadScreen[0][1], quadScreen[2][0], quadScreen[2][1], quadScreen[1][0], quadScreen[1][1]]);
  ctx.setTransform(t2.a, t2.b, t2.c, t2.d, t2.e, t2.f); ctx.drawImage(img, 0, 0); ctx.restore();
}
