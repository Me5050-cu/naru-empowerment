# -*- coding: utf-8 -*-
"""Packs the five-page site into one self-contained file for an Artifact
preview. Artifacts allow no relative assets and no multi-file sites, so
the CSS and JS are inlined and a hash router swaps the pages."""
import re, io, os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

CSS = open("assets/site.css").read()
JS  = open("assets/butterfly.js").read()

PAGES = [
    ("index",            "index.html"),
    ("coaching",         "coaching.html"),
    ("butterfly-effect", "butterfly-effect.html"),
    ("naomi",            "naomi.html"),
    ("connect",          "connect.html"),
]

def grab(html, tag):
    m = re.search(r"<%s[^>]*>(.*?)</%s>" % (tag, tag), html, re.S)
    return m.group(1) if m else ""

def block(html, opener):
    """Extract a <div> block by counting depth — a non-greedy regex stops
    at the first nested close and silently truncates the markup."""
    i = html.index(opener)
    depth, j = 0, i
    while True:
        nxt_o = html.find("<div", j)
        nxt_c = html.find("</div>", j)
        if nxt_c == -1:
            raise ValueError("unbalanced: " + opener)
        if nxt_o != -1 and nxt_o < nxt_c:
            depth += 1; j = nxt_o + 4
        else:
            depth -= 1; j = nxt_c + 6
            if depth == 0:
                return html[i:j]

src = {k: open(f).read() for k, f in PAGES}

# shared chrome, lifted from the real pages so nothing drifts
symbols = re.search(r'(<svg width="0".*?</svg>)', src["index"], re.S).group(1)
footer  = grab(src["index"], "footer")
ribbon  = block(src["butterfly-effect"], '<div class="ribbon">')
nav     = block(src["index"], '<div class="nav">')

# each page's <main>, wrapped so the router can swap them
panels = []
for key, _ in PAGES:
    panels.append('<div class="route" data-route="%s" hidden>\n%s\n</div>'
                  % (key, grab(src[key], "main")))

ROUTER = r"""
/* ---------- single-file router ----------
   The published preview is one file, so page links become hash routes
   (#/coaching, #/connect/book). Everything else — nav state, the
   metamorphosis flag, the ribbon — follows the active route. */
(function () {
  'use strict';
  var ROUTES = ['index','coaching','butterfly-effect','naomi','connect'];
  var panels = {}, ribbon = document.querySelector('.ribbon');

  ROUTES.forEach(function (r) {
    panels[r] = document.querySelector('.route[data-route="' + r + '"]');
  });

  function show(route, anchor, push) {
    if (ROUTES.indexOf(route) < 0) route = 'index';

    ROUTES.forEach(function (r) { panels[r].hidden = (r !== route); });

    /* the wireframe lives on one page only */
    document.body.classList.toggle('bg-live', route === 'butterfly-effect');
    if (ribbon) ribbon.hidden = (route !== 'butterfly-effect');

    /* nav state */
    Array.prototype.forEach.call(
      document.querySelectorAll('.navlinks a[data-route]'), function (a) {
        a.classList.toggle('current', a.getAttribute('data-route') === route);
      });

    var main = document.querySelector('main');
    if (main) main.setAttribute('data-active', route);

    if (push) {
      var h = '#/' + route + (anchor ? '/' + anchor : '');
      if (location.hash !== h) history.pushState(null, '', h);
    }

    /* Scope the lookup to the visible panel: ids can legitimately repeat
       across pages that were separate documents before bundling. */
    if (anchor) {
      var el = panels[route].querySelector('#' + CSS.escape(anchor));
      if (el) { el.scrollIntoView({ behavior: 'instant', block: 'start' }); return; }
    }
    window.scrollTo(0, 0);
    window.dispatchEvent(new Event('scroll'));
  }

  function parse() {
    var raw = location.hash.replace(/^#\/?/, '');
    var bits = raw.split('/');
    return { route: bits[0] || 'index', anchor: bits[1] || '' };
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (!href || /^(https?:|mailto:|tel:)/.test(href)) return;

    if (href.indexOf('.html') > -1) {
      e.preventDefault();
      var parts = href.split('#');
      var route = parts[0].replace('.html', '') || 'index';
      show(route, parts[1] || '', true);
      var nl = document.getElementById('navlinks');
      if (nl) nl.classList.remove('open');
      return;
    }
    if (href.charAt(0) === '#' && href.length > 1 && href.indexOf('#/') !== 0) {
      var live = document.querySelector('.route:not([hidden])');
      var t = live && live.querySelector('#' + CSS.escape(href.slice(1)));
      if (t) { e.preventDefault(); t.scrollIntoView({ behavior: 'smooth' }); }
    }
  });

  addEventListener('popstate', function () { var p = parse(); show(p.route, p.anchor, false); });

  var p0 = parse();
  show(p0.route, p0.anchor, false);
})();
"""

# nav links need route hooks for the current-page state
nav = re.sub(r'href="([a-z\-]+)\.html([^"]*)"',
             lambda m: 'href="%s.html%s" data-route="%s"' % (m.group(1), m.group(2), m.group(1)),
             nav)

out = io.StringIO()
out.write('<title>NaRu Empowerment</title>\n')
out.write('<link rel="preconnect" href="https://fonts.googleapis.com">\n')
out.write('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n')
out.write('<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;'
          '9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600;700&display=swap" '
          'rel="stylesheet">\n')
out.write('<style>\n%s\n.route[hidden]{display:none}\n.ribbon[hidden]{display:none}\n</style>\n'
          % CSS)
out.write('\n<canvas id="bgfx" aria-hidden="true"></canvas>\n')
out.write(symbols + "\n")
out.write('<header id="hdr">\n%s\n%s\n</header>\n' % (nav, ribbon))
out.write('<main>\n%s\n</main>\n' % "\n".join(panels))
out.write('<footer>\n%s\n</footer>\n' % footer)
out.write('<script>\n%s\n%s\n</script>\n' % (JS, ROUTER))

dest = "/private/tmp/claude-501/-Users-morganelder-Claude/db70085f-3a8f-4c5e-9d15-bd6e3b365a65/scratchpad/naru-preview.html"
open(dest, "w").write(out.getvalue())
print("bundled -> %s  (%d bytes)" % (dest, len(out.getvalue())))
