# -*- coding: utf-8 -*-
from build_pages import page, pager, CHECK

# ============================== HOME =========================
home = """
<section class="hero">
  <div class="hero-in">
    <div class="hero-copy rv">
      <p class="kick">Small shifts. Big transformation.</p>
      <h1>Your next chapter<span class="mv">begins with one</span><em>small shift.</em></h1>
      <div class="divider"><i></i></div>
      <p class="lead">Transformational coaching for greater <b>clarity, confidence, alignment,</b> and professional action.</p>
      <div class="hero-actions">
        <a class="btn btn-ink" href="connect.html#book">Begin your next chapter <span class="arw">&rarr;</span></a>
        <a class="btn btn-ghost" href="butterfly-effect.html">See how it works</a>
      </div>
    </div>
  </div>
  <div class="scroll-hint"><i></i> Scroll &mdash; the cocoon is stirring</div>
</section>

<section class="pad veil">
  <div class="wrap">
    <div class="sec-head rv">
      <span class="eyebrow">Where to begin</span>
      <h2 class="sec" style="margin-top:.8rem">Four chapters, <span class="mv">one journey.</span></h2>
      <p>This site follows the same arc our coaching does. Each chapter carries the butterfly a little further &mdash; start anywhere, or move through them in order.</p>
    </div>
    <div class="grid-2">
      <a class="card rv" href="coaching.html">
        <span class="num">CHAPTER 01</span>
        <div class="icon i-mauve"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20c0-7 4-11 9-12 0 7-3 11-9 12Z"/><path d="M11 20c0-5-3-8-7-8.5C4 16 6.5 19.5 11 20Z"/><path d="M11 20v2"/></svg></div>
        <h3>Coaching</h3>
        <p>The three areas we work in &mdash; spiritual growth, emotional healing, and professional development &mdash; and what a session actually looks like.</p>
      </a>
      <a class="card rv" href="butterfly-effect.html">
        <span class="num">CHAPTER 02</span>
        <div class="icon i-clay"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round"><path d="M12 3v18M3 12h18M5.6 5.6l12.8 12.8M18.4 5.6 5.6 18.4"/></svg></div>
        <h3>The Butterfly Effect</h3>
        <p>Cocoon, Transform, Rise. The methodology behind the work, broken into three movements you can actually follow.</p>
      </a>
      <a class="card rv" href="naomi.html">
        <span class="num">CHAPTER 03</span>
        <div class="icon i-ink"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="9" r="4.5"/><path d="M4 21c0-4.2 3.6-7 8-7s8 2.8 8 7"/></svg></div>
        <h3>Meet Naomi</h3>
        <p>Twenty years of leadership, service, and real life &mdash; and why she built NaRu Empowerment.</p>
      </a>
      <a class="card rv" href="connect.html">
        <span class="num">CHAPTER 04</span>
        <div class="icon i-mauve"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="m2.5 7.5 9.5 6 9.5-6"/></svg></div>
        <h3>Connect</h3>
        <p>Book a discovery call, send a message, or join the community. This is where the shift starts.</p>
      </a>
    </div>
  </div>
</section>

<section class="pad veil-open">
  <div class="wrap">
    <div class="sec-head rv" style="margin-inline:auto;text-align:center">
      <span class="eyebrow">Why it works</span>
      <h2 class="sec" style="margin-top:.8rem">You don't need to <span class="mv">overhaul your life.</span></h2>
      <p style="margin-inline:auto">A butterfly's wingbeat doesn't move the storm. It starts the chain that does. Coaching works the same way &mdash; we find the one small shift that changes the shape of everything downstream.</p>
    </div>
  </div>
</section>

<section class="quote veil-ink">
  <div class="wrap rv">
    <p class="l1">Every transformation begins with a single wingbeat.</p>
    <p class="l2">You are becoming who you were created to be.</p>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="rv">
      <h2>Ready for your next chapter?</h2>
      <p>Start with a conversation about where you are and where you want to go.</p>
    </div>
    <div class="rv">
      <a class="btn btn-light" href="connect.html#book">Schedule a discovery call <span class="arw">&rarr;</span></a>
      <small>Let's create your transformation plan.</small>
    </div>
  </div>
</section>
"""

