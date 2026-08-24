#!/usr/bin/env python3
"""Generate the Tech Stack card SVG, matching the About/Glance terminal style."""

W, H = 700, 322
BG, BORDER = "#0f172a", "#334155"
TEXT, MUTED = "#e2e8f0", "#64748b"
AMBER, EMERALD, BLUE, PURPLE, CYAN, RED = "#F59E0B", "#34D399", "#60A5FA", "#A78BFA", "#22D3EE", "#F87171"
DARK = "#0f172a"

# (section label, accent color, [(name, pill color, text color, width)])
groups = [
    ("LANGUAGES", AMBER, [
        ("TypeScript", "#3178C6", "#fff", 88),
        ("JavaScript", "#F7DF1E", DARK, 88),
        ("Python", "#3776AB", "#fff", 62),
        ("C#", "#68217A", "#fff", 40),
    ]),
    ("FRONTEND", CYAN, [
        ("React", "#61DAFB", DARK, 56),
        ("Next.js", "#f8fafc", DARK, 66),
        ("Tailwind CSS", "#06B6D4", "#fff", 102),
    ]),
    ("BACKEND &amp; DATA", EMERALD, [
        (".NET", "#512BD4", "#fff", 48),
        ("Node.js", "#339933", "#fff", 68),
        ("PostgreSQL", "#4169E1", "#fff", 88),
        ("Supabase", "#3ECF8E", DARK, 78),
        ("Stripe", "#635BFF", "#fff", 58),
    ]),
    ("DEVOPS &amp; CLOUD", BLUE, [
        ("Docker", "#2496ED", "#fff", 62),
        ("Kubernetes", "#326CE5", "#fff", 88),
        ("Cloudflare", "#F38020", "#fff", 88),
        ("Linux", "#FCC624", DARK, 54),
        ("Git", "#F05032", "#fff", 40),
        ("GitHub Actions", "#2088FF", "#fff", 114),
    ]),
    ("TOOLS", PURPLE, [
        ("VS Code", "#0078D4", "#fff", 68),
        ("Claude Code", "#D97757", "#fff", 96),
        ("Cursor", "#f8fafc", DARK, 62),
    ]),
]

parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <style>
    text {{ font-family: 'Segoe UI', Ubuntu, Helvetica, Arial, sans-serif; }}
    .hud {{ font-family: 'Courier New', monospace; font-weight: 700; }}
  </style>

  <rect width="{W}" height="{H}" rx="12" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="{BORDER}"/>

  <!-- window chrome -->
  <circle cx="26" cy="24" r="5" fill="{RED}"/>
  <circle cx="44" cy="24" r="5" fill="{AMBER}"/>
  <circle cx="62" cy="24" r="5" fill="{EMERALD}"/>
  <text class="hud" x="{W / 2}" y="29" font-size="12" fill="{MUTED}" text-anchor="middle">ahmad@fireflystack:~$ ls ./tech-stack</text>
  <line x1="1" y1="42" x2="{W - 1}" y2="42" stroke="{BORDER}"/>
''']

y = 78          # baseline-ish anchor for first row
ROW = 48
PILL_H = 26
for label, accent, pills in groups:
    parts.append(f'  <rect x="32" y="{y + 2}" width="4" height="{PILL_H - 4}" rx="2" fill="{accent}"/>')
    parts.append(f'  <text class="hud" x="46" y="{y + PILL_H / 2 + 4}" font-size="11" fill="{accent}">{label}</text>')
    x = 178
    for name, bg, fg, w in pills:
        parts.append(f'''  <g>
    <rect x="{x}" y="{y}" width="{w}" height="{PILL_H}" rx="6" fill="{bg}"/>
    <text x="{x + w / 2}" y="{y + PILL_H / 2 + 4.5}" font-size="12" font-weight="700" fill="{fg}" text-anchor="middle">{name}</text>
  </g>''')
        x += w + 8
    y += ROW

parts.append(f'  <text class="hud" x="{W / 2}" y="{H - 16}" font-size="11" fill="#475569" text-anchor="middle">21 items &#183; 0 regrets</text>')
parts.append("</svg>")

svg = "\n".join(parts) + "\n"
with open("assets/stack-card.svg", "w") as f:
    f.write(svg)
print(f"wrote assets/stack-card.svg ({len(svg)} bytes)")
