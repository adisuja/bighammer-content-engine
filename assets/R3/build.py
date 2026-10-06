"""R3 carousel (AB17 fake-post comparison archetype): Richard, two mindsets."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../pipeline/brand.css">
<style>
body{background:#0B0B10;color:#F4F2FF}
body::before{content:"";position:absolute;inset:0;background:url(../../pipeline/speckle-lav.svg) 0 0/1080px 1350px no-repeat;opacity:.35}
.wrap{position:relative;height:1350px;padding:230px 80px 110px;display:flex;flex-direction:column;justify-content:center}
.logo{top:62px;right:72px}
.id{position:absolute;left:80px;top:120px;display:flex;align-items:center;gap:22px}
.id .av{width:104px;height:104px;border-radius:50%;background:url(../../.private/avatars/richard/face.jpg) center/cover}
.id b{font-family:var(--alt);font-weight:700;font-size:36px}
.lab{align-self:flex-start;display:inline-flex;align-items:center;gap:16px;margin-top:0;padding:14px 30px 14px 22px;border-radius:999px;font-family:var(--alt);font-weight:700;font-size:36px}
.lab i{width:18px;height:18px;border-radius:50%}
.w{background:rgba(254,0,121,.14);color:#FF6FB0}.w i{background:#FE0079}
.c{background:rgba(0,255,137,.12);color:#5CFFB1}.c i{background:#00FF89}
.t{margin-top:40px;font-family:var(--body);font-size:60px;line-height:1.34;color:#EDEBF7}
.t p+p{margin-top:40px}
.t b{color:#fff;font-weight:600}
.cover .t{margin-top:0;font-size:64px}
.cover .t b{font-family:var(--display);font-weight:800}
.stat{display:inline-block;font-family:var(--display);font-weight:800;color:#00FF89}
</style></head><body data-h="1350"><div class="wrap{cls}">
<div class="logo"><img src="../../brand/assets/bighammer-logo.svg"></div>
<div class="id"><span class="av"></span><b>Richard Lawrence</b></div>
"""
W = '<div class="lab w"><i></i>The Worried</div>'
C = '<div class="lab c"><i></i>The Curious</div>'
S = [
 (" cover", """<div class="t"><p>There are two kinds of data engineers meeting AI right now.</p><p><b>The Worried</b> and <b>The Curious</b>.</p><p>Both are smart. One is about to have a much better couple of years.</p><p>Which one are you?</p></div>"""),
 ("", W + """<div class="t"><p>The Worried see AI as a threat to the skills they spent years building.</p><p>That's understandable.</p><p>But it turns into resistance, and every conversation ends up being about what could go wrong.</p></div>"""),
 ("", C + """<div class="t"><p>The Curious ask a different question.</p><p><b>“How could this help me do more?”</b></p><p>Could it take the repetitive work off my plate, and give me time for the problems I actually enjoy?</p></div>"""),
 ("", W + """<div class="t"><p>They tried an AI tool once.</p><p>The output was almost right, but not quite.</p><p>So they decided it can't be trusted, and went back to doing everything by hand.</p></div>"""),
 ("", C + """<div class="t"><p>They don't trust it blindly either. Only <span class="stat">33%</span> of developers say they trust AI accuracy.*</p><p>So they check the output, keep their own judgement, and use it where it genuinely helps.</p></div><p style="position:absolute;left:80px;bottom:60px;font-size:24px;color:#8a8a9c">*Stack Overflow Developer Survey 2025</p>"""),
 ("", W + """<div class="t"><p>Their week is failed jobs, reruns and patching the pipeline that breaks every time a schema changes.</p><p>It's the job they know, so they protect it.</p></div>"""),
 ("", C + """<div class="t"><p>They hand the upkeep to automation.</p><p>Then they spend the time closer to the business: understanding what people are trying to achieve and asking better questions.</p></div>"""),
 ("", W + """<div class="t"><p>Their value stays tied to the tasks they do.</p><p>And tasks are exactly what automation is getting good at.</p></div>"""),
 ("", C + """<div class="t"><p>Their value grows with the problems they solve.</p><p>Their experience and domain knowledge end up counting for more, not less.</p></div>"""),
 (" cover", """<div class="t"><p>At BigHammer.ai, the second mindset is the one we most want to work with.</p><p>Automating the mundane work is where it starts. <b>Human judgement stays at the centre.</b></p><p>Which one sounds more like <b>your</b> team?</p></div>"""),
]
for i, (cls, body) in enumerate(S, 1):
    open(os.path.join(HERE, f"slide-{i:02d}.html"), "w").write(HEAD.replace("{cls}", cls) + body + "</div></body></html>")
print(len(S))