# ============================== COACHING =====================
coaching = """
<section class="phero">
  <div class="wrap">
    <p class="crumb rv"><a href="index.html">Home</a> &nbsp;/&nbsp; Chapter 01</p>
    <div class="rv">
      <span class="eyebrow">Coaching</span>
      <h1>What part of your life is <span class="mv">ready for transformation?</span></h1>
      <p class="sub">NaRu Empowerment supports individuals navigating growth, change and their next chapter. Through personalized coaching and proven strategies, we help you create meaningful change from the inside out.</p>
    </div>
  </div>
</section>

<section class="pad veil">
  <div class="wrap">
    <div class="grid-3">
      <div class="card rv" id="spiritual">
        <span class="num">01</span>
        <div class="icon i-mauve"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20c0-7 4-11 9-12 0 7-3 11-9 12Z"/><path d="M11 20c0-5-3-8-7-8.5C4 16 6.5 19.5 11 20Z"/><path d="M11 20v2"/></svg></div>
        <h3>Spiritual growth</h3>
        <p>Cultivate inner peace, align with your values, and deepen your connection with self and purpose.</p>
        <ul>
          <li>{c} Clarifying what you actually believe and want</li>
          <li>{c} Practices for stillness that survive a busy week</li>
          <li>{c} Aligning daily choices with deeper values</li>
        </ul>
      </div>
      <div class="card rv" id="emotional">
        <span class="num">02</span>
        <div class="icon i-ink"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7-4.4-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.6-7 9-7 9Z"/><path d="M9.5 11h5l-2.5 4Z"/></svg></div>
        <h3>Emotional healing</h3>
        <p>Release what no longer serves you, build resilience, and create emotional strength that lasts.</p>
        <ul>
          <li>{c} Naming the patterns that keep repeating</li>
          <li>{c} Working through grief, burnout, and transition</li>
          <li>{c} Building resilience you can rely on under pressure</li>
        </ul>
      </div>
      <div class="card rv" id="leadership">
        <span class="num">03</span>
        <div class="icon i-clay"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round"><path d="M12 3v18M3 12h18M5.6 5.6l12.8 12.8M18.4 5.6 5.6 18.4"/></svg></div>
        <h3>Professional development</h3>
        <p>Elevate your leadership, build new skills, and step confidently into your next level of impact and influence.</p>
        <ul>
          <li>{c} Leading with authority that feels like your own</li>
          <li>{c} Navigating promotions, pivots, and hard conversations</li>
          <li>{c} Building influence without burning out</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="pad veil-2" id="one-to-one">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="eyebrow">How we work</span>
        <h2 class="sec" style="margin-top:.8rem">What a session <span class="mv">actually looks like.</span></h2>
        <p class="lede">No scripts, no one-size-fits-all worksheets. Every engagement is built around where you are right now &mdash; and where you've said you want to go.</p>
      </div>
      <div class="rv">
        <div class="grid-2" style="gap:1rem">
          <div class="card"><h3 style="font-size:1.2rem">Discovery call</h3><p>Thirty minutes, free. We talk about what's happening and whether coaching is the right fit. No pressure either way.</p></div>
          <div class="card"><h3 style="font-size:1.2rem">Your plan</h3><p>A transformation plan built around your goals, your season of life, and the pace you can actually sustain.</p></div>
          <div class="card"><h3 style="font-size:1.2rem">The work</h3><p>Regular sessions grounded in the Butterfly Effect Methodology, with practical work between them.</p></div>
          <div class="card"><h3 style="font-size:1.2rem">Momentum</h3><p>We track what's shifting, adjust what isn't working, and keep building on what is.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="quote veil-ink">
  <div class="wrap rv">
    <p class="l1">You don't have to have it figured out to begin.</p>
    <p class="l2">You only have to be willing to move.</p>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="rv"><h2>Not sure which area is yours?</h2><p>Most people arrive with one and discover it's really another. That's what the discovery call is for.</p></div>
    <div class="rv"><a class="btn btn-light" href="connect.html#book">Book a discovery call <span class="arw">&rarr;</span></a><small>Free, thirty minutes, no obligation.</small></div>
  </div>
</section>
""".replace("{c}", CHECK)

