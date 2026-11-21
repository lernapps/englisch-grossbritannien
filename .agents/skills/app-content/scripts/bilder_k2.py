# Figures of chapter 2 (britische-inseln): schema maps of the British Isles and of the south-west of England, scenes.
# Loaded by make_images.py via exec; the helpers svg, kid, text, rect and the decorator image are already there.
# All outlines are drawn here by hand, strongly simplified (schema maps, not to scale).

K2_SEA = "#dcebf5"
K2_COL = {"England": "#f3c9c9", "Scotland": "#c9dcf3", "Wales": "#cfe8c4", "Northern Ireland": "#fbe3a6", "Republic of Ireland": "#cde9e6"}
K2_POLY = {  # viewBox 520 x 400, north up; shared corners lie on the borders
    "Scotland": [(290, 175), (320, 160), (345, 150), (350, 125), (365, 100), (352, 75), (358, 45), (335, 25), (300, 30), (275, 50), (258, 72), (268, 100), (262, 128), (272, 150)],
    "England": [(290, 175), (320, 160), (345, 150), (362, 185), (378, 222), (395, 252), (402, 285), (395, 320), (360, 336), (325, 342), (290, 350), (262, 360), (240, 372), (215, 380), (212, 368), (228, 352), (255, 342), (285, 336), (310, 330), (308, 300), (300, 275), (300, 250), (290, 235), (285, 205)],
    "Wales": [(290, 235), (300, 250), (300, 275), (308, 300), (310, 330), (285, 322), (270, 306), (250, 306), (236, 292), (250, 276), (240, 258), (262, 242)],
    "Northern Ireland": [(125, 142), (150, 135), (185, 138), (198, 158), (190, 185), (172, 200), (150, 200), (135, 185), (130, 160)],
    "Republic of Ireland": [(130, 160), (135, 185), (150, 200), (172, 200), (190, 185), (195, 215), (192, 250), (175, 280), (145, 295), (110, 300), (80, 285), (68, 250), (75, 215), (70, 180), (85, 155), (105, 138), (125, 142)],
}
K2_CAP = {"London": (378, 298), "Edinburgh": (335, 135), "Cardiff": (295, 319), "Belfast": (182, 165), "Dublin": (194, 225)}

def k2_land(colours=True, uniform="#e9dfc4", sw=2.5):
    b = ""
    for n, pts in K2_POLY.items():
        d = "M" + " L".join(f"{x} {y}" for x, y in pts) + " Z"
        b += f'  <path d="{d}" fill="{K2_COL[n] if colours else uniform}" stroke="#555" stroke-width="{sw}" stroke-linejoin="round"/>\n'
    return b

def k2_dot(x, y, r=6):
    return f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#222" stroke="#fff" stroke-width="2"/>\n'

def k2_badge(x, y, ch):
    return (f'  <circle cx="{x}" cy="{y}" r="15" fill="#fff" stroke="{ORANGE}" stroke-width="3"/>\n'
            + text(x, y + 6, ch, 18, fill=ORANGE, weight="bold"))

def k2_sea(w=520, h=400):
    return f'  <rect width="{w}" height="{h}" fill="{K2_SEA}"/>\n'

@image
def inseln_karte_namen():
    """Names of the four parts of the UK, the Republic of Ireland and the five capitals."""
    b = k2_sea() + k2_land()
    for n, (x, y) in K2_CAP.items(): b += k2_dot(x, y)
    b += text(312, 88, "Scotland", 18, weight="bold") + text(345, 255, "England", 18, weight="bold")
    b += text(272, 268, "Wales", 16, weight="bold")
    b += text(150, 122, "Northern Ireland", 16, weight="bold")
    b += text(128, 240, "Republic of", 16, weight="bold") + text(128, 260, "Ireland", 16, weight="bold")
    b += text(358, 139, "Edinburgh", 16, "start") + text(410, 303, "London", 16, "start") + text(205, 170, "Belfast", 16, "start")
    b += text(204, 230, "Dublin", 16, "start") + text(278, 328, "Cardiff", 16, "end") + '  <path d="M281 324 L289 320" stroke="#222" stroke-width="2"/>\n'
    b += compass()
    return svg(520, 400, "Schemakarte der Britischen Inseln mit Namen", b)

@image
def inseln_karte_buchstaben():
    """Same map without names: letters A to E on the five areas, capitals as dots (for the exercises)."""
    b = k2_sea() + k2_land()
    for n, (x, y) in K2_CAP.items(): b += k2_dot(x, y)
    for ch, (x, y) in {"C": (318, 88), "A": (350, 245), "D": (271, 278), "B": (160, 170), "E": (128, 250)}.items():
        b += k2_badge(x, y, ch)
    b += compass()
    return svg(520, 400, "Schemakarte der Britischen Inseln mit Buchstaben", b)

@image
def region_karte_buchstaben():
    """Great Britain with three areas marked A, B, C; one colour for all land."""
    b = k2_sea() + k2_land(colours=False)
    for ch, (x, y) in {"B": (302, 196), "C": (272, 282), "A": (232, 362)}.items():
        b += k2_badge(x, y, ch)
    b += compass()
    return svg(520, 400, "Schemakarte von Great Britain mit drei markierten Gebieten", b)

