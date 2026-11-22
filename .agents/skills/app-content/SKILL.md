---
name: app-content
description: Use for any content work in this app - researching, writing, extending, correcting or reviewing its competencies, chapters, pages, rounds, questions, exercises, figures, terms or sources. This app's own content decisions; they take precedence over the generic lernapps content skills. Load it before you change any content.
---

# Content guide of this app

„Großbritannien: Stadt, Inseln, London“: Explainer (Einheiten-App `subject: englisch`, Format 2, Sprache Deutsch, englische Beispiele). Auftrag: Issue lernapps/apps#478 (Epic lernapps/apps#489, Konventionen dort). Die erste Version baut nur Stufe 5-6 (Kapitel 1 bis 3). **Gebaut:** alle neun Inhaltsseiten und beide Wiederholungsseiten der Kapitel 1 bis 3, 54 Audiosätze (9 Seiten × 6, Liste `.agents/skills/app-content/scripts/audio-texte.json`), 23 Bilder in `src/images/`, je Kapitel eine Selbsteinschätzung (zwei Übungen je Seite); Kapitel 4 „Klassenfahrt nach London“ und 5 „Von 1066 bis Westminster“ (Stufe 7-8) kommen als Inkremente `increment/<NN>-<name>`.

## Curriculum

Englisch als erste Fremdsprache, erstes und zweites Lernjahr (Stufe 5-6 der Karte). Kein Lehrplan: Reihenfolge und Bausteine kommen aus der Lernlandkarte `https://lernapps.net/apps/map/englisch.json` (Fokus `competency`, Einheiten-App über die Stränge `wortschatz`, `texte`, `landeskunde`). Vorwissen: Hello, Millbrook! (#470), #471 bis #476. Nicht hier: Politik als Diskussionsthema (#484, #487), USA, Kanada, Australien (#484), Schule und Feste (#470), Alltag und Familie (#477), Kapitel 4 und 5.

## Competencies

Alle neun sind Lücken der Karte, Band 5-6, alle gebaut. Eine Seite je Baustein; die „Ich kann“-Sätze stehen wie in der Karte in `src/<kapitel>/<seite>.yaml` (nicht umformulieren). `competencies:` nennt Karten-Ids; Wiederholungsseiten haben `recap:` und keine `competencies`.

1. Kapitel `wege-laeden-schilder` („Wege, Läden und Schilder“)
   - Wiederholung `recap: [englisch/praepositionen-ort, englisch/imperativ, englisch/zahlen]` → `das-brauchst-du` (ohne Übung)
   - `stadt-wegbeschreibung` → `stadt-wegbeschreibung` (Musterseite): „Ich kann Orte in der Stadt benennen und einen einfachen Weg beschreiben.“
   - `alltagstexte` → `alltagstexte`: „Ich kann Alltagstexte wie Fahrpläne, Speisekarten, Flyer und Schilder erkennen und ihnen gezielt Informationen entnehmen.“
   - `kleidung-einkaufen` → `kleidung-einkaufen`: „Ich kann Kleidung benennen und beim Einkaufen nach Größe und Preis fragen.“
2. Kapitel `britische-inseln` („Die Britischen Inseln“)
   - Wiederholung `recap: englisch/vergleiche` → `das-brauchst-du`
   - `britische-inseln` → `britische-inseln`: „Ich kann die Teile des Vereinigten Königreichs und ihre Hauptstädte auf der Karte zeigen und UK, Great Britain und Ireland unterscheiden.“
   - `region-uk` → `region-uk`: „Ich kann eine Region Großbritanniens wie Cornwall, den Lake District oder Wales vorstellen.“
   - `stadt-land-uk` → `stadt-land-uk`: „Ich kann das Leben in einer britischen Großstadt und auf dem Land vergleichen.“
3. Kapitel `london` („London“) – keine Wiederholungsseite
   - `roemer-in-britannien` → `roemer-in-britannien`: „Ich kann erzählen, was die Römer in Britannien hinterlassen haben, zum Beispiel Hadrian’s Wall und Bath.“
   - `london-sehenswuerdigkeiten` → `london-sehenswuerdigkeiten`: „Ich kann wichtige Sehenswürdigkeiten Londons nennen und beschreiben.“
   - `vielfalt-gb` → `vielfalt-gb`: „Ich kann beschreiben, dass in Großbritannien Menschen mit vielen verschiedenen Herkünften zusammenleben.“

Römer vor Sehenswürdigkeiten, weil das Issue sagt: „Am Anfang steht Londinium“. Alle `requires` stehen vor ihrer Seite oder auf einer Wiederholungsseite.

Übungs-IDs: Präfix = Seite (`wege-ort`), Diktat `<präfix>-hoeren`, Nachsprechen `<präfix>-nachsprechen`.

## Content structure

- Pfad: `src/<kapitel>/chapter.yaml`, Seiten `src/<kapitel>/<seite>.yaml`.
- Jede Inhaltsseite hat dieselben Abschnitts-IDs in dieser Reihenfolge: `einstieg` (Szene der Figuren, erste leichte Aufgabe, „Das kannst du danach“), `neu` (Bild, Merke-Kasten, höchstens eine Wörter-Tabelle „Klassenzimmer-Poster · Wörter dieser Seite“), `uebung` (mindestens vier Übungen, leicht → schwer), `anwenden` (`speaking-task`, `open-task`), `weiter` (nächster Halt; am Kapitelende ein Rückblick „Schulkalender · …“). Wiederholungsseiten: nur `einstieg` mit Text, höchstens einer Tabelle und Links zur Karte.
- Länge: höchstens 350 Wörter Text, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, eine Wörter-Tabelle je Seite. Jede Seite bringt einen neuen Schritt.
- Je Kapitel eine Selbsteinschätzung (`chapter.yaml`, zwei Übungen je Seite).
- Audio: je Seite 6 Sätze (3 Diktat, 3 Nachsprechen), neue Sätze, die nirgends sonst auf der Seite stehen; Liste `.agents/skills/app-content/scripts/audio-texte.json`.
- Geschichte (Stufe 5-6, Figuren und Orte wie in #470, nicht ändern): Sophie (blond, Zöpfe, grüne Jacke, aus Deutschland, 11 bis 12, wohnt bei den Parkers), Ellie Parker (11, roter Pferdeschwanz, rote Jacke), Peter Parker (9, kurze braune Haare, gelbe Jacke), Amir (11, schwarze Locken, Brille, blaue Jacke), Mr Hill (graue Haare, braune Jacke), Mrs Parker. Millbrook School, Schultag ab 8:45. Kapitel 1 ein Samstag in Millbrook (Stadtbummel von Sophie, Ellie und Mrs Parker), Kapitel 2 Mr Hill hängt eine Karte auf, die Parkers fahren in den Herbstferien nach Cornwall, Kapitel 3 ein Tag in London mit Mr Hills Klasse (die Klassenfahrt selbst ist Kapitel 4). Kein Schulfest, kein Lagerraum, keine Ausstellung „Our Millbrook“ als Handlung.
- **Der Stadtplan von Millbrook** (erfunden, bleibt über alle Seiten und Inkremente gleich): Karte in einem Raster, Norden oben. Drei Straßen: **High Street** (von West nach Ost, in der Mitte), **Church Road** (Nord–Süd, kreuzt die High Street im Westen), **Mill Lane** (Nord–Süd, kreuzt sie im Osten). Nördlich der High Street, von West nach Ost: library (an der Ecke Church Road, westlich), bakery (zwischen Church Road und Mill Lane), post office (neben der bakery), park (östlich der Mill Lane). Südlich der High Street: school (Millbrook School, am westlichen Ende der Church Road), clothes shop (zwischen Church Road und Mill Lane), supermarket (neben dem clothes shop), station (östlich der Mill Lane). Start der Wege ist die school (grüner Punkt). Die Schreibung der Straßen: „the High Street“ (mit Artikel: Turn right into the High Street), „Church Road“ und „Mill Lane“ ohne Artikel (Turn right into Mill Lane). Orte stehen mit Namen im Bild (library, bakery, post office, park, school, clothes shop, supermarket, station). Lage: Die Orte nördlich der High Street liegen von West nach Ost library | Church Road | bakery, post office | Mill Lane | park; südlich school | Church Road | clothes shop, supermarket | Mill Lane | station; die school liegt der library, die clothes shop der bakery, der supermarket dem post office und die station dem park gegenüber. Dieser Plan steht als `stadtplan-millbrook` in `make_images.py` (Koordinaten dort einmal); `stadtplan-beispielweg` zeigt den Beispielweg park → supermarket (Turn left. Cross the High Street. The supermarket is on the right.). Himmelsrichtungen: Kompass N im Bild, Osten rechts; die Aufgaben sagen, in welche Richtung man schaut.
- Anrede „du“.

## Terminology

- „Ausdruck“ (fester Ausdruck), nie „Wendung“. Fachbegriffe noun, verb, adjective, sentence.
- Karten-Begriffe, immer dieselben: **Plan** (Stadtplan von Millbrook), **Karte** (Britische Inseln, London), **Halt** (Station eines Wegs oder Rundgangs), **Pfeil** (Richtung auf dem Plan), **Schemakarte** (gezeichnet, nicht maßstabsgerecht).
- Britisches Englisch (favourite, colour, centre). Englische Aufgaben enthalten kein deutsches Wort. Englisches immer mit deutscher Bedeutung, wo ein Wort neu ist.
- Länder und Namen: UK = Vereinigtes Königreich (England, Schottland, Wales, Nordirland); Great Britain = die Insel (England, Schottland, Wales); Ireland = die Insel Irland und der Staat Republik Irland; Nordirland gehört zum UK. Hauptstädte: London, Edinburgh, Cardiff, Belfast, Dublin.
- Aussprache: keine Lautschrift (IPA gehört zu #482); Hörtexte nur als ganze Sätze.

## Exercise patterns

Aufbau leicht → schwer: wählen/zuordnen → Lücke → schreiben mit Cue → übersetzen/frei. Je Übung `mistakes` mit eigener Meldung und `hint`; gleichwertige Antworten mit `(a|b)`; `punctuation: ok`. Die Arten wechseln von Seite zu Seite.

- Plan lesen und zuordnen: `matching`, `single-choice`, `true-false` mit Begründung; Weg ordnen: `ordering`; Weg schreiben: `language-task` mode `write` mit englischem Cue.
- Text entnehmen (Schild, Fahrplan, Speisekarte, Steckbrief): `single-choice`, mode `gap`.
- Form: mode `choice` (Lücke, `distractors`), `write` mit `cue`, `table`.
- Korrigieren: mode `write`; Übersetzen: mode `write` mit `source`.
- Diktat: `language-task` mit `audio` (höchstens drei ganze Sätze); Nachsprechen: `speaking-task`; freies Schreiben: `open-task` mit Punkten.
- Musterseite `stadt-wegbeschreibung` (Beispiele für alle Seiten): Zuordnen der Orte (`matching`), Ort am Plan wählen (`language-task` choice mit `material`), Richtung ableiten (choice), Wortreihenfolge (`ordering`), wahr/falsch mit Begründung, Sätze schreiben, Befehl umformen, Diktat, Nachsprechen, `open-task`. Der Beispielweg im Bild und die Lösungen der Übungen sind verschiedene Wege.
- Typische Fehler (jeweils `mistakes`): turn to left, go straight ohne on, near statt next to, Imperativ mit You, a trousers, How much is the shoes, £ falsch gesprochen, UK = England, Ireland = Nordirland, Dublin/Belfast vertauscht, more busy, bigger then, as busier as, Römer = Wikinger/Normannen, Hadrian’s Wall als Grenze zu Wales, Big Ben als Turmname, Tower Bridge/London Bridge, British = nur eine Herkunft, Herkunft und Staatsangehörigkeit gleichgesetzt.
- Keine Komponente (`prefer-built-in-block`), keine Datendatei: jede Tatsache steht einmal in ihrer Seite. Ein Ziehen-Puzzle auf der Karte wäre ein Wunsch für die Vorlage.

## Figures

- Eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“, `src/images/`, erzeugt vom Skript `.agents/skills/app-content/scripts/make_images.py` (ein neues Bild: Funktion ergänzen und Skript starten, nie die SVG von Hand ändern). Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, bei 360 px lesbar. Skizzen in `.vibe/sketches/`.
- Figuren der Szenen: als `<g id>` aus `millbrook-klassenzimmer.svg` von #470 (hello-millbrook) kopiert und gleich gelassen; keine Fotos, keine Figuren aus Büchern, Filmen oder Marken. `alt` sagt, was das Bild zeigt, nie die Lösung; die Bildunterschrift nennt, wer wer ist (Sophie Zöpfe, Ellie roter Pferdeschwanz, Amir Brille, Peter gelbe Jacke).
- Karten (Britische Inseln, Cornwall, London): **Schemakarten**, selbst gezeichnet, „nicht genau nach Maßstab“ (kindgerecht für „nicht maßstabsgerecht“) in Alt-Text und Bildunterschrift; nichts aus einem Atlas oder aus Wikipedia kopiert; Lage und Namen richtig (England, Schottland, Wales, Nordirland, Irland; London, Edinburgh, Cardiff, Belfast, Dublin; Cornwall im Südwesten, Lake District im Nordwesten Englands, Hadrian’s Wall im Norden Englands). Lage nach den geöffneten Quellen unter „Sources“.
- Poster und Kalender sind `table`-Blöcke, wachsen von Seite zu Seite: „Klassenzimmer-Poster · …“ und „Schulkalender · Rückblick Kapitel 1 bis 3“.
- Gebaut (Skripte `make_images.py` für den Plan und die Szene von Seite 1, `bilder_k1.py`, `bilder_k2.py`, `bilder_k3.py` je Kapitel; `make_images.py` lädt `bilder_*.py` selbst): Kapitel 1 `stadtplan-millbrook`, `stadtplan-beispielweg`, `szene-stadtplan`, `szene-baeckerei-schild`, `alltagstexte-vier`, `alltagstexte-material`, `szene-clothes-shop`, `kleidung-regal`, `kleidung-preise`; Kapitel 2 `szene-karte-klasse`, `inseln-karte-namen`, `inseln-karte-buchstaben` (Aufgabenbild mit Buchstaben statt Namen), `szene-cornwall`, `cornwall-karte` (ohne erfundene Orte), `region-karte-buchstaben`, `stadt-land-bild`; Kapitel 3 `szene-london-roemer`, `zeitstrahl-roemer`, `roemer-orte`, `london-karte`, `london-karte-nummern`, `szene-london-rundgang`, `szene-familien`. Erfundene Ortsnamen (Fairfield, Oakley, Music Club) stehen nur in den Bildern von `alltagstexte`. Auf dem Londoner Rundgang ist Peter nicht dabei (erfunden, damit die Postkarte für ihn passt).
- Aufgabenbilder (`material`) zeigen andere Texte, Preise oder Beschriftungen als die Bilder im Erklärteil.
- Fotos und Videos: keine (Lizenz und Quelle nicht geprüft).

## Sources

Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/` (A1/A2, geöffnet 2026-11-21). Wörter außerhalb der Liste werden auf der Seite mit Bedeutung eingeführt und hier gelistet (Liste wächst mit den Seiten; keine Wörter listen, die nirgends vorkommen): Außerhalb der Liste, jeweils auf der Seite in der Wörter-Tabelle oder im Text mit Bedeutung eingeführt: `stadt-wegbeschreibung` bakery (Bäckerei); `alltagstexte` timetable, flyer, closed (sign und menu stehen als A2 in der Liste); `kleidung-einkaufen` shoes, medium, a pair of (cap und jumper sind A2); `britische-inseln` United Kingdom, Great Britain, Ireland, Republic of Ireland, British Isles (Eigennamen; capital ist A2); `region-uk` region, south-west, north-west, Atlantic Ocean, English Channel, Welsh; `stadt-land-uk` countryside (A2, im Text erklärt); `roemer-in-britannien` Roman, fort, Britain, baths, Londinium, Aquae Sulis, Hadrian’s Wall, came und built (unregelmäßige Formen, im Merke); `london-sehenswuerdigkeiten` bridge, big wheel, Thames, Bloomsbury, Big Ben (tower, palace, wheel in der Tabelle); `vielfalt-gb` grandparents, moved, Welsh, Scottish Gaelic, Irish. Jede neue Seite ergänzt diese Zeile um ihre Wörter. Fakten aus Wikipedia (nur Fakten, keine Sätze, CC BY-SA), geöffnet am 2026-11-21: `United Kingdom` (Teile, Hauptstädte), `Great Britain` (Insel aus England, Schottland, Wales), `British Isles`, `Republic of Ireland` (Dublin, Staat auf der Insel Irland), `Cornwall` (Südwesten Englands, Atlantik, Ärmelkanal), `Lake District` (Nationalpark in Cumbria, Nordwesten Englands, Berge und Seen), `London` (Hauptstadt, Themse, von den Römern als Londinium gegründet), `Londinium`, `Hadrian's Wall` (begonnen 122 n. Chr., im Norden Englands), `Roman Baths (Bath)` (Aquae Sulis), `Tower of London`, `Big Ben`, `Buckingham Palace`, `London Eye`, `Tower Bridge`, `British Museum`, `Languages of the United Kingdom`. Nicht geprüft (HTTP 429): `Roman Britain`, `Demography of London`; **keine Bevölkerungszahlen**, Jahre nur, wo belegt. Nicht gelesen: deutsche Wikipedia, Klexikon. Beispielsätze sind eigene aus dem Alltag der Figuren. Audio: KI-Stimme `bf_emma` (britisch, weiblich), mit Skill `lernapps-audio` erzeugt und als KI-generiert markiert. Material der Ersteller:in: keines.

## Adding a chapter or round

1. Baustein auf der Karte wählen; die Voraussetzungen müssen auf früheren Seiten stehen oder eine Wiederholungsseite bekommen.
2. Seite `src/<kapitel>/<seite>.yaml` mit den Abschnitten `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` anlegen, in `chapter.yaml` und `src/app.yaml` eintragen, Karten-Id als `competencies` setzen.
3. Karte oder Plan in `make_images.py` erweitern (Kapitel 4: derselbe Stadtplan und dieselbe London-Karte für Zug, U-Bahn und Fahrkarten; Kapitel 5: Zeitleiste mit Datendatei `src/data/` und Block `timeline`), Poster um die Zeilen der Seite. Stufe 7-8: Chats und kurze Dialoge, ein Bild nur wo es etwas zeigt.
4. Übungen aus den Mustern oben, je mit `mistakes` und `hint`; 1 bis 3 ihrer Übungen in `selfAssessment` aufnehmen, wie Skill `lernapps-explainer-self-assessment` sagt.
5. Hörtexte: Datei `src/audio/<satz>.mp3` und Eintrag in `audio-texte.json` (Datei → Satz, 6 je Seite), erzeugt mit `regen_audio.py` (schneidet das Ausklingen ab); anhören; Sätze nicht zwischen Seiten wiederholen, Namen am Satzende zweisilbig.
6. Wörter gegen den Grundwortschatz prüfen; `npx --no -- lernapps check`; committen.

## Rules learned from mistakes

Aus den Konventionen Abschnitt 7 und den Vorgängern (#470 bis #476):
- Jede Übung fragt nur Wörter ab, die vorher auf der Seite stehen; eine Tabelle, die eine Übung beantwortet, steht nicht direkt darüber; die Antwort einer Frage steht nie im Absatz direkt darüber.
- Kein Hörsatz steht wörtlich oder fast wörtlich im Einstieg, Poster, Merke, Bildtext oder in einer Aufgabe derselben Seite (Skript prüft es).
- Poster, Merke, Einstieg und Bild nennen andere Beispielsätze und Wörter als die Übungen darunter.
- Distraktoren nur echte Lernerfehler, keine Unwörter; jeder Distraktor und jedes Fehlerbild hat eine eigene Meldung. Ein Einstiegs-`single-choice` hat mindestens drei Optionen.
- Höchstens eine kurze Wörtertabelle je Seite; Seiten mit mehr als etwa 25 Items oder 10 Übungen kürzen.
- Englische Aufgaben enthalten kein deutsches Wort; der Cue ist englisch. Mit `(a|b)` gleichwertige Antworten zulassen; `punctuation: ok`.
- Audio: Jeder Hörsatz endet auf ein zweisilbiges Wort, am besten einen zweisilbigen Namen (Sophie, Peter, Ellie, Amir); einsilbige Schlusswörter (map, town, park, class) hatten einen Fehllaut. „Ding“ nur für Gegenstände, nie für Menschen oder Beziehungen. Ausklingen abschneiden; Namen am Satzende zweisilbig (Sophie, Peter, Ellie, Amir).
- Bilder: Beschriftungen im `viewBox`; `alt` verrät nie die Lösung; Bildwörter ≠ Aufgabenwörter.
- Vorlage: `ordering` zeigt Auswahlfelder, `accepted` einer Sprach-Aufgabe wirkt nicht (Gruppen `(a|b)`), im Modus `choice` zeigt die App `mistakes` nicht, `punctuation: hint` meldet bei richtiger Antwort „Achte auf die Satzzeichen“.
- Kinder in Kapitel 3, besonders `vielfalt-gb`: respektvoll, keine Klischees, keine erfundenen Angaben über Religion oder Herkunft ohne Beleg; Beispiele nennen Sprachen und Feste nur allgemein.