coaching += pager([
    ("Chapter 02", "The Butterfly Effect",
     "The three movements behind every engagement: Cocoon, Transform, Rise.",
     "butterfly-effect.html"),
    ("Chapter 03", "Meet Naomi",
     "The leadership, service, and real life behind NaRu Empowerment.",
     "naomi.html"),
])

# ============================== BUTTERFLY EFFECT =============
method = """
<section class="phero">
  <div class="wrap">
    <p class="crumb rv"><a href="index.html">Home</a> &nbsp;/&nbsp; Chapter 02</p>
    <div class="rv">
      <span class="eyebrow">The method</span>
      <h1>The Butterfly Effect <span class="mv">Methodology</span><sup style="font-size:.3em;vertical-align:super">&trade;</sup></h1>
      <p class="sub">A butterfly's wingbeat doesn't move the storm &mdash; it begins the chain that does. Three movements carry you from where you are to who you are becoming.</p>
    </div>
  </div>
</section>

<section class="pad veil">
  <div class="wrap">
    <div class="stagerow rv">
      <div class="orb"><div class="disc d1"></div><svg width="62" height="52" viewBox="0 0 120 100"><use href="#bfly-mark"/></svg></div>
      <div>
        <h3>Cocoon</h3>
        <p class="beat">Ground. Reflect. Create inner stillness.</p>
        <p>Nothing changes while you're still running. The first movement is a deliberate stop &mdash; long enough to hear yourself think and to tell the difference between what you actually want and what you've been carrying because someone handed it to you.</p>
        <p>This is the least glamorous part of the work and the part people most want to skip. It's also the part that makes everything after it possible.</p>
        <div class="tags"><span class="tag-pill">Self-inventory</span><span class="tag-pill">Values clarification</span><span class="tag-pill">Stillness practice</span><span class="tag-pill">Honest assessment</span></div>
      </div>
    </div>

    <div class="stagerow rv">
      <div class="orb"><div class="disc d2"></div><svg width="62" height="52" viewBox="0 0 120 100"><use href="#bfly-mark"/></svg></div>
      <div>
        <h3>Transform</h3>
        <p class="beat">Release. Heal. Renew your mind.</p>
        <p>Inside the chrysalis, the caterpillar doesn't grow wings &mdash; it dissolves and reorganizes entirely. The second movement is the same kind of honest undoing: releasing the beliefs, habits, and stories that got you here but won't get you there.</p>
        <p>This is where the emotional work lives. It can be uncomfortable. It is never done alone.</p>
        <div class="tags"><span class="tag-pill">Pattern work</span><span class="tag-pill">Releasing what's finished</span><span class="tag-pill">Reframing</span><span class="tag-pill">Resilience building</span></div>
      </div>
    </div>

    <div class="stagerow rv">
      <div class="orb"><div class="disc d3"></div><svg width="62" height="52" viewBox="0 0 120 100"><use href="#bfly-mark"/></svg></div>
      <div>
        <h3>Rise</h3>
        <p class="beat">Align. Take action. Live on purpose.</p>
        <p>Insight that never becomes action is just a nicer way of staying put. The third movement is deliberate, structured, accountable action &mdash; the part where the new understanding becomes a new way of living.</p>
        <p>Wings don't work immediately. We build the strength to use them.</p>
        <div class="tags"><span class="tag-pill">Goal architecture</span><span class="tag-pill">Accountability</span><span class="tag-pill">Leadership practice</span><span class="tag-pill">Sustainable momentum</span></div>
      </div>
    </div>
  </div>
</section>

<section class="pad veil-open">
  <div class="wrap center">
    <div class="rv" style="max-width:640px;margin-inline:auto">
      <span class="eyebrow">Worth saying plainly</span>
      <h2 class="sec" style="margin-top:.8rem">It isn't <span class="mv">linear.</span></h2>
      <p style="color:var(--muted)">Most people move through these movements more than once, and often in circles rather than a straight line. Returning to Cocoon after a season of Rise isn't failure &mdash; it's the method working exactly as intended.</p>
    </div>
  </div>
</section>

<section class="quote veil-ink">
  <div class="wrap rv">
    <p class="l1">Small shifts. Big transformation.</p>
    <p class="l2">The smallest movement, repeated, rewrites everything downstream.</p>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="rv"><h2>Which movement are you in?</h2><p>Most people already know. A discovery call helps you name it and decide what comes next.</p></div>
    <div class="rv"><a class="btn btn-light" href="connect.html#book">Find out together <span class="arw">&rarr;</span></a><small>Free, thirty minutes, no obligation.</small></div>
  </div>
</section>
"""

