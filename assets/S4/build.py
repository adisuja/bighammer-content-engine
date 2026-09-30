"""S4 chart generator (HD49 hand-drawn two-curve archetype). Geometry is computed, not hand-placed:
curve points, node dots, leader lines, call-outs and the crossing marker all come from the beziers."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
X0, Y0, YT = 60, 760, 40           # axis origin and top
def yv(pct): return Y0 - pct / 62 * (Y0 - YT)   # axis spans 0..62% of the week (no numeric ticks shown)

def cubic(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0],
            u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1])

# upkeep: starts at 53% (the Fivetran figure), stays high, then falls
UP = [((62, yv(53)), (200, yv(53)), (300, yv(50)), (400, yv(35))),
      ((400, yv(35)), (500, yv(20)), (620, yv(8)), (740, yv(6)))]
# value work: starts low (the other ~47% is mostly not strategic), rises
VW = [((62, yv(6)), (200, yv(8)), (300, yv(16)), (400, yv(28))),
      ((400, yv(28)), (500, yv(42)), (620, yv(54)), (740, yv(57)))]

def pt(curve, t):  # t in [0,1] over the whole 2-segment curve
    seg = 0 if t < .5 else 1
    return cubic(*curve[seg], (t - .5 * seg) * 2)

def d(curve):
    s = f"M{curve[0][0][0]:.1f} {curve[0][0][1]:.1f} "
    for (_, a, b, c) in curve:
        s += f"C{a[0]:.1f} {a[1]:.1f}, {b[0]:.1f} {b[1]:.1f}, {c[0]:.1f} {c[1]:.1f} "
    return s

# crossing
best = None
for i in range(2001):
    t = i / 2000
    a, b = pt(UP, t), pt(VW, t)
    if best is None or abs(a[1] - b[1]) < best[0]:
        best = (abs(a[1] - b[1]), a)
CX, CY = best[1]

NODES = [  # (curve, t, label, chip_dy, chip_dx)
    (UP, .10, "Failed jobs", -70, 30), (UP, .30, "Reruns", -70, 40), (UP, .56, "Schema breaks", 48, 30), (UP, .80, "Manual checks", 48, -20),
    (VW, .16, "Design", -74, 10), (VW, .36, "Business logic", 56, 20), (VW, .66, "Data products", -74, -60), (VW, .88, "AI ready data", -74, -80),
]
MAG, VIO = "#E0006B", "#5600EF"
g_nodes, g_leads, g_chips = [], [], []
for curve, t, lab, dy, dx in NODES:
    col = MAG if curve is UP else VIO
    n = (NODES.index((curve, t, lab, dy, dx)) % 4) + 1
    x, y = pt(curve, t)
    w = 44 + len(lab) * 10.2
    cx, cy = x + dx - w / 2, y + dy - (21 if dy < 0 else 0)
    cx = max(80, min(cx, 960 - w))
    g_nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#fff" stroke="{col}" stroke-width="4"/>')
    ly = cy + 42 if dy < 0 else cy
    g_leads.append(f'<path d="M{x:.1f} {y + (-11 if dy < 0 else 11):.1f} L{x:.1f} {ly:.1f}" stroke="{col}" stroke-width="2" stroke-dasharray="5 6"/>')
    g_chips.append(f'<g transform="translate({cx:.1f},{cy:.1f})"><rect width="{w:.0f}" height="42" rx="8" fill="#fff" stroke="{col}" stroke-width="3" filter="url(#rough)"/>'
                   f'<circle cx="21" cy="21" r="12" fill="{col}"/><text x="21" y="27" fill="#fff" text-anchor="middle">{n}</text>'
                   f'<text x="42" y="27" fill="#141414">{lab}</text></g>')

svg = f'''<svg width="968" height="820" viewBox="0 0 968 820">
<defs>
  <filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".02" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter>
  <marker id="ah" markerUnits="userSpaceOnUse" markerWidth="46" markerHeight="46" refX="14" refY="15" orient="auto" viewBox="-2 -5 20 26"><path d="M1 2 L13 8 L1 14" fill="none" stroke="#141414" stroke-width="2.6" stroke-linecap="round"/></marker>
  <marker id="ahM" markerUnits="userSpaceOnUse" markerWidth="46" markerHeight="46" refX="14" refY="15" orient="auto" viewBox="-2 -5 20 26"><path d="M1 2 L13 8 L1 14" fill="none" stroke="{MAG}" stroke-width="2.6" stroke-linecap="round"/></marker>
  <marker id="ahV" markerUnits="userSpaceOnUse" markerWidth="46" markerHeight="46" refX="14" refY="15" orient="auto" viewBox="-2 -5 20 26"><path d="M1 2 L13 8 L1 14" fill="none" stroke="{VIO}" stroke-width="2.6" stroke-linecap="round"/></marker>
</defs>
<g filter="url(#rough)">
  <path d="M{X0} {Y0} L{X0} {YT}" stroke="#141414" stroke-width="3.5" fill="none" marker-end="url(#ah)"/>
  <path d="M{X0} {Y0} L760 {Y0}" stroke="#141414" stroke-width="3.5" fill="none" marker-end="url(#ah)"/>
  <path d="{d(UP)}" stroke="{MAG}" stroke-width="7" fill="none" stroke-linecap="round" marker-end="url(#ahM)"/>
  <path d="{d(VW)}" stroke="{VIO}" stroke-width="7" fill="none" stroke-linecap="round" marker-end="url(#ahV)"/>
  {"".join(g_leads)}
</g>
{"".join(g_nodes)}
<circle cx="{CX:.1f}" cy="{CY:.1f}" r="14" fill="#fff" stroke="#141414" stroke-width="4"/><circle cx="{CX:.1f}" cy="{CY:.1f}" r="5" fill="#141414"/>
<g class="lab" font-size="17">{"".join(g_chips)}</g>
<g font-family="Axiforma" font-weight="800">
  <text x="784" y="{yv(57) - 4:.0f}" fill="{VIO}" font-size="26">VALUE WORK</text>
  <g transform="translate(784,{yv(57) + 12:.0f})"><rect width="176" height="58" rx="8" fill="{VIO}"/><text x="88" y="25" fill="#fff" font-size="17" text-anchor="middle">CLOSER TO THE</text><text x="88" y="47" fill="#fff" font-size="17" text-anchor="middle">BUSINESS</text></g>
  <text x="784" y="{yv(6) - 20:.0f}" fill="{MAG}" font-size="26">THE UPKEEP</text>
  <g transform="translate(784,{yv(6) - 4:.0f})"><rect width="176" height="36" rx="8" fill="{MAG}"/><text x="88" y="25" fill="#fff" font-size="17" text-anchor="middle">AUTOMATED</text></g>
</g>
<text x="20" y="400" transform="rotate(-90 20 400)" text-anchor="middle" font-family="Axiforma" font-weight="800" font-size="22" fill="#141414">SHARE OF THE WEEK</text>
<text x="410" y="808" text-anchor="middle" font-family="Axiforma" font-weight="800" font-size="22" fill="#141414">MONTHS AFTER AUTOMATING</text>
<g font-family="Caveat" font-weight="700" fill="#2d2d33">
  <text x="80" y="{yv(53) + 70:.0f}" font-size="31">53% of</text>
  <text x="80" y="{yv(53) + 100:.0f}" font-size="31">the week today*</text>
  <path d="M88 {yv(53) + 44:.0f} q -6 -14 -4 -30" stroke="#2d2d33" stroke-width="2.4" fill="none"/>
  <text x="{CX + 62:.0f}" y="{CY - 2:.0f}" font-size="31" fill="#141414">where the job</text>
  <text x="{CX + 62:.0f}" y="{CY + 28:.0f}" font-size="31" fill="#141414">gets better</text>
  <path d="M{CX + 58:.0f} {CY - 8:.0f} q -18 -2 -30 4" stroke="#141414" stroke-width="2.4" fill="none"/>
  <text x="600" y="{yv(22):.0f}" font-size="30" fill="{VIO}">people move up,</text>
  <text x="600" y="{yv(22) + 30:.0f}" font-size="30" fill="{VIO}">not out</text>
</g>
</svg>'''

html = open(os.path.join(HERE, "image.html")).read()
a = html.index("<svg width=\"968\""); b = html.index("</svg>", a) + 6
html = html[:a] + svg + html[b:]
html = html.replace(".src{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:14px;color:#8a8a98}",
                    ".src{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:15px;color:#5E5E6A}")
html = html.replace(".share{position:absolute;left:56px;bottom:44px;", ".share{position:absolute;left:56px;bottom:52px;")
open(os.path.join(HERE, "image.html"), "w").write(html)
print("crossing", round(CX), round(CY))
