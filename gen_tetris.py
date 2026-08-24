#!/usr/bin/env python3
"""Generate an animated Tetris-style SVG of the tech stack for the profile README."""

W, H = 600, 430
BADGE_H = 32
ROW_STEP = 34
FLOOR_Y = 372          # top of the floor line
LOOP = 14              # seconds per loop

DARK_TEXT = "#0f172a"

# rows bottom-up: (label, badge_color, text_color, width)
rows = [
    [  # bottom row
        ("TypeScript", "#3178C6", "#fff", 100),
        ("React", "#61DAFB", DARK_TEXT, 64),
        ("Node.js", "#339933", "#fff", 78),
        ("PostgreSQL", "#4169E1", "#fff", 104),
        ("Docker", "#2496ED", "#fff", 70),
    ],
    [
        ("JavaScript", "#F7DF1E", DARK_TEXT, 100),
        ("Next.js", "#f8fafc", DARK_TEXT, 76),
        (".NET", "#512BD4", "#fff", 56),
        ("Supabase", "#3ECF8E", DARK_TEXT, 88),
        ("Cloudflare", "#F38020", "#fff", 100),
    ],
    [  # top row
        ("Python", "#3776AB", "#fff", 72),
        ("C#", "#68217A", "#fff", 46),
        ("Tailwind", "#06B6D4", "#fff", 86),
        ("Stripe", "#635BFF", "#fff", 70),
        ("Git", "#F05032", "#fff", 50),
    ],
]

row_x0 = [78, 72, 120]   # left offset per row (staggered, tetris-like)
GAP = 6

# build piece list with final positions
pieces = []
for r, row in enumerate(rows):
    x = row_x0[r]
    y = FLOOR_Y - BADGE_H - r * ROW_STEP
    for label, bg, fg, w in row:
        pieces.append({"label": label, "bg": bg, "fg": fg, "w": w, "x": x, "y": y, "row": r})
        x += w + GAP

# drop order: bottom row fills first, shuffled within each row for a tetris feel
order = []
shuffle = [2, 0, 4, 1, 3]
for r in range(3):
    base = r * 5
    order += [base + i for i in shuffle]

css = ["""
    .badge text { font-family: 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif;
                  font-size: 13px; font-weight: 700; }
    .hud { font-family: 'Courier New', monospace; font-weight: 700; fill: #64748b; }
"""]

for seq, idx in enumerate(order):
    p = pieces[idx]
    s = 3.0 + seq * 3.4          # % of loop when this piece starts falling
    land = s + 4.5               # % when it lands
    x, y = p["x"], p["y"]
    css.append(f"""
    .p{idx} {{ animation: fall{idx} {LOOP}s steps(6, end) infinite; opacity: 0;
               transform: translate({x}px, -60px); }}
    @keyframes fall{idx} {{
      0%, {s - 0.4:.1f}% {{ opacity: 0; transform: translate({x}px, -60px); }}
      {s:.1f}% {{ opacity: 1; transform: translate({x}px, -60px); }}
      {land:.1f}%, 91% {{ opacity: 1; transform: translate({x}px, {y}px); }}
      95%, 100% {{ opacity: 0; transform: translate({x}px, {y}px); }}
    }}""")

# line-clear style flash before the board resets
css.append("""
    .flash { animation: flash 14s linear infinite; opacity: 0; }
    @keyframes flash {
      0%, 88% { opacity: 0; }
      89.5% { opacity: 0.18; }
      91% { opacity: 0; }
      92.5% { opacity: 0.12; }
      94%, 100% { opacity: 0; }
    }""")

badges = []
for idx, p in enumerate(pieces):
    tx = p["w"] / 2
    badges.append(
        f'  <g class="badge p{idx}">\n'
        f'    <rect width="{p["w"]}" height="{BADGE_H}" rx="6" fill="{p["bg"]}"/>\n'
        f'    <text x="{tx}" y="21" text-anchor="middle" fill="{p["fg"]}">{p["label"]}</text>\n'
        f'  </g>'
    )

grid = []
for gx in range(60, W - 40, 34):
    for gy in range(60, FLOOR_Y, 34):
        grid.append(f'<circle cx="{gx}" cy="{gy}" r="1" fill="#1e293b"/>')

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <style>{''.join(css)}
  </style>

  <rect width="{W}" height="{H}" rx="12" fill="#0f172a"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="#334155"/>

  <!-- playfield well -->
  {''.join(grid)}
  <line x1="44" y1="48" x2="44" y2="{FLOOR_Y + 8}" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
  <line x1="{W - 44}" y1="48" x2="{W - 44}" y2="{FLOOR_Y + 8}" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
  <line x1="44" y1="{FLOOR_Y + 8}" x2="{W - 44}" y2="{FLOOR_Y + 8}" stroke="#334155" stroke-width="3" stroke-linecap="round"/>

  <text class="hud" x="46" y="30" font-size="13">TECH-STACK.EXE</text>
  <text class="hud" x="{W - 46}" y="30" font-size="13" text-anchor="end">LINES 3 &#183; SCORE &#8734;</text>

{chr(10).join(badges)}

  <rect class="flash" x="46" y="250" width="{W - 92}" height="122" fill="#f8fafc" rx="4"/>

  <text class="hud" x="{W / 2}" y="{H - 14}" font-size="11" text-anchor="middle" fill="#475569">the stack builds itself &#8212; every 14 seconds</text>
</svg>
"""

with open("assets/tetris-stack.svg", "w") as f:
    f.write(svg)
print(f"wrote assets/tetris-stack.svg ({len(svg)} bytes, {len(pieces)} pieces)")