method += pager([
    ("Chapter 03", "Meet Naomi",
     "The leadership, service, and real life behind the method.", "naomi.html"),
    ("Chapter 01", "Coaching",
     "The three areas we work in and what a session looks like.", "coaching.html"),
])

# ============================== NAOMI ========================
naomi = """
<section class="phero">
  <div class="wrap">
    <p class="crumb rv"><a href="index.html">Home</a> &nbsp;/&nbsp; Chapter 03</p>
    <div class="rv">
      <span class="eyebrow">Meet the founder</span>
      <h1>Naomi R. <span class="mv">Wiley</span></h1>
      <p class="sub">CEO &amp; Founder &middot; U.S. Army Veteran &middot; Certified Life Coach</p>
    </div>
  </div>
</section>

<section class="pad veil">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <div class="portrait"><div class="ph">Portrait &mdash; add naomi.jpg</div></div>
        <div class="creds">
          <div class="cred"><div class="ring"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="9" r="5"/><path d="M9 13.5 8 22l4-2.2L16 22l-1-8.5"/></svg></div><span>U.S. Army Veteran</span></div>
          <div class="cred"><div class="ring"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.2"/></svg></div><span>Certified Life Coach</span></div>
          <div class="cred"><div class="ring"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="9" cy="9" r="3.2"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5"/><path d="M16 7.2a3 3 0 0 1 0 5.6M17.5 14.4c2 .7 3.5 2.3 3.5 4.6"/></svg></div><span>Leadership &amp; HR Expert</span></div>
          <div class="cred"><div class="ring"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 20s-7-4.4-7-9a4 4 0 0 1 7-2.6A4 4 0 0 1 19 11c0 4.6-7 9-7 9Z"/></svg></div><span>Wife, Mother &amp; Purpose-Driven Leader</span></div>
        </div>
      </div>
      <div class="rv">
        <h2 class="sec">Twenty years of leadership, service, <span class="mv">and real life.</span></h2>
        <p class="lede">With over 20 years of leadership, service, and real-life experience, Naomi empowers individuals to break through limitations and create lives of clarity, confidence, and purpose.</p>
        <p style="color:var(--muted);margin-top:1.4rem">Her mission is simple: to inspire growth while empowering change &mdash; and to help you transform your life one day and one step at a time.</p>
        <p style="color:var(--muted)">That mission didn't come from a textbook. It came from military service, from years inside leadership and HR watching capable people stall out for reasons no org chart explains, and from her own seasons of rebuilding. The Butterfly Effect Methodology is what she built out of all of it.</p>

        <div class="factrow">
          <div class="fact"><b>20+</b><span>Years of leadership and service</span></div>
          <div class="fact"><b>3</b><span>Areas of focused coaching practice</span></div>
          <div class="fact"><b>1</b><span>Small shift to begin</span></div>
        </div>

        <a class="btn btn-ink" style="margin-top:2.4rem" href="connect.html#book">Work with Naomi <span class="arw">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<section class="pad veil-2">
  <div class="wrap">
    <div class="sec-head rv" style="margin-inline:auto;text-align:center">
      <span class="eyebrow">What she believes</span>
      <h2 class="sec" style="margin-top:.8rem">Four convictions <span class="mv">behind the work.</span></h2>
    </div>
    <div class="grid-2">
      <div class="card rv"><h3>You are not starting from zero</h3><p>Everything you've survived is material. Coaching doesn't replace your history &mdash; it puts it to work.</p></div>
      <div class="card rv"><h3>Small is not slow</h3><p>The shift that changes everything is usually unglamorous and close at hand. Scale comes from repetition, not scale.</p></div>
      <div class="card rv"><h3>Clarity precedes confidence</h3><p>Confidence isn't something you talk yourself into. It arrives once you know what you actually want.</p></div>
      <div class="card rv"><h3>Growth is not a solo act</h3><p>Nobody thinks their way out alone. Being genuinely seen is not a luxury in this work &mdash; it's the mechanism.</p></div>
    </div>
  </div>
</section>

<section class="quote veil-ink">
  <div class="wrap rv">
    <p class="l1">Inspiring growth while empowering change.</p>
    <p class="l2">One day and one step at a time.</p>
  </div>
</section>
"""

