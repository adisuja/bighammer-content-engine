"""R6 carousel (AV41 dark glass archetype): Richard, 'Please don't come to our masterclass if...'"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="../../pipeline/brand.css">
<style>
body{background:radial-gradient(60% 45% at 50% 30%,rgba(139,92,255,.20),transparent 70%),radial-gradient(120% 90% at 50% 40%,#1a1a24 0%,#0c0c12 60%,#060609 100%);color:#F4F2FF}
.wrap{position:relative;height:1350px;padding:0 80px}
.logo{top:60px;right:72px}
.icon{position:absolute;left:50%;top:150px;width:470px;height:470px;transform:translateX(-50%);background:center/contain no-repeat;filter:drop-shadow(0 40px 60px rgba(86,0,239,.35))}
.row{position:absolute;left:80px;right:80px;top:680px;display:flex;align-items:center;gap:26px}
.num{flex:none;width:92px;height:92px;border-radius:18px;background:rgba(255,255,255,.08);border:1.5px solid rgba(255,255,255,.18);display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:48px}
.row h2{font-family:var(--body);font-weight:400;font-size:52px;line-height:1.12;letter-spacing:-.01em}
.row h2 b{font-weight:700}
.glass{position:absolute;left:80px;right:80px;top:900px;border-radius:20px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.12);padding:28px 32px;font-size:31px;line-height:1.42;color:#D9D8E6;box-shadow:inset 0 1px 0 rgba(255,255,255,.08)}
.bold{position:absolute;left:80px;right:80px;top:1130px;font-family:var(--alt);font-weight:700;font-size:38px;line-height:1.25;color:#fff}
.bold em{font-style:normal;color:#00FF89}
</style></head><body data-h="1350"><div class="wrap">
<div class="logo"><img src="../../brand/assets/bighammer-logo.svg"></div>
"""
def item(n, icon, title, glass, bold):
    return (f'<div class="icon" style="background-image:url({icon}.png)"></div>'
            f'<div class="row"><div class="num">{n}</div><h2>{title}</h2></div>'
            f'<div class="glass">{glass}</div><div class="bold">{bold}</div>')

S = []
S.append("""<style>.cv h1{position:absolute;left:80px;right:80px;top:330px;font-family:var(--body);font-weight:300;font-size:84px;line-height:1.06;letter-spacing:-.02em}
.cv h1 b{font-weight:700}.cv h1 em{font-style:normal;font-weight:700;color:#FF4FA3}
.cv .pill{position:absolute;left:80px;top:760px;max-width:600px;padding:18px 28px;font-family:var(--body)!important;letter-spacing:0!important;text-transform:none!important;border-radius:999px;background:rgba(255,255,255,.07);border:1.5px solid rgba(255,255,255,.14);font-size:28px;color:#D9D8E6}
.cv .who{position:absolute;left:80px;bottom:80px;display:flex;align-items:center;gap:20px}
.cv .who i{width:96px;height:96px;border-radius:50%;background:url(../../.private/avatars/richard/face.jpg) center/cover;border:3px solid #8B5CFF}
.cv .who b{display:block;font-family:var(--alt);font-weight:700;font-size:32px}
.cv .who span{display:block;font-size:24px;color:#9a9aae;margin-top:4px}
.cv .ghost{position:absolute;right:-60px;bottom:40px;width:520px;height:520px;background:url(megaphone.png) center/contain no-repeat;opacity:.9;transform:rotate(-8deg)}</style>
<div class="cv"><div class="ghost"></div><h1><b>Please don't come</b> to our masterclass on <em>15&nbsp;October</em> if any of these are true.</h1>
<div class="pill">An honest filter from someone who used to sell software.</div>
<div class="who"><i></i><div><b>Richard Lawrence</b></div></div></div>""")
S.append(item(1, "receipt", "Your platform bill is <b>small and flat.</b>",
  "If it hasn't moved in a year, you have better things to do on a Thursday.", "Come back when it <em>starts climbing.</em>"))
S.append(item(2, "tag", "Every cluster has <b>an owner tag and auto-termination.</b>",
  "And every job has a timeout. Those are the first fixes we'd suggest anyway.", "You've done <em>the hard part.</em>"))
