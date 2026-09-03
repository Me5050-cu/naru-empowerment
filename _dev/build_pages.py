# -*- coding: utf-8 -*-
"""Assembles the NaRu site pages from one shared shell."""

import hashlib as _hl

def _asset_hash():
    """Short content hash of the shared assets. Appended to their URLs so a
    push always busts the browser cache — otherwise returning visitors keep
    the old CSS/JS and never see the change."""
    h = _hl.sha256()
    for f in ("assets/site.css", "assets/butterfly.js", "assets/light.css"):
        h.update(open("../" + f, "rb").read())
    return h.hexdigest()[:10]

ASSET_HASH = _asset_hash()

BASE_URL = "https://me5050-cu.github.io/naru-empowerment/"
DARK_ICON  = "data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%20120%20100%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%2523CFBEDE%27%20stroke-width%3D%277%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M60%2038C72%2016%2092%204%20104%2012c11%208%206%2030-10%2040-11%207-27%204-34-4Z%27%2F%3E%3Cpath%20d%3D%27M60%2052c13%202%2030%208%2034%2020%204%2012-8%2020-18%2016-11-5-16-14-16-24Z%27%2F%3E%3Cpath%20d%3D%27M60%2038C48%2016%2028%204%2016%2012%205%2020%2010%2042%2026%2052c11%207%2027%204%2034-4Z%27%2F%3E%3Cpath%20d%3D%27M60%2052c-13%202-30%208-34%2020-4%2012%208%2020%2018%2016%2011-5%2016-14%2016-24Z%27%2F%3E%3Cpath%20d%3D%27M60%2032v46%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E"
LIGHT_ICON = "data:image/svg+xml,%3Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%20120%20100%27%3E%3Cg%20fill%3D%27none%27%20stroke%3D%27%25235E4770%27%20stroke-width%3D%277%27%20stroke-linejoin%3D%27round%27%20stroke-linecap%3D%27round%27%3E%3Cpath%20d%3D%27M60%2038C72%2016%2092%204%20104%2012c11%208%206%2030-10%2040-11%207-27%204-34-4Z%27%2F%3E%3Cpath%20d%3D%27M60%2052c13%202%2030%208%2034%2020%204%2012-8%2020-18%2016-11-5-16-14-16-24Z%27%2F%3E%3Cpath%20d%3D%27M60%2038C48%2016%2028%204%2016%2012%205%2020%2010%2042%2026%2052c11%207%2027%204%2034-4Z%27%2F%3E%3Cpath%20d%3D%27M60%2052c-13%202-30%208-34%2020-4%2012%208%2020%2018%2016%2011-5%2016-14%2016-24Z%27%2F%3E%3Cpath%20d%3D%27M60%2032v46%27%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E"

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="{themecolor}">
<link rel="icon" href="{favicon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="NaRu Empowerment Life Coach Group">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ap}assets/site.css?v={assethash}">{extracss}
<noscript><style>.rv{{opacity:1!important;transform:none!important}}</style></noscript>
</head>
<body{bodyclass}>
{canvas}

<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="bfly-mark" viewBox="0 0 120 100">
    <g fill="none" stroke="currentColor" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
      <path d="M60 38C72 16 92 4 104 12c11 8 6 30-10 40-11 7-27 4-34-4Z"/>
      <path d="M60 52c13 2 30 8 34 20 4 12-8 20-18 16-11-5-16-14-16-24Z"/>
      <path d="M60 38C48 16 28 4 16 12 5 20 10 42 26 52c11 7 27 4 34-4Z"/>
      <path d="M60 52c-13 2-30 8-34 20-4 12 8 20 18 16 11-5 16-14 16-24Z"/>
      <path d="M60 32v46"/>
      <path d="M60 32c-4-8-10-13-16-15M60 32c4-8 10-13 16-15"/>
    </g>
  </symbol>
</svg>

<a class="skip" href="#main">Skip to content</a>

<header id="hdr">
  <div class="nav">
    <a class="logo" href="index.html" aria-label="NaRu Empowerment home">
      <svg class="mark" viewBox="0 0 120 100"><use href="#bfly-mark"/></svg>
      <div>
        <div class="name">Na<b>Ru</b></div>
        <div class="sub">Empowerment</div>
      </div>
    </a>
    <nav class="navlinks" id="navlinks">
      <a href="coaching.html">Coaching</a>
      <a href="butterfly-effect.html">The Butterfly Effect</a>
      <a href="naomi.html">Meet Naomi</a>
      <a href="connect.html">Connect</a>
      <a class="btn btn-ink" href="connect.html#book">Schedule a call</a>
    </nav>
    <button class="navtoggle" id="navtoggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
{ribbon}</header>

<main id="main">
"""

FOOT = """</main>

