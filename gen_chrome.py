#!/usr/bin/env python3
"""Generate hero banner, link pills, and footer SVGs — same terminal design as the cards."""

BG, BORDER = "#0f172a", "#334155"
TEXT, BRIGHT, MUTED, DIM = "#e2e8f0", "#f8fafc", "#64748b", "#475569"
AMBER, EMERALD, BLUE, PURPLE, CYAN, RED, PINK = (
    "#F59E0B", "#34D399", "#60A5FA", "#A78BFA", "#22D3EE", "#F87171", "#F472B6")
SQUARES = [RED, AMBER, EMERALD, BLUE, PURPLE, CYAN, PINK]

STYLE = f"""
  <style>
    text {{ font-family: 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; }}
    .hud {{ font-family: 'Courier New', monospace; font-weight: 700; }}
    .cursor {{ animation: blink 1.2s steps(1) infinite; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
    .fade {{ opacity: 0; animation: fadein 0.6s ease-out forwards; }}
    @keyframes fadein {{ to {{ opacity: 1; }} }}
  </style>"""


def chrome(w, title):
    return f'''
  <circle cx="26" cy="24" r="5" fill="{RED}"/>
  <circle cx="44" cy="24" r="5" fill="{AMBER}"/>
  <circle cx="62" cy="24" r="5" fill="{EMERALD}"/>
  <text class="hud" x="{w / 2}" y="29" font-size="12" fill="{MUTED}" text-anchor="middle">{title}</text>
  <line x1="1" y1="42" x2="{w - 1}" y2="42" stroke="{BORDER}"/>'''


def frame(w, h):
    return f'''
  <rect width="{w}" height="{h}" rx="12" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="none" stroke="{BORDER}"/>'''


def squares_strip(x, y):
    out = []
    for i, c in enumerate(SQUARES):
        out.append(f'<rect x="{x + i * 16}" y="{y}" width="10" height="10" rx="2.5" fill="{c}"/>')
    return "".join(out)


def write(path, svg):
    with open(path, "w") as f:
        f.write(svg)
    print(f"wrote {path} ({len(svg)} bytes)")


# ---------------- hero ----------------
W, H = 700, 216
grid = []
for gx in range(60, W - 40, 34):
    for gy in range(64, H - 20, 34):
        grid.append(f'<circle cx="{gx}" cy="{gy}" r="1" fill="#1e293b"/>')

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{STYLE}
{frame(W, H)}
  {''.join(grid)}{chrome(W, 'ahmad@fireflystack:~$ ./welcome.sh')}
  <text class="hud fade" x="32" y="80" font-size="12" fill="{MUTED}">&gt; hello, world &#8212; glad you&#8217;re here</text>
  <text class="fade" style="animation-delay:.25s" x="32" y="122" font-size="32" font-weight="700" fill="{BRIGHT}">Ahmad Mustafa Jebran</text>
  <text class="fade" style="animation-delay:.5s" x="32" y="152" font-size="15">
    <tspan fill="{TEXT}">Software Engineer</tspan><tspan fill="{DIM}"> &#183; </tspan><tspan fill="{TEXT}">Founder @ </tspan><tspan fill="{AMBER}" font-weight="700">FireFly Stack LLC</tspan>
  </text>
  <text class="hud fade" style="animation-delay:.75s" x="32" y="184" font-size="12" fill="{MUTED}">utah, usa</text>
  <text class="hud cursor" x="108" y="184" font-size="12" fill="{EMERALD}">&#9608;</text>
  <g class="fade" style="animation-delay:1s">{squares_strip(W - 32 - 7 * 16 + 6, H - 42)}</g>
</svg>
'''
write("assets/hero.svg", hero)

# ---------------- link pills ----------------
pills = [
    ("link-portfolio.svg", "PORTFOLIO", EMERALD, 128),
    ("link-firefly.svg", "FIREFLY STACK", AMBER, 156),
    ("link-linkedin.svg", "LINKEDIN", BLUE, 118),
    ("link-email.svg", "EMAIL", RED, 96),
]
for fname, label, accent, w in pills:
    h = 40
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{STYLE}
  <rect width="{w}" height="{h}" rx="10" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10" fill="none" stroke="{BORDER}"/>
  <rect x="16" y="{h / 2 - 5.5}" width="11" height="11" rx="2.5" fill="{accent}"/>
  <text class="hud" x="38" y="{h / 2 + 4.5}" font-size="12" fill="{TEXT}">{label}</text>
</svg>
'''
    write(f"assets/{fname}", svg)

# ---------------- footer ----------------
W, H = 700, 132
footer = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{STYLE}
{frame(W, H)}
  <text class="hud" x="32" y="42" font-size="12" fill="{MUTED}">ahmad@fireflystack:~$ echo "$MISSION"</text>
  <text x="32" y="76" font-size="15.5" fill="{BRIGHT}"><tspan fill="{EMERALD}">&#8220;</tspan>Building software that helps businesses grow &#8212; one project at a time.<tspan fill="{EMERALD}">&#8221;</tspan></text>
  <text class="hud" x="32" y="106" font-size="11" fill="{DIM}">[process completed &#8212; thanks for scrolling]</text>
  <text class="hud cursor" x="310" y="106" font-size="11" fill="{EMERALD}">&#9608;</text>
  {squares_strip(W - 32 - 7 * 16 + 6, H - 38)}
</svg>
'''
write("assets/footer.svg", footer)