S.append(item(3, "stopwatch", "You already know <b>your cost per job.</b>",
  "A 90-day baseline, every job with an owner, and failed runs costed on their own line.", "You're ahead of <em>most teams we meet.</em>"))
S.append(item(4, "megaphone", "You're hoping for <b>a product demo.</b>",
  "It's 30 minutes of framework and 15 minutes of your questions. We only mention BigHammer.ai in the last minute.", "Book a demo instead. <em>We won't mind.</em>"))
S.append("""<style>.fr h1{position:absolute;left:80px;right:80px;top:190px;font-family:var(--body);font-weight:300;font-size:82px;line-height:1.05;letter-spacing:-.02em}
.fr h1 b{font-weight:700}
.fr .list{position:absolute;left:80px;right:80px;top:480px;display:flex;flex-direction:column;gap:22px}
.fr .list > div{display:flex;align-items:center;gap:26px;border-radius:20px;background:rgba(255,255,255,.06);border:1.5px solid rgba(255,255,255,.12);padding:26px 30px;font-size:33px;line-height:1.3;color:#EDEBF7}
.fr .list span{flex:none;width:70px;height:70px;border-radius:16px;display:grid;place-items:center;background:rgba(139,92,255,.22);color:#C9B0FF;font-family:var(--display);font-weight:800;font-size:34px}
.fr .list b{color:#fff;font-weight:600}</style>
<div class="fr"><h1>Still here? <b>Then it's for you.</b></h1><div class="list">
<div><span>1</span><p><b>Data leaders</b> whose platform bill keeps climbing</p></div>
<div><span>2</span><p><b>Platform owners</b> with a renewal coming up</p></div>
<div><span>3</span><p><b>FinOps teams</b> asked to explain the spend</p></div>
<div><span>4</span><p><b>Engineering managers</b> planning a move to EMR or Dataproc</p></div>
</div></div>""")
S.append("""<style>.ct .card{position:absolute;left:80px;right:80px;top:170px;border-radius:28px;overflow:hidden;background:linear-gradient(135deg,#6A16FF,#3D00AD);height:640px}
.ct .ph{position:absolute;right:-20px;bottom:0;width:470px;height:560px;background:url(../../brand/assets/photos/srinath-ceo.png) center bottom/contain no-repeat;filter:grayscale(1) contrast(1.05)}
.ct .tx{position:absolute;left:44px;top:50px;width:470px}
.ct .lv{font-family:var(--mono);font-weight:700;font-size:21px;letter-spacing:.16em;color:#00FF89}
.ct h2{margin-top:22px;font-family:var(--display);font-weight:800;font-size:54px;line-height:1.05}
.ct .d{margin-top:26px;font-size:28px;line-height:1.4;color:#E6DCFF}
.ct .nm{position:absolute;left:44px;bottom:40px;font-size:24px;color:#E6DCFF;width:420px;line-height:1.35}
.ct .nm b{color:#fff;font-family:var(--alt)}
.ct .btn{position:absolute;left:80px;right:80px;top:850px;border-radius:20px;background:#00FF89;color:#0D0D14;text-align:center;font-family:var(--display);font-weight:800;font-size:44px;padding:30px}
.ct .sm{position:absolute;left:80px;right:80px;top:1010px;text-align:center;font-size:29px;color:#B9B8C8;line-height:1.4}</style>
<div class="ct"><div class="card"><div class="ph"></div><div class="tx"><h2>Reduce your Databricks costs by up to 75%</h2><div class="d">Free live masterclass<br>Thu 15 Oct · 12:00 PM ET<br>5 PM UK · 45 minutes</div></div>
<div class="nm">Hosted by <b>Srinath Reddy</b>,<br>founder and CEO of BigHammer.ai</div></div>
<div class="btn">webinar.bighammerai.com</div>
<div class="sm">Bring your hardest cost question.<br>The best three win a $50 Amazon gift card.</div></div>""")

for i, body in enumerate(S, 1):
    open(os.path.join(HERE, f"slide-{i:02d}.html"), "w").write(HEAD + body + "</div></body></html>")
print(len(S))
