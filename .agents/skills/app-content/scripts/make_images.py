# Draws the figures of this app into src/images/ (the plan of Millbrook, scenes with the children, maps).
# Run from the app folder: python3 .agents/skills/app-content/scripts/make_images.py [name ...]
# The figures are the <g id> of millbrook-klassenzimmer.svg of hello-millbrook (#470) and szene-cafe.svg of
# englisch-verbketten (Mr Hill, Mrs Parker), copied unchanged into figuren-defs.svg.
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
DEFS = open(os.path.join(HERE, "figuren-defs.svg"), encoding="utf-8").read().strip()
BG = "#f4efe2"; BLUE = "#2c6fd8"; ORANGE = "#d35400"; GREEN = "#138d75"; INK = "#333"
OUT = "src/images/"

def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img">\n  <title>{title}</title>\n  {DEFS}\n'
            f'  <rect width="{w}" height="{h}" fill="{BG}"/>\n{body}\n</svg>\n')
def kid(name, x, y, s=0.85): return f'  <use href="#{name}" transform="translate({x},{y}) scale({s})"/>\n'
def text(x, y, t, size=16, anchor="middle", fill=INK, weight="normal"):
    return f'  <text x="{x}" y="{y}" text-anchor="{anchor}" font-family="sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{t}</text>\n'
def rect(x, y, w, h, fill, stroke=INK, sw=2, rx=6):
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'

# ---- The plan of Millbrook: fixed for all pages (see the content guide, "Content structure") ----
# viewBox 520 x 360, north up. High Street y 170-190 (west-east); Church Road x 140-160 and Mill Lane x 380-400 (north-south).
PLACES = {  # name: (x, y, w, h, colour); the label is the name
    "library": (20, 50, 110, 100, "#d6e4f7"), "bakery": (168, 50, 100, 100, "#f7e0c8"),
    "post office": (274, 50, 100, 100, "#efd9f3"), "park": (408, 50, 102, 100, "#cfe8c4"),
    "school": (20, 210, 110, 100, "#f3d9d9"), "clothes shop": (168, 210, 100, 100, "#fbe9a6"),
    "supermarket": (274, 210, 100, 100, "#d9f0ee"), "station": (408, 210, 102, 100, "#e0e0e0"),
}
def compass():
    return ('  <g stroke="#333" stroke-width="2" fill="#333"><path d="M490 40 V12" fill="none"/><path d="M484 20 L490 8 L496 20 Z"/></g>\n'
            + text(472, 30, "N", 16, weight="bold") + text(512, 190, "O", 14, fill="#555") * 0)
def street_names():
    return compass() + text(460, 186, "High Street", 16, fill="#222") + text(150, 32, "Church Road", 16, fill="#222") + text(390, 345, "Mill Lane", 16, fill="#222")
def plan_base(show=True):
    b = ""
    b += '  <g fill="#cfcfcf" stroke="#999" stroke-width="2"><rect x="0" y="170" width="520" height="20"/><rect x="140" y="0" width="20" height="360"/><rect x="380" y="0" width="20" height="360"/></g>\n'
    for n, (x, y, w, h, c) in PLACES.items():
        b += rect(x, y, w, h, c)
        words = n.split(" ")
        for i, wd in enumerate(words):
            b += text(x + w / 2, y + h / 2 + (i - (len(words) - 1) / 2) * 18 + 5, wd, 16)
    return b

IMAGES = {}
def image(f):
    IMAGES[f.__name__.replace("_", "-")] = f; return f

@image
def stadtplan_millbrook():
    b = plan_base()
    b += street_names()
    b += '  <circle cx="75" cy="200" r="7" fill="#138d75" stroke="#333" stroke-width="2"/>\n'
    return svg(520, 360, "Plan von Millbrook (Schemaplan)", b)

@image
def stadtplan_beispielweg():
    """Example route park -> supermarket: out of the park onto Mill Lane, south, over the High Street."""
    b = plan_base() + street_names()
    b += f'  <path d="M390 100 V262" fill="none" stroke="{ORANGE}" stroke-width="5" stroke-linecap="round"/>\n'
    b += f'  <path d="M380 256 L390 276 L400 256 Z" fill="{ORANGE}"/>\n'
    b += '  <circle cx="390" cy="100" r="8" fill="#138d75" stroke="#333" stroke-width="2"/>\n'
    for y, n in ((130, "1"), (180, "2"), (238, "3")):
        b += f'  <circle cx="390" cy="{y}" r="11" fill="#fff" stroke="{ORANGE}" stroke-width="3"/>\n' + text(390, y + 6, n, 16, fill=ORANGE, weight="bold")
    return svg(520, 360, "Plan von Millbrook mit einem Weg (Schemaplan)", b)

@image
def szene_stadtplan():
    b = '  <rect y="262" width="640" height="78" fill="#cfcfcf"/>\n  <rect width="640" height="262" fill="#efe7d3"/>\n'
    b += rect(250, 40, 140, 56, "#fff", sw=3) + text(320, 74, "Millbrook", 24)
    b += '  <rect x="316" y="96" width="8" height="94" fill="#7a5a35"/>\n'
    b += kid("sophie", 120, 110, .85) + kid("ellie", 450, 110, .85)
    b += rect(240, 200, 160, 80, "#fff", sw=2) + '  <path d="M250 240 H390 M320 210 V270" stroke="#999" stroke-width="8"/>\n'
    return svg(640, 340, "Sophie und Ellie stehen mit einem Plan unter dem Ortsschild von Millbrook", b)

import glob
for _f in sorted(glob.glob(os.path.join(HERE, "bilder_*.py"))):  # further figures, one file per chapter, same helpers
    exec(compile(open(_f, encoding="utf-8").read(), _f, "exec"))

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, f in IMAGES.items():
        if len(sys.argv) > 1 and name not in sys.argv[1:]: continue
        open(OUT + name + ".svg", "w", encoding="utf-8").write(f())
        print("wrote", OUT + name + ".svg")
