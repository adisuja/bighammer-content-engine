"""Generate S6 carousel slides (AB34 dark tutorial archetype) -> slide-NN.html"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../pipeline/brand.css">
<style>
body{background:#121217;color:#F4F2FF}
body::before{content:"";position:absolute;inset:0;background:url(../../pipeline/speckle.svg) 0 0/1080px 1350px no-repeat;opacity:.18;filter:invert(1)}
.wrap{position:relative;height:1350px;padding:64px 72px 0}
.logo{top:70px;right:72px}
.id{display:flex;align-items:center;gap:18px}
.id .av{width:92px;height:92px;border-radius:50%;background:#e9e9ee url(../../brand/assets/photos/srinath-face.jpg) center/cover no-repeat;border:3px solid #5600EF}
.id b{display:block;font-family:var(--alt);font-weight:700;font-size:30px}
.id span{display:block;font-size:21px;color:#9a9aae;margin-top:2px}
h2{margin-top:48px;font-family:var(--display);font-weight:800;font-size:58px;line-height:1.16;letter-spacing:-.015em}
h2 mark{background:#5600EF;color:#fff;padding:0 10px;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
h2 .n{color:#00FF89}
p{margin-top:26px;font-size:35px;line-height:1.45;color:#D9D8E6}
p b{color:#fff}
ul{margin:22px 0 0 0;padding:0;list-style:none}
li{position:relative;padding-left:40px;margin-top:20px;font-size:34px;line-height:1.4;color:#D9D8E6}
li::before{content:"";position:absolute;left:0;top:16px;width:16px;height:16px;border-radius:4px;background:#00FF89}
li b{color:#fff}
.win{margin-top:30px;border-radius:18px;background:#1C1C24;border:1px solid rgba(255,255,255,.1);box-shadow:0 30px 60px -30px rgba(0,0,0,.8);overflow:hidden}
.win .bar{display:flex;align-items:center;gap:9px;padding:14px 18px;background:#24242E;border-bottom:1px solid rgba(255,255,255,.07)}
.win .bar i{width:13px;height:13px;border-radius:50%}
.win .bar span{margin-left:12px;font-family:var(--mono);font-size:17px;color:#9a9aae}
.win pre{margin:0;padding:30px 32px;font-family:var(--mono);font-size:28px;line-height:1.6;color:#E6E4F0;white-space:pre-wrap}
.k{color:#C9A7FF}.s{color:#FFB3D6}.c{color:#7A7A8E}.ok{color:#00FF89}.er{color:#FF5C8A}
.fix{margin-top:26px;display:flex;gap:16px;align-items:flex-start;border-radius:16px;border:1.5px solid rgba(0,255,137,.4);background:rgba(0,255,137,.07);padding:18px 22px}
.fix b{flex:none;font-family:var(--mono);font-weight:700;font-size:21px;letter-spacing:.12em;color:#00FF89;margin-top:6px}
.fix span{font-size:29px;line-height:1.4;color:#E6E4F0}
.fix code,li code,p code{font-family:var(--mono);font-size:.9em;color:#FFB3D6}
.pg{position:absolute;right:72px;bottom:54px;font-family:var(--mono);font-size:19px;letter-spacing:.14em;color:#6f6f84}
.swipe{position:absolute;left:72px;bottom:54px;font-family:var(--mono);font-size:19px;letter-spacing:.14em;color:#00FF89}
.tline{margin-top:40px;position:relative;padding-top:10px}
.tline .rail{position:relative;height:10px;border-radius:5px;background:linear-gradient(90deg,#3a3a4a 0%,#3a3a4a 48%,#5600EF 48%,#FE0079 100%)}
.tline .pts{display:grid;grid-template-columns:1fr 1fr 1fr;margin-top:18px;gap:14px}
.tline .pts div{border-radius:14px;background:rgba(255,255,255,.05);padding:16px 18px}
.tline .pts b{display:block;font-family:var(--mono);font-size:21px;color:#00FF89}
.tline .pts span{display:block;margin-top:6px;font-size:23px;line-height:1.3;color:#E6E4F0}
.chk{margin-top:34px;display:flex;flex-direction:column;gap:14px}
.chk > div{display:flex;align-items:center;gap:22px;border-radius:16px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);padding:18px 22px}
.chk .box{flex:none;width:40px;height:40px;border-radius:8px;border:3px solid #00FF89}
.chk .nm{flex:none;width:44px;font-family:var(--display);font-weight:800;font-size:34px;color:#8B5CFF}
.chk b{display:block;font-family:var(--alt);font-weight:700;font-size:30px;color:#fff}
.chk > div span{display:block;font-size:24px;color:#B9B8C8;margin-top:2px}
.flowd{margin-top:40px;display:grid;grid-template-columns:1fr 70px 1fr 70px 1fr;align-items:center}
.flowd .nd{border-radius:16px;padding:20px 16px;text-align:center;background:rgba(255,255,255,.05);border:1.5px solid rgba(255,255,255,.12);font-family:var(--alt);font-weight:700;font-size:25px}
.flowd .nd small{display:block;font-family:var(--body);font-weight:400;font-size:19px;color:#B9B8C8;margin-top:6px}
.flowd .ar{text-align:center;font-size:40px;color:#00FF89}
.flowd .stack{display:flex;flex-direction:column;gap:12px}
.map{margin-top:26px;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.1)}
.map > div{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:14px 22px;font-size:25px;color:#E6E4F0;border-top:1px solid rgba(255,255,255,.07)}
.map > div code{font-family:var(--mono);font-size:23px;color:#FFB3D6}
.map .mh{background:rgba(86,0,239,.25);border-top:none;font-family:var(--mono);font-weight:700;font-size:18px!important;letter-spacing:.12em;text-transform:uppercase;color:#C9A7FF}
.chk > div{padding:24px 24px!important}
.chk b{font-size:33px!important}
.take{position:absolute;left:72px;right:72px;bottom:118px;display:flex;align-items:center;gap:18px;border-top:2px solid rgba(139,92,255,.5);padding-top:26px;font-family:var(--display);font-weight:800;font-size:36px;line-height:1.2;color:#fff}
.take i{flex:none;font-style:normal;font-family:var(--mono);font-weight:700;font-size:18px;letter-spacing:.14em;color:#8B5CFF}
</style></head><body data-h="1350"><div class="wrap">
<div class="logo"><img src="../../brand/assets/bighammer-logo.svg"></div>
<div class="id"><span class="av"></span><div><b>Srinath Reddy - Founder &amp; CEO</b></div></div>
"""
TAIL = """{take}{swipe}</div></body></html>"""
WIN = '<div class="win"><div class="bar"><i style="background:#FF5F57"></i><i style="background:#FEBC2E"></i><i style="background:#28C840"></i><span>{t}</span></div><pre>{c}</pre></div>'

