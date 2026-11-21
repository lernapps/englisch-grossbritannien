# Figures of chapter 3 "London" (k3): scenes, time line of the Romans, schematic maps. Loaded by make_images.py with the same helpers.
def _floor(w=640, h=340, fy=262):
    return (f'  <rect y="{fy}" width="{w}" height="{h - fy}" fill="#cfcfcf"/>\n'
            f'  <rect width="{w}" height="{fy}" fill="#efe7d3"/>\n')

def _bricks(x, y, w, h, rows=5):
    b = rect(x, y, w, h, "#c9b79c", sw=3, rx=4)
    rh = h / rows
    for r in range(1, rows):
        b += f'  <path d="M{x} {y + r * rh} H{x + w}" stroke="#7a6a52" stroke-width="2"/>\n'
    for r in range(rows):
        off = 0 if r % 2 == 0 else 26
        xx = x + 26 + off
        while xx < x + w - 4:
            b += f'  <path d="M{xx} {y + r * rh} V{y + (r + 1) * rh}" stroke="#7a6a52" stroke-width="2"/>\n'
            xx += 52
    return b

@image
def szene_london_roemer():
    b = _floor()
    b += _bricks(190, 120, 260, 142)
    b += rect(250, 40, 140, 52, "#fff", sw=3) + text(320, 74, "London", 24)
    b += kid("hill", 70, 110, .85) + kid("ellie", 470, 110, .85)
    return svg(640, 340, "Mr Hill und Ellie stehen vor einer alten Steinmauer unter einem Schild mit dem Wort London", b)

@image
def zeitstrahl_roemer():
    b = '  <path d="M30 110 H490" stroke="#333" stroke-width="5" stroke-linecap="round"/>\n'
    b += '  <path d="M484 98 L500 110 L484 122 Z" fill="#333"/>\n'
    # 43 | 47-50 | 122, spaced for reading (not to scale)
    b += f'  <circle cx="70" cy="110" r="11" fill="{BLUE}" stroke="#333" stroke-width="2"/>\n'
    b += text(70, 70, "43", 20, weight="bold") + text(70, 52, "Invasion", 16)
    b += f'  <rect x="190" y="99" width="70" height="22" rx="11" fill="{ORANGE}" stroke="#333" stroke-width="2"/>\n'
    b += text(225, 160, "47 bis 50", 20, weight="bold") + text(225, 182, "Londinium", 16)
    b += f'  <circle cx="420" cy="110" r="11" fill="{GREEN}" stroke="#333" stroke-width="2"/>\n'
    b += text(420, 70, "122", 20, weight="bold") + text(420, 52, "Hadrian’s Wall", 16)
    b += text(260, 214, "Jahre nach Christi Geburt (nicht maßstabsgerecht)", 16, fill="#555")
    return svg(520, 230, "Zeitstrahl mit drei Marken: 43, 47 bis 50 und 122", b)

def _gb_base():
    b = rect(40, 10, 400, 70, "#e8e2d2", stroke="#aaa", sw=2, rx=14) * 0
    # Scotland (north), Wales (west), England (own rough outline)
    b += '  <path d="M150 10 L330 10 L330 98 L150 98 Z" fill="#e6e0cf" stroke="#999" stroke-width="2" stroke-dasharray="6 5"/>\n'
    b += text(240, 60, "Schottland", 16, fill="#555")
    b += '  <path d="M120 215 L150 200 L160 255 L150 300 L110 305 L80 285 L95 250 Z" fill="#e6e0cf" stroke="#999" stroke-width="2" stroke-dasharray="6 5"/>\n'
    b += text(70, 250, "Wales", 16, fill="#555", anchor="middle")
    b += ('  <path d="M150 98 L330 98 L322 150 L345 200 L352 250 L400 275 L390 320 L330 340 L250 352 L170 350 L120 335 L110 305 '
          'L150 300 L160 255 L150 200 L170 170 L150 130 Z" fill="#d6e4c8" stroke="#555" stroke-width="3" stroke-linejoin="round"/>\n')
    b += text(250, 200, "England", 16, fill="#2f4f2f")
    return b

@image
def roemer_orte():
    b = _gb_base()
    # Hadrian's Wall across the north of England (east Wallsend to west Bowness-on-Solway)
    b += f'  <path d="M170 112 L318 118" stroke="{ORANGE}" stroke-width="7" stroke-linecap="round" fill="none"/>\n'
    b += text(245, 148, "Hadrian’s Wall", 16, weight="bold")
    for (x, y, t, dx) in ((190, 292, "Bath", -14), (345, 292, "London", 0)):
        b += f'  <circle cx="{x}" cy="{y}" r="9" fill="{BLUE}" stroke="#333" stroke-width="2"/>\n'
    b += text(182, 322, "Bath", 16, anchor="end", weight="bold") + text(364, 292, "London", 16, anchor="start", weight="bold")
    b += compass2()
    return svg(480, 370, "Schemakarte von England mit drei Orten der Römer", b)

