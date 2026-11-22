# Kapitel 5, Seite politik-uk (Stufe 7-8): Schaubild und Aufgabenbild. Wird von make_images.py geladen (gleiche Hilfsfunktionen).
@image
def politik_schaubild():
    b = ""
    # row 1: King
    b += rect(20, 20, 200, 70, "#d6e4f7", stroke=BLUE, sw=3, rx=12) + text(120, 63, "King", 22, weight="bold")
    b += text(364, 62, "represents the country", 16)
    # row 2: Parliament with two houses
    b += rect(20, 120, 200, 160, "#f7e0c8", stroke=ORANGE, sw=3, rx=12) + text(120, 148, "Parliament", 22, weight="bold")
    b += rect(34, 165, 172, 46, "#fff", rx=8) + text(120, 194, "House of Commons", 16)
    b += rect(34, 222, 172, 46, "#fff", rx=8) + text(120, 251, "House of Lords", 16)
    b += text(364, 205, "makes laws", 16)
    # row 3: Prime Minister
    b += rect(20, 310, 200, 70, "#d9f0ee", stroke=GREEN, sw=3, rx=12) + text(120, 353, "Prime Minister", 22, weight="bold")
    b += text(364, 352, "leads the government", 16)
    for y in (55, 205, 345):
        b += f'  <path d="M232 {y} H256" stroke="#555" stroke-width="3" fill="none"/>\n  <path d="M268 {y} l-14 -8 v16 z" fill="#555"/>\n'
    return svg(480, 400, "Schaubild mit drei Kästen: King, Parliament mit zwei Teilen und Prime Minister, daneben je eine kurze englische Zeile", b)

@image
def politik_orte():
    b = ""
    for i, (letter, l1, l2, c) in enumerate([("A", "Buckingham", "Palace", "#f7e0c8"), ("B", "Palace of", "Westminster", "#d6e4f7"), ("C", "Elizabeth", "Tower", "#d9f0ee")]):
        x = 16 + i * 152
        b += rect(x, 40, 144, 140, c, sw=3, rx=12) + text(x + 72, 80, letter, 28, weight="bold")
        b += text(x + 72, 123, l1, 18) + text(x + 72, 148, l2, 18)
    return svg(480, 220, "Drei Kästen mit den Buchstaben A, B und C, in jedem steht der Name eines Gebäudes in London", b)
