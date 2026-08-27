/* ===========================================================
   NaRu — background metamorphosis
   A low-poly wireframe that evolves across the whole site:
   larva -> chrysalis -> emerging -> butterfly.

   Every stage is described by one boundary-radius function
   R(angle). A fixed mesh of concentric rings is mapped into
   whichever stage you are in, keeping each node's angle and
   its normalised radius — so the mesh morphs coherently
   instead of scrambling between shapes.

   Each page owns one fifth of the journey (body[data-stage]);
   scrolling advances within it, and the motion lags the
   scroll so the background drifts behind you.
   =========================================================== */
(function () {
  'use strict';

  var cvs = document.getElementById('bgfx');
  if (!cvs || !cvs.getContext) return;
  var ctx = cvs.getContext('2d');

  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  var W = 0, H = 0, DPR = 1;
  var target = 0, smooth = 0;
  var t0 = performance.now(), t = 0;
  var running = true;

  function clamp(v, a, b) { return v < a ? a : v > b ? b : v; }
  function seg(v, a, b) { return clamp((v - a) / (b - a), 0, 1); }
  function lerp(a, b, k) { return a + (b - a) * k; }
  function smoothstep(x) { return x * x * (3 - 2 * x); }

  /* =========================================================
     Stage silhouettes — R(angle), angle 0 = straight up
     ========================================================= */

  /* Classic butterfly curve: four lobes at the diagonals,
     pinched at the vertical and horizontal axes. */
  function R_butterfly(a) {
    var r = Math.exp(Math.cos(a)) - 2 * Math.cos(4 * a)
          + Math.pow(Math.sin((2 * a - Math.PI) / 24), 5);
    return r / 3.7;
  }

  /* Pod: tall, narrow, tapered toward the bottom. */
  function R_chrysalis(a) {
    var wx = 0.30, wy = 0.86;
    var s = Math.sin(a) / wx, c = Math.cos(a) / wy;
    var r = 1 / Math.sqrt(s * s + c * c);
    var down = Math.max(0, -Math.cos(a));
    return r * (1 - 0.34 * down * down);
  }

  /* Larva: a curled, segmented caterpillar — fat body with a
     bite taken out of one side so it reads as a comma, not a ball. */
  function angDist(a, b) {
    var d = Math.abs(((a - b + Math.PI) % (Math.PI * 2) + Math.PI * 2) % (Math.PI * 2) - Math.PI);
    return d;
  }
  function R_larva(a) {
    var wx = 0.58, wy = 0.50;
    var s = Math.sin(a) / wx, c = Math.cos(a) / wy;
    var r = 1 / Math.sqrt(s * s + c * c);
    var curl = 1 - 0.46 * Math.exp(-Math.pow(angDist(a, -Math.PI / 2) / 0.62, 2));
    var segs = 1 + 0.070 * Math.cos(9 * a);
    return r * curl * segs * (1 + 0.10 * Math.cos(a));
  }

  /* Emerging: the pod with the first push of wings at the diagonals. */
  function R_emerging(a) {
    var base = lerp(R_chrysalis(a), R_butterfly(a), 0.30);
    var up = Math.max(0, Math.sin(Math.abs(a) < Math.PI ? a : a));
    var bump = 0.16 * Math.exp(-Math.pow((Math.abs(Math.sin(a)) - 0.72) / 0.30, 2));
    return base + bump * (0.5 + 0.5 * Math.cos(a));
  }

  var SHAPES = [R_larva, R_chrysalis, R_emerging, R_butterfly];

  /* =========================================================
     Mesh: concentric rings in (angle, normalised radius) space
     ========================================================= */
  var RINGS = [
    { rho: 1.00, n: 40 },
    { rho: 0.74, n: 28 },
    { rho: 0.47, n: 20 },
    { rho: 0.22, n: 12 }
  ];
  var NODES = [];   // {a, rho, ring}
  var EDGES = [];   // [i, j]
  var CENTER;

  (function buildMesh() {
    var offset = [];
    for (var r = 0; r < RINGS.length; r++) {
      var ring = RINGS[r];
      offset[r] = NODES.length;
      for (var i = 0; i < ring.n; i++) {
        NODES.push({
          a: (i / ring.n) * Math.PI * 2 + (r % 2 ? Math.PI / ring.n : 0),
          rho: ring.rho,
          ring: r
        });
      }
    }
    CENTER = NODES.length;
    NODES.push({ a: 0, rho: 0, ring: RINGS.length });

    for (var r2 = 0; r2 < RINGS.length; r2++) {
      var n = RINGS[r2].n, base = offset[r2];
      for (var i2 = 0; i2 < n; i2++) {
        EDGES.push([base + i2, base + (i2 + 1) % n]);      // around the ring
        if (r2 + 1 < RINGS.length) {                        // spokes inward
          var nn = RINGS[r2 + 1].n, bb = offset[r2 + 1];
          var j = Math.round(i2 * nn / n) % nn;
          EDGES.push([base + i2, bb + j]);
          if (i2 % 2 === 0) EDGES.push([base + i2, bb + (j + 1) % nn]);
        } else {
          if (i2 % 2 === 0) EDGES.push([base + i2, CENTER]);
        }
      }
    }
  })();

  /* ---------- pre-rendered sprites ----------
     Radial gradients are expensive and were previously rebuilt for every
     glowing node on every frame. Bake them once and blit instead. */
  function makeSprite(px, rgb) {
    var c = document.createElement('canvas');
    c.width = c.height = px;
    var g = c.getContext('2d');
    var rg = g.createRadialGradient(px / 2, px / 2, 0, px / 2, px / 2, px / 2);
    rg.addColorStop(0, 'rgba(' + rgb + ',1)');
    rg.addColorStop(0.5, 'rgba(' + rgb + ',0.28)');
    rg.addColorStop(1, 'rgba(' + rgb + ',0)');
    g.fillStyle = rg; g.fillRect(0, 0, px, px);
    return c;
  }
  var SPR_BLOOM_COOL = makeSprite(192, '139,110,155');
  var SPR_BLOOM_WARM = makeSprite(192, '201,123,90');
  var SPR_NODE       = makeSprite(48,  '237,231,242');

  /* Resolve every node for a given morph position. */
  var PTS = new Float32Array(NODES.length * 2);
  var MAXR = 0;
  function solve(stageF, size, flap) {
    var i = Math.min(SHAPES.length - 2, Math.floor(stageF));
    var k = smoothstep(clamp(stageF - i, 0, 1));
    var A = SHAPES[i], B = SHAPES[i + 1];
    var m = 0;
    for (var n = 0; n < NODES.length; n++) {
      var nd = NODES[n];
      var R = lerp(A(nd.a), B(nd.a), k) * nd.rho * size;
      var px = Math.sin(nd.a) * R * flap, py = -Math.cos(nd.a) * R;
      PTS[n * 2] = px; PTS[n * 2 + 1] = py;
      var d2 = px * px + py * py;          /* squared — no sqrt in the loop */
      if (d2 > m) m = d2;
    }
    MAXR = Math.sqrt(m);
  }

  /* =========================================================
     Sizing
     ========================================================= */
  var motes = [];
  function seedMotes() {
    motes = [];
    var n = Math.round(clamp(W / 30, 18, 54));
    for (var i = 0; i < n; i++) {
      motes.push({
        x: Math.random() * W, y: Math.random() * H,
        r: 0.5 + Math.random() * 1.5,
        sp: 0.10 + Math.random() * 0.40,
        ph: Math.random() * Math.PI * 2,
        am: 10 + Math.random() * 40
      });
    }
  }
  function resize() {
    DPR = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth; H = window.innerHeight;
    cvs.width = Math.floor(W * DPR); cvs.height = Math.floor(H * DPR);
    cvs.style.width = W + 'px'; cvs.style.height = H + 'px';
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    seedMotes();
  }

  /* The whole metamorphosis plays across this single page:
     0 at the top, a finished butterfly at the bottom. */
  function readScroll() {
    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    target = max > 12 ? clamp(window.scrollY / max, 0, 1) : 0;
  }

  /* Drift path — kept to the right so it never fights the copy.
     Narrow screens have no side column, so it tucks further out
     and dims down rather than sitting under the text. */
  function narrow() { return W < 900; }
  function pathAt(p) {
    if (narrow()) {
      return {
        x: W * (0.62 + 0.14 * Math.sin(p * Math.PI * 2.6)),
        y: H * (0.60 - 0.10 * p + 0.10 * Math.cos(p * Math.PI * 2.2))
      };
    }
    return {
      x: W * (0.70 + 0.13 * Math.sin(p * Math.PI * 2.6) - 0.16 * p),
      y: H * (0.52 - 0.10 * p + 0.12 * Math.cos(p * Math.PI * 2.2))
    };
  }

  /* =========================================================
     Paint
     ========================================================= */
  function rgba(c, a) { return 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + a.toFixed(3) + ')'; }
  var C_LILAC = [201, 184, 217], C_GLOW = [237, 231, 242],
      C_MAUVE = [139, 110, 155], C_CLAY = [201, 123, 90];
  function mix(a, b, k) {
    return [Math.round(lerp(a[0], b[0], k)), Math.round(lerp(a[1], b[1], k)), Math.round(lerp(a[2], b[2], k))];
  }

  function drawMotes(p) {
    ctx.globalCompositeOperation = 'lighter';
    var base = 0.06 + 0.10 * p;
    /* three alpha buckets, one path each — not one fill per mote */
    for (var b = 0; b < 3; b++) {
      ctx.fillStyle = rgba(C_LILAC, base * (0.35 + b * 0.32));
      ctx.beginPath();
      for (var i = b; i < motes.length; i += 3) {
        var m = motes[i];
        var y = m.y - (t * m.sp * 12) % (H + 80);
        if (y < -40) y += H + 80;
        var x = m.x + Math.sin(t * 0.4 + m.ph) * m.am;
        ctx.moveTo(x + m.r, y);
        ctx.arc(x, y, m.r, 0, 6.2832);
      }
      ctx.fill();
    }
  }

  function drawMesh(cx, cy, rot, warm, energy, alpha) {
    var edgeCol = mix(C_MAUVE, C_CLAY, warm);
    var maxR = MAXR;

    ctx.save();
    ctx.translate(cx, cy);
    ctx.rotate(rot);
    ctx.globalCompositeOperation = 'lighter';

    /* bloom: two baked sprites cross-faded by warmth */
    var R = maxR * 1.9, D = R * 2;
    ctx.globalAlpha = 0.30 * alpha * (1 - warm);
    ctx.drawImage(SPR_BLOOM_COOL, -R, -R, D, D);
    if (warm > 0.01) {
      ctx.globalAlpha = 0.30 * alpha * warm;
      ctx.drawImage(SPR_BLOOM_WARM, -R, -R, D, D);
    }
    ctx.globalAlpha = 1;

    /* the energy beam that flares during a transition (one gradient/frame) */
    if (energy > 0.02) {
      var lg = ctx.createLinearGradient(-maxR * 3.2, 0, maxR * 3.2, 0);
      lg.addColorStop(0, 'rgba(201,184,217,0)');
      lg.addColorStop(0.5, 'rgba(237,231,242,' + (0.16 * energy * alpha) + ')');
      lg.addColorStop(1, 'rgba(201,184,217,0)');
      ctx.fillStyle = lg;
      ctx.fillRect(-maxR * 3.2, -maxR * 0.05, maxR * 6.4, maxR * 0.10);
    }

    /* edges — one path, one stroke */
    ctx.lineWidth = 1;
    ctx.strokeStyle = rgba(edgeCol, 0.30 * alpha);
    ctx.beginPath();
    for (var e = 0; e < EDGES.length; e++) {
      var i = EDGES[e][0], j = EDGES[e][1];
      ctx.moveTo(PTS[i * 2], PTS[i * 2 + 1]);
      ctx.lineTo(PTS[j * 2], PTS[j * 2 + 1]);
    }
    ctx.stroke();

    /* brighter outer rim */
    ctx.strokeStyle = rgba(C_LILAC, 0.42 * alpha);
    ctx.lineWidth = 1.3;
    ctx.beginPath();
    var n1 = RINGS[0].n;
    ctx.moveTo(PTS[0], PTS[1]);
    for (var k = 1; k <= n1; k++) {
      var b1 = k % n1;
      ctx.lineTo(PTS[b1 * 2], PTS[b1 * 2 + 1]);
    }
    ctx.stroke();

    /* nodes: small dots batched into one path, glows blitted */
    ctx.fillStyle = rgba(C_LILAC, 0.62 * alpha);
    ctx.beginPath();
    for (var n2 = 0; n2 < NODES.length; n2++) {
      var x2 = PTS[n2 * 2], y2 = PTS[n2 * 2 + 1];
      ctx.moveTo(x2 + 1.15, y2);
      ctx.arc(x2, y2, 1.15, 0, 6.2832);
    }
    ctx.fill();

    for (var n3 = 0; n3 < NODES.length; n3 += 6) {
      var x3 = PTS[n3 * 2], y3 = PTS[n3 * 2 + 1];
      var tw = 0.55 + 0.45 * Math.sin(t * 1.8 + n3 * 0.7);
      ctx.globalAlpha = 0.55 * alpha * tw;
      ctx.drawImage(SPR_NODE, x3 - 9, y3 - 9, 18, 18);
    }
    ctx.globalAlpha = 1;
    ctx.restore();
  }

  /* antennae appear once the butterfly is fully formed */
  function drawAntennae(cx, cy, rot, size, k, alpha) {
    if (k <= 0.02) return;
    ctx.save();
    ctx.translate(cx, cy); ctx.rotate(rot);
    ctx.globalCompositeOperation = 'lighter';
    ctx.strokeStyle = rgba(C_LILAC, 0.5 * k * alpha);
    ctx.lineWidth = 1.2; ctx.lineCap = 'round';
    var top = -size * 0.30, len = size * 0.46 * k;
    ctx.beginPath();
    ctx.moveTo(0, top); ctx.quadraticCurveTo(-len * 0.55, top - len * 0.55, -len, top - len * 0.86);
    ctx.moveTo(0, top); ctx.quadraticCurveTo(len * 0.55, top - len * 0.55, len, top - len * 0.86);
    ctx.stroke();
    ctx.fillStyle = rgba(C_GLOW, 0.7 * k * alpha);
    ctx.beginPath(); ctx.arc(-len, top - len * 0.86, 2, 0, Math.PI * 2); ctx.fill();
    ctx.beginPath(); ctx.arc(len, top - len * 0.86, 2, 0, Math.PI * 2); ctx.fill();
    ctx.restore();
  }

  /* =========================================================
     Frame
     ========================================================= */
  function frame(now) {
    if (!running) return;

    /* Only the Butterfly Effect page animates. On the multi-page site
       the other pages carry no canvas at all; in a single-file build
       they share one, so honour the body flag either way. */
    if (!document.body.classList.contains('bg-live')) {
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      ctx.clearRect(0, 0, W, H);
      requestAnimationFrame(frame);
      return;
    }

    t = (now - t0) / 1000;

    /* Follow factor: how hard the mesh chases the scroll position. Higher
       is more responsive. Touch screens get a tighter follow because the
       drift that reads as elegant on a trackpad reads as lag on a phone. */
    smooth += (target - smooth) * (reduce ? 1 : (narrow() ? 0.16 : 0.09));
    var p = smooth;

    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'source-over';

    /* The metamorphosis completes at ~85% of the page so the finished
       butterfly lands on the closing quote band rather than behind the
       footer; the last stretch holds it complete and lets it ripple. */
    var stageF = clamp(p / 0.85 * 3, 0, 3);
    var done = seg(stageF, 2.45, 3);            // how "finished" the butterfly is
    var frac = stageF - Math.floor(stageF);
    var energy = Math.sin(clamp(frac, 0, 1) * Math.PI) * (stageF < 2.98 ? 1 : 0.25);
    var warm = Math.sin(clamp((p - 0.20) / 0.55, 0, 1) * Math.PI) * 0.85;

    /* wing beat only once there are wings to beat */
    var beat = (Math.sin(t * (1.6 + 2.6 * done)) + 1) / 2;
    var flap = lerp(1, lerp(0.46, 1, beat), done);

    var base = Math.min(W, H);
    var size = base * (0.16 + 0.10 * done) * (narrow() ? 0.92 : 1);
    var vis = narrow() ? 0.85 : 1;   // the wireframe is the point of this page

    var pos = pathAt(p);
    var bob = Math.sin(t * 1.1) * (5 + 9 * done);
    var cx = pos.x + Math.sin(t * 0.35) * 12;
    var cy = pos.y + bob;
    var rot = Math.sin(t * 0.42) * 0.05 * done;

    solve(stageF, size, flap);

    ribbon();
    drawMotes(p);
    drawMesh(cx, cy, rot, warm, energy, vis);
    drawAntennae(cx, cy, rot, size, done, vis);

    /* the butterfly effect: the ripples that follow one small shift */
    var rippleK = seg(p, 0.88, 1);
    if (rippleK > 0.01) {
      for (var i = 0; i < 5; i++) {
        var lag = clamp((rippleK - i * 0.10) / 0.55, 0, 1);
        if (lag <= 0) continue;
        var ang = (i / 5) * Math.PI * 2 + t * 0.12;
        var rad = base * 0.42 * lag;
        var sx = cx + Math.cos(ang) * rad * 1.25;
        var sy = cy + Math.sin(ang) * rad * 0.65;
        var sb = (Math.sin(t * (2.4 + i * 0.5) + i) + 1) / 2;
        solve(3, size * (0.26 + i * 0.03), lerp(0.46, 1, sb));
        drawMesh(sx, sy, Math.sin(t * 0.5 + i) * 0.2, warm, 0, 0.42 * lag * vis);
      }
      solve(stageF, size, flap);
    }

    requestAnimationFrame(frame);
  }

  /* ---------- stage ribbon ---------- */
  var fill = document.querySelector('.ribbon .fill');
  var label = document.querySelector('.ribbon .stage');
  var lastPct = -1, lastName = '';
  /* Called from inside the animation frame, never from the scroll event —
     writing layout on every scroll tick is what makes iOS scrolling stutter. */
  function ribbon() {
    var p = target;
    var pct = Math.round(p * 100);
    if (fill && pct !== lastPct) { fill.style.width = pct + '%'; lastPct = pct; }
    if (label) {
      var sF = clamp(p / 0.85 * 3, 0, 3);
      var name = sF < 0.85 ? 'Larva' : sF < 1.85 ? 'Chrysalis'
               : sF < 2.75 ? 'Emerging' : 'Butterfly';
      if (name !== lastName) { label.textContent = name; lastName = name; }
    }
  }

  addEventListener('resize', resize, { passive: true });
  addEventListener('scroll', readScroll, { passive: true });   // no DOM writes here
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) running = false;
    else if (!running) { running = true; t0 = performance.now() - t * 1000; requestAnimationFrame(frame); }
  });

  resize();
  readScroll();
  smooth = target;
  ribbon();
  requestAnimationFrame(frame);
})();

