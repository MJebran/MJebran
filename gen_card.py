#!/usr/bin/env python3
"""Generate the About / At a Glance profile card SVG, matching the Tetris window style."""

W, H = 700, 288
BG, BORDER = "#0f172a", "#334155"
TEXT, DIM, MUTED = "#e2e8f0", "#94a3b8", "#64748b"
AMBER, EMERALD, BLUE, PURPLE, CYAN, RED, PINK = (
    "#F59E0B", "#34D399", "#60A5FA", "#A78BFA", "#22D3EE", "#F87171", "#F472B6")

# About prose: list of lines, each line a list of (text, color, bold) runs
about = [
    [("Software engineer and founder of ", TEXT, False), ("FireFly Stack LLC", AMBER, True), (" —", TEXT, False)],
    [("a Utah studio designing and building modern websites", TEXT, False)],
    [("and software for businesses.", TEXT, False)],
    [],
    [("My background bridges engineering and product,", TEXT, False)],
    [("with degrees across ", TEXT, False), ("software", EMERALD, True), (", ", TEXT, False),
     ("management", BLUE, True), (", and ", TEXT, False), ("biomedical", PURPLE, True)],
    [("engineering — technical depth plus business thinking.", TEXT, False)],
    [],
    [("Currently: ", MUTED, False), ("growing FireFly Stack, launching SaaS", TEXT, False)],
    [("products, and building ", TEXT, False), ("AI-powered applications", CYAN, True), (".", TEXT, False)],
]

glance = [
    ("Utah, USA", RED),
    ("Founder · FireFly Stack LLC", AMBER),
    ("B.S. Software Engineering", EMERALD),
    ("M.S. Engineering Management", BLUE),
    ("B.S. Biomedical Engineering", PURPLE),
    ("SaaS · AI apps · client work", CYAN),
    ("Hiking · cinema · gym", PINK),
]

parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <style>
    text {{ font-family: 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; }}
    .hud {{ font-family: 'Courier New', monospace; font-weight: 700; }}
    .cursor {{ animation: blink 1.2s steps(1) infinite; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}
  </style>

  <rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="{BORDER}"/>

  <!-- window chrome -->
  <circle cx="26" cy="24" r="5" fill="{RED}"/>
  <circle cx="44" cy="24" r="5" fill="{AMBER}"/>
  <circle cx="62" cy="24" r="5" fill="{EMERALD}"/>
  <text class="hud" x="{W / 2}" y="29" font-size="12" fill="{MUTED}" text-anchor="middle">ahmad@fireflystack:~$ whoami</text>
  <line x1="1" y1="42" x2="{W - 1}" y2="42" stroke="{BORDER}"/>

  <!-- section headers -->
  <text class="hud" x="32" y="74" font-size="13" fill="{AMBER}">&#9654; ABOUT</text>
  <rect x="32" y="82" width="46" height="2" rx="1" fill="{AMBER}"/>
  <text class="hud" x="472" y="74" font-size="13" fill="{CYAN}">&#9654; AT A GLANCE</text>
  <rect x="472" y="82" width="88" height="2" rx="1" fill="{CYAN}"/>

  <!-- divider -->
  <line x1="448" y1="60" x2="448" y2="{H - 24}" stroke="{BORDER}" stroke-dasharray="1 5" stroke-linecap="round"/>
''']

# about prose
y = 108
for line in about:
    if not line:
        y += 9
        continue
    runs = "".join(
        f'<tspan fill="{color}"{" font-weight=\"700\"" if bold else ""}>{txt}</tspan>'
        for txt, color, bold in line)
    parts.append(f'  <text x="32" y="{y}" font-size="13.5">{runs}</text>')
    y += 19

parts.append(f'  <text class="hud cursor" x="32" y="{y + 10}" font-size="13" fill="{EMERALD}">&#9608;</text>')

# glance rows with tetromino-style square bullets
y = 106
for label, color in glance:
    parts.append(f'''  <rect x="472" y="{y - 10}" width="11" height="11" rx="2.5" fill="{color}"/>
  <text x="494" y="{y}" font-size="13.5" fill="{TEXT}">{label}</text>''')
    y += 26

parts.append("</svg>")

svg = "\n".join(parts) + "\n"
with open("assets/profile-card.svg", "w") as f:
    f.write(svg)
print(f"wrote assets/profile-card.svg ({len(svg)} bytes)")
