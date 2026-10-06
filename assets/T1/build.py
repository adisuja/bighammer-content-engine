"""T1 carousel (AB33 dark numbered archetype): Terry, 'Your cost per job report is missing the jobs that cost the most'."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../pipeline/brand.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=block">
<style>
body{background:#0E0E13;color:#F4F2FF}
body::before{content:"";position:absolute;inset:0;background:url(../../pipeline/speckle-lav.svg) 0 0/1080px 1350px no-repeat;opacity:.3}
.wrap{position:relative;height:1350px;padding:120px 84px 110px;display:flex;flex-direction:column;justify-content:center}
.logo{top:60px;right:72px}
h2{font-family:var(--display);font-weight:800;font-size:78px;line-height:1.12;letter-spacing:-.02em}
h2 .n{display:inline-block;background:#5600EF;color:#fff;padding:0 14px;border-radius:6px;margin-right:12px}
.hl{background:#FE0079;color:#fff;padding:0 10px;border-radius:5px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.hv{background:#5600EF;color:#fff;padding:0 10px;border-radius:5px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
p{margin-top:44px;font-size:48px;line-height:1.38;color:#E6E4F0}
p b{color:#fff}
.box{margin-top:40px;background:#F7F5FF;color:#141414;border-radius:18px;padding:30px 34px;box-shadow:0 20px 40px -24px rgba(0,0,0,.8)}
.box div{display:flex;align-items:center;gap:18px;font-family:Caveat,cursive;font-weight:700;font-size:56px;line-height:1.1;padding:8px 0}
.box div i{flex:none;font-style:normal;background:#00FF89;color:#0D0D14;border-radius:7px;padding:0 12px;font-family:var(--display);font-weight:800;font-size:34px;line-height:52px}
.box code{font-family:var(--mono);font-size:36px;color:#5600EF}
.sig{position:absolute;right:84px;bottom:70px;font-family:Caveat,cursive;font-weight:700;font-size:44px;color:#8a8a9c}
.cmp{margin-top:40px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.cmp div{border-radius:18px;padding:30px 28px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.14)}
.cmp div.m{background:rgba(254,0,121,.14);border-color:rgba(254,0,121,.5)}
.cmp b{display:block;font-family:var(--display);font-weight:800;font-size:112px;letter-spacing:-.02em}
.cmp span{display:block;font-size:36px;color:#D9D8E6;margin-top:6px;line-height:1.3}
.src{position:absolute;left:84px;bottom:66px;font-size:22px;color:#8a8a9c;max-width:700px}
</style></head><body data-h="1350"><div class="wrap">
<div class="logo"><img src="../../brand/assets/bighammer-logo.svg"></div>
"""
S = []
S.append("""<style>.cov{}.cov .id{display:flex;align-items:center;gap:22px}
.cov .id i{width:120px;height:120px;border-radius:50%;background:url(../../.private/avatars/terry/face.jpg) center/cover}
.cov .id b{font-family:var(--alt);font-weight:700;font-size:40px}
.cov h1{margin-top:70px;font-family:var(--display);font-weight:800;font-size:96px;line-height:1.08;letter-spacing:-.025em}
.cov h1 u{text-decoration-thickness:7px;text-underline-offset:10px;text-decoration-color:#FE0079}
.cov .sub{margin-top:50px;font-size:46px;line-height:1.35;color:#D9D8E6}</style>
<div class="cov"><div class="id"><i></i><b>Terry Dhariwal</b></div>
<h1>Your <u>cost per job</u> report is <span class="hl">missing</span> the jobs that cost the most.</h1>
<div class="sub"><span class="hv">5 steps to find them</span><br>(straight from Databricks' own docs)</div></div>""")
S.append("""<h2>Why most cost per job reports leave the big ones out</h2>
<p>Databricks attributes cost to a job using the <b>job ID</b> in billing data.</p>
<p>Jobs that run on <span class="hl">All-Purpose clusters</span> don't carry one.</p>
<p>So Databricks' own cost-per-job queries exclude them. And All-Purpose is the priciest classic compute for a scheduled job.</p>""")
S.append("""<h2><span class="n">1.</span>Spot the gap</h2>
<p>In <b>system.billing.usage</b>, the job ID is only filled in for:</p>
<div class="box"><div><i>+</i>Jobs on job compute</div><div><i>+</i>Serverless jobs</div><div><i style="background:#FE0079;color:#fff">×</i>Jobs on All-Purpose clusters</div></div>
<p>If a big share of your spend has no job ID, this is usually why.</p>""")
S.append("""<h2><span class="n">2.</span>Price the gap</h2>
<p>Same work, different rate. AWS Premium list price per DBU:</p>
<div class="cmp"><div class="m"><b>$0.55</b><span>All-Purpose<br>Classic</span></div><div><b>$0.15</b><span>Jobs<br>Classic</span></div></div>
<p>That's <span class="hl">3.67x the DBU rate</span> for the same job. The cloud VMs cost the same either way.</p>
<div class="src">Source: Databricks list prices, AWS, US East, Sep 2026</div>""")
S.append("""<h2><span class="n">3.</span>Find the jobs</h2>
<div class="box"><div><i>1</i>List every scheduled job and its tasks</div><div><i>2</i><span>Flag tasks set to <code>existing_cluster_id</code></span></div><div><i>3</i>Those run on All-Purpose compute</div><div><i>4</i>Note each cluster's owner and tags</div></div>
<p>Most teams find a handful of them. They're usually old, busy and nobody's favourite.</p>""")
S.append("""<h2><span class="n">4.</span>Move them</h2>
<p>Point scheduled work at <b>job compute</b> or <b>serverless jobs</b>.</p>
<div class="box"><div><i>+</i>Every run gets a job ID</div><div><i>+</i>Cost per job becomes real</div><div><i>+</i>The rate per DBU drops</div></div>
<p>It's configuration, not a migration. Job clusters add start-up time, so use pools or serverless where that matters.</p>""")
S.append("""<h2><span class="n">5.</span>Report the rest honestly</h2>
<p>Some spend will still have no job: notebooks, shared clusters, ad hoc work.</p>
<p>Report it as a <span class="hv">visibility gap</span>. Give it an owner and a target.</p>
<p>Just never count it as savings. Untraced isn't the same as wasted.</p>""")
S.append("""<style>.ct .card{margin-top:10px;border-radius:26px;overflow:hidden;background:linear-gradient(135deg,#6A16FF,#3D00AD);position:relative;height:560px}
.ct .ph{position:absolute;right:-10px;bottom:0;width:420px;height:500px;background:url(../../brand/assets/photos/srinath-ceo.png) center bottom/contain no-repeat;filter:grayscale(1)}
.ct .tx{position:absolute;left:44px;top:46px;width:500px}
.ct .lv{font-family:var(--mono);font-weight:700;font-size:21px;letter-spacing:.16em;color:#00FF89}
.ct .tx b{display:block;margin-top:20px;font-family:var(--display);font-weight:800;font-size:52px;line-height:1.06}
.ct .tx span{display:block;margin-top:22px;font-size:28px;line-height:1.4;color:#E6DCFF}
.ct .nm{position:absolute;left:44px;bottom:40px;font-size:24px;color:#E6DCFF;line-height:1.35;width:430px}
.ct .btn{margin-top:30px;border-radius:18px;background:#00FF89;color:#0D0D14;text-align:center;font-family:var(--display);font-weight:800;font-size:44px;padding:28px}
.ct p{margin-top:28px;text-align:center;font-size:30px}</style>
<div class="ct"><h2>Want to see this on a real bill?</h2>
<div class="card" style="margin-top:36px"><div class="ph"></div><div class="tx"><b>Reduce your Databricks costs by up to 75%</b><span>Free live masterclass<br>Thu 15 Oct · 12:00 PM ET · 5 PM UK</span></div><div class="nm">Hosted by <b style="color:#fff">Srinath Reddy</b>,<br>founder and CEO of BigHammer.ai</div></div>
<div class="btn">webinar.bighammerai.com</div></div>""")
for i, body in enumerate(S, 1):
    open(os.path.join(HERE, f"slide-{i:02d}.html"), "w").write(HEAD + body + "</div></body></html>")
print(len(S))
