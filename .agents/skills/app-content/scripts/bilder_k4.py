# Kapitel 4 (Stufe 7-8): Fahrkarten. Wird von make_images.py geladen (gleiche Hilfsfunktionen).
def _ticket(rows, title):
    b = rect(20, 30, 440, 250, "#fffbe8", sw=3, rx=14)
    b += rect(20, 30, 440, 50, "#2c6fd8", sw=3, rx=14) + text(240, 64, title, 22, fill="#fff", weight="bold")
    y = 112
    for k, v in rows:
        b += text(40, y, k, 16, anchor="start", fill="#555") + text(200, y, v, 20, anchor="start", weight="bold")
        y += 36
    return b

@image
def fahrkarte_beispiel():
    b = _ticket([("FROM", "Millbrook"), ("TO", "London"), ("TYPE", "Return"), ("PLATFORM", "2"), ("DEPARTS", "08:10")], "TRAIN TICKET")
    return svg(480, 310, "Fahrkarte mit Abfahrtsort, Ziel, Art, Gleis und Abfahrtszeit", b)

@image
def fahrkarte_material():
    b = _ticket([("FROM", "Fairfield"), ("TO", "Millbrook"), ("TYPE", "Single"), ("PLATFORM", "6"), ("DEPARTS", "17:20")], "TRAIN TICKET")
    return svg(480, 310, "Eine andere Fahrkarte mit Abfahrtsort, Ziel, Art, Gleis und Abfahrtszeit", b)