S = []
S.append(("""<h2>Moving Spark jobs to EMR or Dataproc? <mark>3 things break quietly</mark> that your tests won't catch.</h2>
<p>Plus the 5 checks I'd run before switching anything off.</p>""" + WIN.format(t="same query · two engines", c="""<span class="k">SELECT</span> <span class="k">CAST</span>(<span class="s">'abc'</span> <span class="k">AS INT</span>) <span class="k">AS</span> amount;

<span class="c">-- Databricks Runtime 15.4 cluster (ANSI off)</span>
<span class="ok">→ NULL</span>

<span class="c">-- Spark 4.0 on EMR 8.0 or Dataproc 3.0</span>
<span class="er">→ [CAST_INVALID_INPUT] job fails</span>"""), True))
S.append(("""<h2><span class="n">Why now.</span> The target platforms moved to Spark 4.0.</h2>
<ul>
<li><b>EMR 8.0</b> shipped Spark 4.0 in June 2026.</li>
<li><b>Dataproc image 3.0</b> went GA in July 2026.</li>
<li>Spark 4.0 turns <code>ANSI mode</code> on by default.</li>
<li>Databricks Runtime only did the same from <b>17.0</b>. Most older jobs ran with it off.</li>
</ul>
<div class="tline"><div class="rail"></div><div class="pts"><div><b>DBR before 17</b><span>ANSI off on clusters. Bad casts become NULL.</span></div><div><b>DBR 17 / Spark 4.0</b><span>ANSI on by default. Bad casts throw.</span></div><div><b>EMR 8 · DATAPROC 3</b><span>Spark 4.0 is where your jobs land.</span></div></div></div>
<p>So a job that "worked" for years can fail, or quietly change, on day one.</p>""", False))
S.append(("""<h2><span class="n">1.</span> ANSI mode throws where Spark used to shrug.</h2>
<p>Bad input used to become NULL, or silently wrap. Now it stops the job.</p>""" + WIN.format(t="spark 4.0", c="""<span class="k">SELECT</span> 2147483647 + 1;
<span class="c">-- ANSI off:</span> <span class="ok">-2147483648 (silent wrap)</span>
<span class="c">-- Spark 4.0:</span> <span class="er">[ARITHMETIC_OVERFLOW]</span>

<span class="k">SELECT</span> to_date(<span class="s">'15/10/2026'</span>, <span class="s">'yyyy-MM-dd'</span>);
<span class="c">-- ANSI off:</span> <span class="ok">NULL</span>
<span class="c">-- Spark 4.0:</span> <span class="er">[CANNOT_PARSE_TIMESTAMP]</span>""") + """<div class="fix"><b>FIX</b><span>Use <code>try_cast</code> and <code>try_add</code> where NULL was the intent, and set <code>spark.sql.ansi.enabled</code> explicitly per job.</span></div>""", False))
S.append(("""<h2><span class="n">2.</span> Time zones shift your dates.</h2>
<p>Timestamps default to <code>TIMESTAMP_LTZ</code>, read in the <b>session time zone</b>.</p>
""" + WIN.format(t="one event, two sessions", c="""event_ts = <span class="s">2026-10-15 02:30 UTC</span>

<span class="c">-- session time zone UTC</span>
to_date(event_ts)  <span class="ok">→ 2026-10-15</span>

<span class="c">-- session time zone America/New_York</span>
to_date(event_ts)  <span class="er">→ 2026-10-14</span>""") + """<p>Same row, different day. Daily totals move and nobody gets an error.</p><div class="fix"><b>FIX</b><span>Pin <code>spark.sql.session.timeZone</code> in every job, and compare one day of output across both engines.</span></div>""", False))
S.append(("""<h2><span class="n">3.</span> Some code only exists on Databricks.</h2>""" + WIN.format(t="grep before you migrate", c="""dbutils.widgets.get(<span class="s">"run_date"</span>)  <span class="c"># notebook only</span>
dbutils.fs.ls(<span class="s">"/mnt/raw"</span>)           <span class="c"># DBFS</span>
<span class="k">import</span> dlt                         <span class="c"># old module</span>
spark.table(<span class="s">"main.sales.orders"</span>)   <span class="c"># 3-part names</span>""") + """<div class="map"><div class="mh"><span>Databricks call</span><span>Portable replacement</span></div>
<div><code>dbutils.widgets</code><span>job parameters</span></div>
<div><code>dbutils.fs</code><span>plain cloud paths (s3://, gs://)</span></div>
<div><code>import dlt</code><span>plain jobs (pipelines need Spark 4.1+)</span></div>
<div><code>catalog.schema.table</code><span>your target catalog's names</span></div></div>
<div class="fix"><b>NOTE</b><span>Photon is different: it's an engine swap, not a code break. Expect speed changes, not failures.</span></div>""", False))
S.append(("""<h2>The <mark>parity checklist.</mark> Run it on every migrated job.</h2>
<div class="chk">
<div><span class="nm">1</span><div><b>Row and column counts</b><span>The fastest signal something is off</span></div></div>
<div><span class="nm">2</span><div><b>Schema</b><span>Same columns, same types</span></div></div>
<div><span class="nm">3</span><div><b>Null rates per column</b><span>Catches silent handling changes</span></div></div>
<div><span class="nm">4</span><div><b>Numeric aggregates</b><span>Sums, mins and maxes on key measures</span></div></div>
<div><span class="nm">5</span><div><b>Row-level compare</b><span>By business key, or by hash if there's no clean key</span></div></div>
</div>""", False))
S.append(("""<h2><span class="n">How to run it</span> without touching production.</h2>
<div class="flowd"><div class="stack"><div class="nd">Old job<small>Databricks</small></div><div class="nd">New job<small>EMR / Dataproc</small></div></div><div class="ar">→</div><div class="nd" style="border-color:rgba(0,255,137,.5)">5 checks<small>same cloned inputs</small></div><div class="ar">→</div><div class="nd" style="background:#5600EF;border-color:#5600EF">Sign-off<small style="color:#E6DCFF">then cut over in waves</small></div></div>
<ul>
<li>Run old and new side by side on <b>cloned data</b>.</li>
<li>Agree the checks and tolerances with the <b>business owner first</b>.</li>
<li>Cut over in <b>small groups</b> of jobs, never all at once.</li>
<li>Keep the comparison results. That's your <b>sign-off evidence</b>.</li>
</ul>
""", False))
S.append(("""<h2><span style="color:#FF3D98">Want the full playbook?</span> Assess, migrate, monitor.</h2>
<p>I'm walking through it live, with real numbers, then taking your questions.</p>
<div class="cta"><div class="ph"></div><div class="tx"><b>Reduce your Databricks costs by up to 75%</b><em>Thu 15 Oct · 12:00 PM ET · 5 PM UK</em></div></div>
<div class="btn">webinar.bighammerai.com</div>
<style>.cta{margin-top:34px;display:flex;gap:0;border-radius:22px;overflow:hidden;background:linear-gradient(135deg,#6A16FF,#3D00AD);min-height:330px}
.cta .ph{width:330px;flex:none;background:url(../../brand/assets/photos/srinath-ceo.png) center bottom/cover no-repeat;filter:grayscale(1)}
.cta .tx{padding:34px 30px;display:flex;flex-direction:column;gap:14px;justify-content:center}
.cta .lv{font-family:var(--mono);font-weight:700;font-size:18px;letter-spacing:.16em;color:#00FF89}
.cta b{font-family:var(--display);font-weight:800;font-size:38px;line-height:1.1}
.cta em{font-style:normal;font-size:23px;color:#E6DCFF}
.btn{margin-top:30px;text-align:center;border-radius:16px;background:#00FF89;color:#0D0D14;font-family:var(--display);font-weight:800;font-size:36px;padding:24px}</style>""", False))

TAKE = {1: "3 quiet breakers, 5 checks that catch them.", 2: "Same code. New defaults.", 3: "NULL used to hide bad data. Now it fails loudly.",
        6: "Agree tolerances up front. Keep the evidence after.",
        7: "Conversion is visible. Parity is where trust is won."}
for i, (body, swipe) in enumerate(S, 1):
    take = f'<div class="take">{TAKE[i]}</div>' if i in TAKE else ""
    html = HEAD + body + TAIL.format(n=i, take=take, swipe="")
    open(os.path.join(HERE, f"slide-{i:02d}.html"), "w").write(html)
print(len(S), "slides")