@image
def cornwall_karte():
    """South-west of England: Cornwall (the peninsula), the rest of England, the two seas."""
    corn = [(72, 285), (95, 262), (130, 225), (170, 190), (215, 155), (255, 123), (268, 246), (240, 262), (195, 282), (150, 298), (95, 312), (70, 305)]
    rest = [(255, 123), (285, 85), (300, 40), (300, 0), (520, 0), (520, 215), (425, 232), (370, 218), (330, 226), (285, 240), (268, 246)]
    def poly(pts, fill): return '  <path d="M' + " L".join(f"{x} {y}" for x, y in pts) + f' Z" fill="{fill}" stroke="#555" stroke-width="2.5" stroke-linejoin="round"/>\n'
    b = k2_sea(520, 340) + poly(rest, K2_COL["England"]) + poly(corn, "#f7e0a8")
    b += text(185, 242, "Cornwall", 18, weight="bold") + text(410, 110, "England", 18, weight="bold")
    b += text(105, 135, "Atlantic Ocean", 16, fill="#2c5f8a") + text(375, 300, "English Channel", 16, fill="#2c5f8a")
    b += compass()
    return svg(520, 340, "Schemakarte der Südwestspitze Englands", b)

def k2_wall_map(x, y, s):
    """The map on the classroom wall: the five areas without names."""
    out = f'  <g transform="translate({x},{y}) scale({s}) translate(-60,-20)">\n' + k2_land(sw=3) + "  </g>\n"
    return out

@image
def szene_karte_klasse():
    b = '  <rect y="262" width="640" height="78" fill="#cfcfcf"/>\n  <rect width="640" height="262" fill="#efe7d3"/>\n'
    b += rect(180, 28, 190, 190, K2_SEA, sw=3, rx=4) + k2_wall_map(222, 50, .42)
    b += kid("hill", 50, 95, .9) + kid("amir", 400, 100, .85) + kid("sophie", 470, 100, .85) + kid("ellie", 540, 100, .85)
    return svg(640, 340, "Mr Hill hängt eine Karte auf, Sophie, Ellie und Amir schauen zu", b)

@image
def szene_cornwall():
    b = '  <rect y="262" width="640" height="78" fill="#c9b79a"/>\n  <rect width="640" height="262" fill="#f3ead6"/>\n'
    b += rect(60, 205, 100, 70, "#6a8fb5", sw=3) + rect(75, 190, 70, 18, "#6a8fb5", sw=3) + rect(540, 220, 80, 55, "#b55a5a", sw=3)
    b += kid("parker", 190, 100, .85) + kid("ellie", 320, 105, .85) + kid("peter", 440, 135, .72)
    b += '  <ellipse cx="500" cy="62" rx="34" ry="26" fill="#fff" stroke="#333" stroke-width="3"/>\n' + text(500, 76, "?", 34, weight="bold")
    return svg(640, 340, "Mrs Parker, Ellie und Peter in der Küche, daneben zwei Koffer, über Peter eine Sprechblase mit Fragezeichen", b)

@image
def stadt_land_bild():
    """Left a busy town street, right quiet fields, Ellie left and Sophie right."""
    b = '  <rect width="320" height="340" fill="#d8dde6"/>\n  <rect x="320" width="320" height="340" fill="#e2efd2"/>\n'
    for i, (x, h, c) in enumerate(((10, 180, "#b9a38a"), (80, 230, "#a6b4c8"), (150, 150, "#c9b0a0"), (220, 200, "#b4bca4"))):
        b += rect(x, 262 - h, 62, h, c, sw=2, rx=2)
        for r in range(int(h // 40)):
            b += f'  <rect x="{x + 10}" y="{262 - h + 12 + r * 40}" width="14" height="18" fill="#fff8d6" stroke="#666"/><rect x="{x + 36}" y="{262 - h + 12 + r * 40}" width="14" height="18" fill="#fff8d6" stroke="#666"/>\n'
    b += '  <rect y="262" width="320" height="78" fill="#8a8a8a"/><rect x="40" y="300" width="60" height="22" rx="6" fill="#d33" stroke="#333" stroke-width="2"/><rect x="150" y="300" width="60" height="22" rx="6" fill="#2c6fd8" stroke="#333" stroke-width="2"/>\n'
    b += '  <path d="M320 262 C380 190 440 180 500 230 C550 180 610 190 640 215 V262 Z" fill="#a9d18e" stroke="#4d8a3a" stroke-width="2"/>\n  <rect x="320" y="262" width="320" height="78" fill="#8fc272"/>\n'
    b += '  <path d="M320 300 H640" stroke="#6aa04f" stroke-width="3" stroke-dasharray="14 8"/>\n'
    b += '  <rect x="560" y="196" width="46" height="36" fill="#e9d8b8" stroke="#333" stroke-width="2"/><path d="M554 198 L583 172 L612 198 Z" fill="#b5501e" stroke="#333" stroke-width="2"/>\n'
    b += '  <rect x="372" y="226" width="12" height="40" fill="#7a5a35"/><circle cx="378" cy="214" r="26" fill="#4d9a3a" stroke="#2d6a22" stroke-width="2"/>\n'
    b += kid("ellie", 175, 120, .72) + kid("sophie", 455, 120, .72)
    return svg(640, 340, "Links eine volle Straße mit Häusern und Autos, rechts Felder und ein kleines Haus; Ellie links, Sophie rechts", b)