naomi += pager([
    ("Chapter 04", "Connect",
     "Book a call, send a message, or join the community.", "connect.html"),
    ("Chapter 02", "The Butterfly Effect",
     "The methodology Naomi built from all of it.", "butterfly-effect.html"),
])

# ============================== CONNECT ======================
connect = """
<section class="phero">
  <div class="wrap">
    <p class="crumb rv"><a href="index.html">Home</a> &nbsp;/&nbsp; Chapter 04</p>
    <div class="rv">
      <span class="eyebrow">Connect</span>
      <h1>Ready for your <span class="mv">next chapter?</span></h1>
      <p class="sub">Start with a conversation about where you are and where you want to go. Thirty minutes, free, and no obligation at the end of it.</p>
    </div>
  </div>
</section>

<section class="pad veil" id="book">
  <div class="wrap">
    <div class="split" style="grid-template-columns:1.15fr .85fr">
      <div class="rv">
        <h2 class="sec">Book a discovery call</h2>
        <p style="color:var(--muted);margin-bottom:2rem">Tell us a little about what's going on. Naomi reads every message personally and will follow up within two business days.</p>
        <form data-demo data-ok="Thank you &mdash; your request is in. Naomi will follow up within two business days.">
          <div class="frow" style="margin-bottom:1.1rem">
            <input class="field" type="text" name="name" placeholder="Full name" autocomplete="name" required>
            <input class="field" type="email" name="email" placeholder="Email address" autocomplete="email" required>
          </div>
          <div class="frow" style="margin-bottom:1.1rem">
            <input class="field" type="tel" name="phone" placeholder="Phone (optional)" autocomplete="tel">
            <select class="field" name="area" style="flex:1 1 190px;width:auto">
              <option value="">What brings you here?</option>
              <option>Spiritual growth</option>
              <option>Emotional healing</option>
              <option>Professional development</option>
              <option>Not sure yet</option>
            </select>
          </div>
          <div class="fgroup">
            <textarea class="field" name="message" placeholder="What would you like to work on?"></textarea>
          </div>
          <button class="btn btn-clay" type="submit">Request my discovery call <span class="arw">&rarr;</span></button>
          <p class="formnote"></p>
        </form>
      </div>

      <div class="rv">
        <div class="darkcard">
          <div class="ring"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h3l1.5 4-2 1.5a12 12 0 0 0 6 6L15 13.5 19 15v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 6.2 2 2 0 0 1 5 4Z"/></svg></div>
          <h3>Prefer to talk?</h3>
          <p>Reach out directly &mdash; sometimes a conversation is simply faster than a form.</p>
          <ul style="margin-top:1.6rem">
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 4h3l1.5 4-2 1.5a12 12 0 0 0 6 6L15 13.5 19 15v3a2 2 0 0 1-2.2 2A16 16 0 0 1 4 6.2 2 2 0 0 1 5 4Z"/></svg> <a href="tel:+16785809648">(678) 580-9648</a></li>
            <li><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="m2.5 7.5 9.5 6 9.5-6"/></svg> <a href="mailto:info@narucoaching.com">info@narucoaching.com</a></li>
          </ul>
          <p style="margin-top:1.6rem;font-size:.85rem;opacity:.7">Response within two business days.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad veil-2" id="newsletter">
  <div class="wrap">
    <div class="split" style="grid-template-columns:1.1fr .9fr;align-items:center">
      <div class="rv">
        <span class="eyebrow">Stay connected</span>
        <h2 class="sec" style="margin-top:.8rem">Not ready <em class="it mv">just yet?</em></h2>
        <p style="color:var(--muted);margin-bottom:1.8rem">Join the NaRu community for inspiration, practical tools, and resources that support your journey &mdash; whenever you're ready to begin.</p>
        <form data-demo data-ok="Welcome to the NaRu community &mdash; check your inbox.">
          <div class="frow">
            <input class="field" type="text" name="first" placeholder="First name" autocomplete="given-name" required>
            <input class="field" type="email" name="email" placeholder="Email address" autocomplete="email" required>
          </div>
          <button class="btn btn-ink" style="margin-top:.9rem" type="submit">Join the community <span class="arw">&rarr;</span></button>
          <p class="formnote"></p>
        </form>
      </div>
      <div class="rv">
        <div class="darkcard">
          <div class="ring"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2.5" y="5" width="19" height="14" rx="3"/><path d="m2.5 7.5 9.5 6 9.5-6"/></svg></div>
          <h3>What lands in your inbox</h3>
          <ul>
            <li>{c} Practical tools you can use this week</li>
            <li>{c} Exclusive resources and guides</li>
            <li>{c} Honest encouragement, never spam</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pad veil">
  <div class="wrap" style="max-width:860px">
    <div class="sec-head rv"><span class="eyebrow">Before you ask</span><h2 class="sec" style="margin-top:.8rem">Common questions</h2></div>
    <div class="faq rv">
      <details open><summary>What happens on a discovery call?</summary><p>We talk. You describe what's going on, Naomi asks questions, and together you work out whether coaching is the right fit right now. There's no pitch at the end &mdash; if it isn't a fit, she'll tell you that plainly.</p></details>
      <details><summary>How long does coaching take?</summary><p>It depends entirely on what you're working through. Some people come for a focused season of eight to twelve weeks around a specific transition; others stay longer. You'll never be locked into something that isn't serving you.</p></details>
      <details><summary>Is this therapy?</summary><p>No. Coaching is forward-facing and action-oriented; therapy treats mental health conditions and processes the past clinically. The two work well alongside each other, and Naomi will say so if what you're describing calls for a licensed clinician.</p></details>
      <details><summary>Do you work with organizations?</summary><p>Yes. Leadership development and HR consulting are part of the practice. Reach out through the form above with a note about your team and what you're trying to move.</p></details>
      <details><summary>Are sessions in person or remote?</summary><p>Both. Most clients meet remotely by video, which keeps scheduling flexible. In-person sessions are available depending on location.</p></details>
    </div>
  </div>
</section>

<section class="quote veil-ink">
  <div class="wrap rv">
    <p class="l1">One small shift is all it takes to begin.</p>
    <p class="l2">The rest follows from there.</p>
  </div>
</section>
""".replace("{c}", CHECK)

connect += pager([
    ("Chapter 01", "Coaching",
     "The three areas we work in and what a session looks like.", "coaching.html"),
    ("Back to the start", "Home",
     "Return to the beginning of the journey.", "index.html"),
])

# ============================== BUILD ========================
page("index.html", "NaRu Empowerment Life Coach Group — Small Shifts. Big Transformation.",
     "Transformational coaching for greater clarity, confidence, alignment, and professional action.",
     home)

page("coaching.html", "Coaching — NaRu Empowerment Life Coach Group",
     "Spiritual growth, emotional healing, and professional development coaching with NaRu Empowerment.",
     coaching)

# The one page that carries the animated metamorphosis: larva to
# butterfly, completed by the bottom of the page.
page("butterfly-effect.html", "The Butterfly Effect Methodology — NaRu Empowerment",
     "Cocoon, Transform, Rise — the three movements of the Butterfly Effect Methodology.",
     method, live=True)

page("naomi.html", "Meet Naomi R. Wiley — NaRu Empowerment",
     "Twenty years of leadership, service, and real-life experience behind NaRu Empowerment.",
     naomi)

page("connect.html", "Connect — NaRu Empowerment Life Coach Group",
     "Book a discovery call, send a message, or join the NaRu community.",
     connect)
