# Figures of the pages alltagstexte and kleidung-einkaufen (chapter 1). Loaded by make_images.py with exec: the helpers
# svg, kid, text, rect and the decorator image are in scope; nothing is imported here.

def _g(x, y, s, body):
    return f'  <g transform="translate({x},{y}) scale({s})" stroke="#333" stroke-width="2" stroke-linejoin="round">{body}</g>\n'

# ---- clothes icons, drawn in a 70 x 60 box, feet on y = 60 ----
def _shirt(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<path d="M10 12 L24 4 Q30 12 36 4 L50 12 L60 30 L49 34 L45 24 L45 60 L15 60 L15 24 L11 34 L0 30 Z" fill="{col}"/>')
def _jumper(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<path d="M8 14 L24 4 Q30 12 36 4 L52 14 L64 52 L52 56 L45 32 L45 60 L15 60 L15 32 L8 56 L-4 52 Z" fill="{col}"/>'
              '<path d="M15 52 H45" fill="none" stroke-width="3"/>')
def _trousers(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<path d="M12 2 H48 L54 60 H34 L30 22 L26 60 H6 Z" fill="{col}"/><path d="M12 10 H48" fill="none"/>')
def _hat(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<ellipse cx="30" cy="52" rx="30" ry="8" fill="{col}"/><path d="M14 50 Q14 16 30 16 Q46 16 46 50 Z" fill="{col}"/>'
              '<path d="M14 42 H46" fill="none" stroke="#fff" stroke-width="5"/>')
def _cap(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<path d="M6 54 Q6 20 32 20 Q56 20 56 54 Z" fill="{col}"/><path d="M48 54 Q72 52 74 60 Q62 62 44 58 Z" fill="{col}"/>')
def _shoes(x, y, s, col):
    return _g(x, y - 60 * s, s, f'<path d="M0 34 H20 Q26 40 36 42 Q40 44 40 50 V60 H0 Z" fill="{col}"/>'
              f'<path d="M42 34 H62 Q68 40 78 42 Q82 44 82 50 V60 H42 Z" fill="{col}"/>')

def _tag(cx, y, price):
    return (f'  <path d="M{cx} {y - 6} V{y}" stroke="#333" stroke-width="2"/>\n' + rect(cx - 30, y, 60, 28, "#fff", sw=2, rx=4)
            + text(cx, y + 21, price, 18, weight="bold"))

# ---- four cards: sign, timetable, menu, flyer (A with labels, B without) ----
def _cards(labels, sign, timetable, menu, flyer):
    b = ""
    pos = [(10, 10), (265, 10), (10, 195), (265, 195)]
    W, H = 245, 175
    for (x, y) in pos:
        b += rect(x, y, W, H, "#fffdf6", sw=2, rx=10)
    if labels:
        for (x, y), n in zip(pos, labels):
            b += text(x + W / 2, y + 24, n, 16, fill="#555", weight="bold")
    # sign
    x, y = pos[0]
    b += rect(x + 20, y + 40, W - 40, 112, "#fff", stroke="#c0392b", sw=5, rx=8)
    n = len(sign)
    for i, (t, sz) in enumerate(sign):
        b += text(x + W / 2, y + 96 + (i - (n - 1) / 2) * 38 + sz / 3, t, sz, weight="bold", fill="#c0392b")
    # timetable
    x, y = pos[1]
    b += text(x + W / 2, y + 52, timetable["title"], 20, weight="bold", fill=BLUE)
    b += rect(x + 18, y + 64, W - 36, 26, "#d6e4f7", sw=1, rx=3)
    b += text(x + 65, y + 83, timetable["header"][0], 16, weight="bold") + text(x + 160, y + 83, timetable["header"][1], 16, weight="bold")
    for i, (a, c) in enumerate(timetable["rows"]):
        yy = y + 112 + i * 26
        b += text(x + 65, yy, a, 18) + text(x + 160, yy, c, 18)
        b += f'  <path d="M{x + 18} {yy + 8} H{x + W - 18}" stroke="#bbb" stroke-width="1"/>\n'
    # menu
    x, y = pos[2]
    b += text(x + W / 2, y + 54, menu["title"], 22, weight="bold", fill=GREEN)
    for i, (a, c) in enumerate(menu["rows"]):
        yy = y + 90 + i * 32
        b += text(x + 24, yy, a, 18, anchor="start") + text(x + W - 24, yy, c, 18, anchor="end", weight="bold")
        b += f'  <path d="M{x + 24} {yy + 9} H{x + W - 24}" stroke="#bbb" stroke-width="1" stroke-dasharray="3 4"/>\n'
    # flyer
    x, y = pos[3]
    b += rect(x + 16, y + 38, W - 32, 122, "#fdeec0", stroke=ORANGE, sw=3, rx=6)
    for i, (t, sz, w) in enumerate(flyer):
        b += text(x + W / 2, y + 78 + i * 34, t, sz, weight=w, fill=ORANGE if i == 0 else INK)
    return b

@image
def alltagstexte_vier():
    b = _cards(["Schild", "Fahrplan", "Speisekarte", "Flyer"],
               [("Please", 30), ("wait here.", 30)],
               {"title": "Bus 12", "header": ["Time", "To"], "rows": [("9:10", "Oakley"), ("9:40", "Oakley"), ("10:10", "Oakley")]},
               {"title": "Menu", "rows": [("Tea", "£2"), ("Cake", "£3"), ("Eggs", "£4")]},
               [("Book Fair!", 28, "bold"), ("Saturday, 10:00", 20, "normal"), ("At the library", 20, "normal")])
    return svg(520, 380, "Vier Alltagstexte: Schild, Fahrplan, Speisekarte und Flyer (eigene Zeichnung)", b)

@image
def alltagstexte_material():
    b = _cards(None,
               [("Closed", 34), ("Back at 2:30", 22)],
               {"title": "Train to Fairfield", "header": ["Leaves", "Arrives"], "rows": [("9:15", "9:50"), ("10:20", "10:55"), ("11:20", "11:55")]},
               {"title": "Menu", "rows": [("Sandwich", "£3.50"), ("Soup", "£4.50"), ("Juice", "£2")]},
               [("Music Club", 28, "bold"), ("Friday, 4:30", 20, "normal"), ("Room 5", 20, "normal")])
    return svg(520, 380, "Vier Alltagstexte zum Nachschauen (eigene Zeichnung)", b)

@image
def szene_baeckerei_schild():
    b = '  <rect y="262" width="640" height="78" fill="#cfcfcf"/>\n  <rect width="640" height="262" fill="#efe7d3"/>\n'
    b += rect(200, 30, 240, 232, "#f7e0c8", sw=3, rx=4)
    b += rect(240, 42, 160, 42, "#fff", sw=3) + text(320, 72, "bakery", 26)
    b += rect(270, 100, 100, 162, "#b98a5a", sw=3, rx=4)
    b += rect(277, 112, 86, 62, "#fff", sw=2, rx=2)
    b += text(320, 138, "Please", 18, weight="bold") + text(320, 162, "come in", 18, weight="bold")
    b += '  <circle cx="356" cy="210" r="4" fill="#333"/>\n'
    b += kid("sophie", 70, 110, .85) + kid("ellie", 480, 110, .85)
    b += text(120, 90, "?", 40, fill="#c0392b", weight="bold")
    return svg(640, 340, "Sophie und Ellie stehen vor der Tür einer Bäckerei, an der ein Schild hängt", b)

@image
def szene_clothes_shop():
    b = '  <rect y="270" width="640" height="70" fill="#d9c7a3"/>\n  <rect width="640" height="270" fill="#efe7d3"/>\n'
    b += rect(220, 24, 200, 40, "#fff", sw=3) + text(320, 53, "clothes shop", 24)
    b += '  <path d="M180 120 H460" stroke="#7a5a35" stroke-width="6"/>\n  <rect x="186" y="120" width="6" height="150" fill="#7a5a35"/><rect x="448" y="120" width="6" height="150" fill="#7a5a35"/>\n'
    cols = ["#d33", "#2c6fd8", "#e0b020", "#138d75", "#8a4fb0"]
    for i, c in enumerate(cols):
        cx = 215 + i * 52
        b += f'  <path d="M{cx} 120 V132" stroke="#333" stroke-width="2"/>\n'
        b += (_jumper if i % 2 == 0 else _shirt)(cx - 22, 190, .62, c)
    b += kid("sophie", 50, 120, .85) + kid("ellie", 500, 120, .85)
    b += '  <rect x="256" y="222" width="130" height="10" fill="#7a5a35"/>\n'
    b += _cap(300, 222, .55, "#2c6fd8") + _cap(345, 222, .55, "#d33")
    return svg(640, 340, "Sophie und Ellie in einem Kleidungsgeschäft vor einer Stange mit Pullovern und Hemden", b)

@image
def kleidung_regal():
    b = '  <rect x="20" y="130" width="480" height="10" rx="3" fill="#7a5a35"/>\n  <rect x="20" y="300" width="480" height="10" rx="3" fill="#7a5a35"/>\n'
    items = [(_shirt, 60, 128, "#d33", "shirt", "£9"), (_trousers, 215, 128, "#2c6fd8", "jeans", "£20"), (_cap, 370, 128, "#e0b020", "cap", "£6")]
    for f, x, y, c, name, price in items:
        b += f(x, y, 1.5, c)
        cx = x + 45
        b += _tag(cx, 150, price) + text(cx, 205, name, 18)
    for (x, s, name) in ((80, .8, "small"), (225, 1.1, "medium"), (365, 1.4, "large")):
        b += _shirt(x, 298, s, "#2c6fd8")
        b += text(x + 30 * s, 332, name, 18)
    return svg(520, 345, "Regale mit Kleidung und Preisschildern (eigene Zeichnung)", b)

@image
def kleidung_preise():
    b = '  <rect x="20" y="170" width="480" height="10" rx="3" fill="#7a5a35"/>\n'
    items = [(_jumper, 40, "#138d75", "jumper", "£14", 1.3), (_trousers, 160, "#2c6fd8", "trousers", "£18", 1.3),
             (_shoes, 262, "#8a4fb0", "shoes", "£25", 1.1), (_cap, 396, "#d33", "cap", "£7", 1.3)]
    for f, x, c, name, price, s in items:
        b += f(x, 168, s, c)
        cx = x + 38 * s
        b += _tag(cx, 192, price) + text(cx, 250, name, 20)
    return svg(520, 280, "Preisschilder im Laden (eigene Zeichnung)", b)