/* ===========================================================
   Shared UI: nav, reveals, forms
   =========================================================== */
(function () {
  'use strict';

  var hdr = document.getElementById('hdr');
  if (hdr) addEventListener('scroll', function () {
    hdr.classList.toggle('scrolled', window.scrollY > 8);
  }, { passive: true });

  var tgl = document.getElementById('navtoggle'), links = document.getElementById('navlinks');
  if (tgl && links) {
    tgl.addEventListener('click', function () {
      tgl.setAttribute('aria-expanded', links.classList.toggle('open'));
    });
    links.addEventListener('click', function (e) {
      if (e.target.closest('a')) links.classList.remove('open');
    });
  }

  var here = location.pathname.split('/').pop() || 'index.html';
  Array.prototype.forEach.call(document.querySelectorAll('.navlinks a[href]'), function (a) {
    if (a.getAttribute('href') === here) a.classList.add('current');
  });

  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: .1, rootMargin: '0px 0px -50px' });
  Array.prototype.forEach.call(document.querySelectorAll('.rv'), function (el, i) {
    el.style.transitionDelay = (i % 3 * 90) + 'ms'; io.observe(el);
  });

  Array.prototype.forEach.call(document.querySelectorAll('form[data-demo]'), function (form) {
    var note = form.querySelector('.formnote');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var name = (d.get('first') || d.get('name') || '').toString().trim();
      var mail = (d.get('email') || '').toString().trim();
      if (!name || !/^\S+@\S+\.\S+$/.test(mail)) {
        if (note) note.textContent = 'Please add your name and a valid email address.';
        return;
      }
      if (note) note.textContent = form.getAttribute('data-ok') ||
        'Thank you — we’ll be in touch shortly.';
      form.reset();
    });
  });
})();