def compass2():
    return ('  <g stroke="#333" stroke-width="2" fill="#333"><path d="M450 70 V42" fill="none"/><path d="M444 50 L450 38 L456 50 Z"/></g>\n'
            + text(450, 90, "N", 16, weight="bold"))

THAMES = "M-10 305 L110 292 L190 257 L250 202 L300 162 L380 167 L470 202 L530 214"
STOPS = {  # number: (x, y, name, label x, label y)
    1: (420, 138, "Tower of London", 410, 108),
    2: (462, 196, "Tower Bridge", 462, 250),
    3: (239, 258, "London Eye", 245, 304),
    4: (191, 206, "Big Ben", 191, 172),
    5: (95, 165, "Buckingham Palace", 95, 132),
    6: (300, 72, "British Museum", 300, 40),
}
def _london(names):
    b = f'  <path d="{THAMES}" fill="none" stroke="#9cc3e6" stroke-width="38" stroke-linejoin="round" stroke-linecap="round"/>\n'
    b += f'  <path d="{THAMES}" fill="none" stroke="#5b95c9" stroke-width="2" stroke-dasharray="2 10"/>\n'
    b += text(360, 208, "River Thames", 16, fill="#1f4e79", anchor="middle") * 0
    b += text(125, 322, "River Thames", 16, fill="#1f4e79")
    # Tower Bridge: two small towers across the river
    b += '  <g stroke="#333" stroke-width="2"><rect x="450" y="176" width="10" height="42" fill="#bdbdbd" transform="rotate(-12 455 197)"/><rect x="474" y="184" width="10" height="42" fill="#bdbdbd" transform="rotate(-12 479 205)"/></g>\n'
    for n, (x, y, name, lx, ly) in STOPS.items():
        b += f'  <circle cx="{x}" cy="{y}" r="15" fill="#fff" stroke="{ORANGE}" stroke-width="3"/>\n' + text(x, y + 6, str(n), 18, fill=ORANGE, weight="bold")
        if names: b += text(lx, ly, name, 16, weight="bold")
    b += ('  <g stroke="#333" stroke-width="2" fill="#333"><path d="M490 62 V34" fill="none"/><path d="M484 42 L490 30 L496 42 Z"/></g>\n' + text(490, 82, "N", 16, weight="bold"))
    return b

@image
def london_karte():
    return svg(520, 340, "Schemakarte von London mit der Themse und sechs Halten", _london(True))

@image
def london_karte_nummern():
    return svg(520, 340, "Schemakarte von London mit der Themse und sechs nummerierten Halten", _london(False))

@image
def szene_london_rundgang():
    b = _floor()
    b += '  <rect y="236" width="640" height="26" fill="#9cc3e6"/>\n'
    b += rect(60, 130, 80, 106, "#d9d0bb", sw=2) + rect(150, 100, 70, 136, "#cdbfa6", sw=2) + rect(440, 120, 90, 116, "#d9d0bb", sw=2) + rect(540, 150, 70, 86, "#cdbfa6", sw=2)
    b += kid("hill", 250, 110, .85) + kid("peter", 340, 120, .8) + kid("sophie", 420, 110, .85)
    return svg(640, 340, "Mr Hill, Peter und Sophie gehen an einem Fluss entlang, hinter ihnen stehen Häuser", b)

@image
def szene_familien():
    b = _floor()
    b += rect(220, 30, 200, 130, "#fff", sw=3)
    b += '  <path d="M250 150 V100 L320 62 L390 100 V150 Z" fill="#fbe9a6" stroke="#333" stroke-width="3"/>\n'
    for x in (285, 320, 355):
        b += f'  <circle cx="{x}" cy="118" r="10" fill="#f3d2b3" stroke="#333" stroke-width="2"/><path d="M{x - 11} 150 Q{x} 128 {x + 11} 150" fill="#d6e4f7" stroke="#333" stroke-width="2"/>\n'
    b += kid("amir", 60, 110, .85) + kid("ellie", 450, 110, .85)
    return svg(640, 340, "Amir und Ellie stehen neben einem Plakat mit einem Haus und mehreren Personen", b)