<footer>
  <div class="foot">
    <div>
      <div class="logo">
        <svg class="mark" viewBox="0 0 120 100"><use href="#bfly-mark"/></svg>
        <div>
          <div class="name">Na<b>Ru</b></div>
          <div class="sub">Empowerment</div>
        </div>
      </div>
      <p class="tagline">Inspiring growth while<br><em>empowering change.</em></p>
      <div class="social">
        <a href="#" aria-label="Facebook"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M14 8.5V7c0-.8.4-1 1-1h1.5V3H14c-2.2 0-3.5 1.4-3.5 3.6V8.5H8.5V12h2V21H14v-9h2.3l.4-3.5H14Z"/></svg></a>
        <a href="#" aria-label="Instagram"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17" cy="7" r="1" fill="currentColor" stroke="none"/></svg></a>
        <a href="#" aria-label="LinkedIn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4.5 9h3v11h-3zM6 4a1.8 1.8 0 1 0 0 3.6A1.8 1.8 0 0 0 6 4Zm4 5h2.9v1.5c.5-.9 1.7-1.8 3.3-1.8 3 0 3.8 1.8 3.8 4.4V20h-3v-6c0-1.5-.6-2.4-1.9-2.4-1.2 0-2.1.9-2.1 2.4v6h-3Z"/></svg></a>
        <a href="#" aria-label="YouTube"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22 12s0-3.2-.4-4.7a2.5 2.5 0 0 0-1.7-1.8C18.3 5 12 5 12 5s-6.3 0-7.9.5A2.5 2.5 0 0 0 2.4 7.3C2 8.8 2 12 2 12s0 3.2.4 4.7c.2.9.9 1.6 1.7 1.8C5.7 19 12 19 12 19s6.3 0 7.9-.5a2.5 2.5 0 0 0 1.7-1.8C22 15.2 22 12 22 12ZM10 15V9l5.2 3Z"/></svg></a>
      </div>
    </div>
    <div>
      <h4>The four chapters</h4>
      <a href="coaching.html">Coaching</a>
      <a href="butterfly-effect.html">The Butterfly Effect</a>
      <a href="naomi.html">Meet Naomi</a>
      <a href="connect.html">Connect</a>
    </div>
    <div>
      <h4>Work with us</h4>
      <a href="connect.html#book">Discovery call</a>
      <a href="coaching.html#one-to-one">1:1 coaching</a>
      <a href="coaching.html#leadership">Leadership development</a>
      <a href="connect.html#newsletter">Newsletter</a>
    </div>
    <div>
      <h4>Connect</h4>
      <a class="contact-row" href="tel:+16785809648"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h3l1.5 4-2 1.5a12 12 0 0 0 6 6L15 13.5 19 15v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 6.2 2 2 0 0 1 5 4Z"/></svg> (678) 580-9648</a>
      <a class="contact-row" href="mailto:info@narucoaching.com"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="m2.5 7.5 9.5 6 9.5-6"/></svg> info@narucoaching.com</a>
      <a class="contact-row" href="index.html"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 3 2.5 15 0 18M12 3c-2.5 3-2.5 15 0 18"/></svg> narucoaching.com</a>
    </div>
  </div>
  <div class="legal">
    <span>&copy; 2026 NaRu Empowerment Life Coach Group. All rights reserved.</span>
    <span><a href="#" style="display:inline">Privacy policy</a> &nbsp;&middot;&nbsp; <a href="#" style="display:inline">Terms of service</a></span>
  </div>
</footer>

<script src="{ap}assets/butterfly.js?v={assethash}"></script>
</body>
</html>
"""

CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m4 12 6 6L20 6"/></svg>'

def pager(items):
    out = ['<section class="veil"><div class="wrap"><div class="pager">']
    for kick, title, blurb, href in items:
        out.append(
            '<a class="pagecard rv" href="%s"><span>%s</span><h4>%s</h4>'
            '<p>%s</p></a>' % (href, kick, title, blurb))
    out.append('</div></div></section>')
    return "\n".join(out)

import os
RIBBON = """  <div class="ribbon">
    <div class="ribbon-in">
      <span>Metamorphosis</span>
      <span class="stage">Larva</span>
      <span class="track"><span class="fill"></span></span>
      <span>Scroll to complete</span>
    </div>
  </div>
"""

def page(fname, title, desc, body, live=False, theme="dark", subdir=""):
    """live=True gives the page the animated wireframe background.
    theme="light" layers the light override and flips the render mode.
    subdir puts the output in a folder, adjusting asset paths."""
    ap = "../" if subdir else ""
    extra = ('\n<link rel="stylesheet" href="%sassets/light.css?v=%s">' % (ap, ASSET_HASH)
             if theme == "light" else "")
    cls = " ".join(filter(None, [
        "bg-live" if live else "",
        "theme-light" if theme == "light" else "",
    ]))
    html = HEAD.format(
        title=title, desc=desc, assethash=ASSET_HASH, ap=ap, extracss=extra,
        canon=BASE_URL + (subdir + "/" if subdir else "") + (fname if fname != "index.html" else ""),
        themecolor="#F7F5F3" if theme == "light" else "#131017",
        favicon=LIGHT_ICON if theme == "light" else DARK_ICON,
        bodyclass=(' class="%s"' % cls) if cls else '',
        canvas='\n<canvas id="bgfx" aria-hidden="true"></canvas>\n' if live else '',
        ribbon=RIBBON if live else '',
    ) + body + FOOT.replace('{assethash}', ASSET_HASH).replace('{ap}', ap)
    out = "../" + (subdir + "/" if subdir else "") + fname
    import os as _os
    _os.makedirs(_os.path.dirname(out), exist_ok=True) if subdir else None
    with open(out, "w") as f:
        f.write(html)
    print("%-30s %6d bytes" % (out.replace("../", ""), len(html)))
