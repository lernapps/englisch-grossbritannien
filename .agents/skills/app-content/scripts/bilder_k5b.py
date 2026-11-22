# Kapitel 5, Seite politik-uk (Stufe 7-8): Schaubild und Aufgabenbild. Wird von make_images.py geladen (gleiche Hilfsfunktionen).
@image
def politik_schaubild():
    b = ""
    rows = [(20, 80, "#d6e4f7", BLUE, "Monarch", ["represents", "the country"]),
            (125, 175, "#f7e0c8", ORANGE, "Parliament", ["makes laws"]),
            (330, 80, "#d9f0ee", GREEN, "Prime Minister", ["leads the", "government"])]
    # row 1: Monarch
    b += rect(14, 20, 220, 80, "#d6e4f7", stroke=BLUE, sw=3, rx=12) + text(124, 70, "Monarch", 26, weight="bold")
    # row 2: Parliament with two houses
    b += rect(14, 130, 220, 190, "#f7e0c8", stroke=ORANGE, sw=3, rx=12) + text(124, 164, "Parliament", 26, weight="bold")
    b += rect(26, 182, 196, 56, "#fff", rx=8) + text(124, 218, "House of Commons", 19)
    b += rect(26, 250, 196, 56, "#fff", rx=8) + text(124, 286, "House of Lords", 19)
    # row 3: Prime Minister
    b += rect(14, 350, 220, 80, "#d9f0ee", stroke=GREEN, sw=3, rx=12) + text(124, 400, "Prime Minister", 26, weight="bold")
    for y, lines in ((60, ["represents", "the country"]), (225, ["makes", "laws"]), (390, ["leads the", "government"])):
        b += text(280, y - 4 if len(lines) == 2 else y, lines[0], 24, anchor="start")
        b += text(280, y + 26 if len(lines) == 2 else y + 26, lines[1], 24, anchor="start")
        b += f'  <path d="M240 {y} H262" stroke="#555" stroke-width="3" fill="none"/>\n  <path d="M274 {y} l-14 -8 v16 z" fill="#555"/>\n'
    return svg(480, 450, "Schaubild mit drei Kästen: Monarch, Parliament mit zwei Teilen und Prime Minister, daneben je eine kurze englische Zeile", b)

@image
def politik_orte():
    b = ""
    for i, (letter, l1, l2, c) in enumerate([("A", "Buckingham", "Palace", "#f7e0c8"), ("B", "Palace of", "Westminster", "#d6e4f7"), ("C", "Elizabeth", "Tower", "#d9f0ee")]):
        x = 16 + i * 152
        b += rect(x, 40, 144, 140, c, sw=3, rx=12) + text(x + 72, 80, letter, 28, weight="bold")
        b += text(x + 72, 123, l1, 18) + text(x + 72, 148, l2, 18)
    return svg(480, 220, "Drei Kästen mit den Buchstaben A, B und C, in jedem steht der Name eines Gebäudes in London", b)
