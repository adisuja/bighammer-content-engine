"""T6 carousel (HD40 surreal-cover + % breakdown archetype): Terry, AI agents vs data transformation."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../pipeline/brand.css">
<style>
body{background:#FBFAF7;color:#141414}
.wrap{position:relative;height:1350px;padding:130px 76px 120px;display:flex;flex-direction:column;justify-content:center}
.logo{top:56px;right:64px}
.big{font-family:var(--display);font-weight:800;text-transform:uppercase;letter-spacing:-.03em;line-height:.92}
.num{display:inline-flex;align-items:center;justify-content:center;width:84px;height:84px;border-radius:14px;background:#00FF89;font-family:var(--display);font-weight:800;font-size:48px}
p{font-size:48px;line-height:1.36}
p b{font-weight:600}
.vis{height:300px;margin:6px -76px 34px;background:center/cover no-repeat;border-radius:0}
.src{position:absolute;left:76px;right:76px;bottom:52px;font-size:20px;color:#6b6b78}
.trust{margin-top:44px;font-size:40px!important;line-height:1.3}.trust b{font-family:var(--display);font-weight:800;color:#FE0079}.trust span{display:block;margin-top:8px;font-size:24px;color:#6b6b78}
</style></head><body data-h="1350"><div class="wrap">
<div class="logo"><img src="../../brand/assets/bighammer-logo-dark.svg"></div>
"""
S = []
S.append("""<style>.cov{position:absolute;inset:0;padding:150px 76px 0}.cov .t1{font-size:86px;max-width:820px}.cov .t2{font-size:86px;color:#5600EF;margin-top:10px;max-width:900px}
.cov .img{position:absolute;left:0;right:0;bottom:0;height:640px;background:url(cover.png) center 62%/cover}
.cov .img::before{content:"";position:absolute;left:0;right:0;top:0;height:140px;background:linear-gradient(#FBFAF7,rgba(251,250,247,0))}
.cov .id{position:absolute;left:76px;bottom:52px;display:flex;align-items:center;gap:16px;padding:10px 26px 10px 10px;border-radius:999px;background:rgba(255,255,255,.92);font-family:var(--alt);font-weight:700;font-size:28px}
.cov .id i{width:64px;height:64px;border-radius:50%;background:url(../../.private/avatars/terry/face.jpg) center/cover}</style>
<div class="cov"><div class="big t1">AI agents can move your data.</div><div class="big t2">Can they transform it?</div>
<div class="img"></div><div class="id"><i></i>Terry Dhariwal</div></div>""")
S.append("""<style>.s2 .big{font-size:104px}.s2 p{margin-top:56px}</style>
<div class="s2"><div class="big">What the benchmarks actually say</div>
<p>Everyone has a demo where an AI agent builds a pipeline in minutes.</p>
<p>The public benchmarks tell a <b>more useful story</b>: which part of the work is solved, and which part isn't yet.</p></div>""")
S.append("""<style>.s3 .big{font-size:96px}.bars{margin-top:60px;display:flex;flex-direction:column;gap:34px}
.bars div{display:flex;align-items:center;gap:24px}
.bars b{flex:none;width:230px;text-align:center;padding:14px 0;border-radius:10px;background:#00FF89;font-family:var(--display);font-weight:800;font-size:56px}
.bars span{font-family:var(--display);font-weight:800;font-size:50px;line-height:1.1;text-transform:uppercase;letter-spacing:-.01em}
.bars span small{display:block;font-family:var(--body);font-weight:400;font-size:30px;text-transform:none;letter-spacing:0;color:#4F4F5C;margin-top:6px}
.bars div.lo b{background:#FE0079;color:#fff}.note3{margin-top:44px;font-size:30px!important;line-height:1.4;color:#4F4F5C}.bars div.mid b{background:#BA99FF}</style>
<div class="s3"><div class="big">AI on data work, by the numbers</div>
<div class="bars">
<div><b>96%</b><span>Extract and load<small>moving data from source to target</small></span></div>
<div class="mid"><b>66%</b><span>dbt project tasks<small>best score, Spider 2.0-DBT</small></span></div>
<div class="lo"><b>33%</b><span>Full transformation<small>raw data to correct models, end to end</small></span></div>
</div><p class="note3">Two different benchmarks. Spider 2.0-DBT scores narrower dbt project tasks; ELT-Bench-Verified asks the agent to build the full transformation layer end to end.</p></div>
<div class="src">ELT-Bench-Verified, Mar 2026: one agent setup (Claude Sonnet 4.5 + SWE-agent), 96% / 32.51%. Spider 2.0-DBT leaderboard, best 65.6%.</div>""")
S.append("""<style>.s4 .num{margin-bottom:34px}.s4 .big{font-size:92px}.s4 p{margin-top:44px}</style>
<div class="s4"><span class="num">1</span><div class="big">Moving data is nearly solved</div>
<div class="vis" style="background-image:url(cubes.png)"></div><p>In the ELT-Bench paper, extract and load success rose from <b>37% to 96%</b> when the agent moved to a newer model.</p>
<p>One setup, one benchmark, but a clear signal: use agents here now.</p></div>
<div class="src">Source: ELT-Bench-Verified, arXiv 2603.29399</div>""")
S.append("""<style>.s5 .num{margin-bottom:34px}.s5 .big{font-size:92px}.s5 p{margin-top:44px}</style>
<div class="s5"><span class="num">2</span><div class="big">Meaning is the hard part</div>
<p>Transformation is where business rules live: what counts as revenue, which customer is active, how two systems reconcile.</p>
<p>Agents get it right about <b>one time in three</b>. That's progress. It isn't autopilot.</p><div class="vis" style="background-image:url(blobs.png);margin-top:40px"></div></div>""")
S.append("""<style>.s6 .num{margin-bottom:34px}.s6 .big{font-size:88px}
.rules{margin-top:50px;display:flex;flex-direction:column;gap:26px}
.rules div{border-radius:16px;background:#fff;border:3px solid #141414;padding:30px 32px;font-size:42px;line-height:1.3;box-shadow:6px 6px 0 #5600EF}
.rules b{font-family:var(--display);font-weight:800}</style>
<div class="s6"><span class="num">3</span><div class="big">So split the work</div><p class="trust">Only <b>33%</b> of developers say they trust AI accuracy.<span>Stack Overflow Developer Survey 2025</span></p>
<div class="rules">
<div><b>AI</b> for the repetitive, checkable steps</div>
<div><b>Fixed rules</b> wherever results must be predictable</div>
<div><b>People</b> own the business logic and review what ships</div>
</div></div>""")
S.append("""<style>.s7 .big{font-size:104px}.s7 .big span{color:#5600EF}.s7 p{margin-top:50px}</style>
<div class="s7"><div class="big">Use agents where they're <span>strong.</span></div>
<p>Keep human judgement where they're not. That's how you get the speed without shipping wrong numbers to the board.</p>
<p>Which part of your pipeline would you trust an agent with today?</p></div>""")
for i, body in enumerate(S, 1):
    open(os.path.join(HERE, f"slide-{i:02d}.html"), "w").write(HEAD + body + "</div></body></html>")
print(len(S))
