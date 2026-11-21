---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: code
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 2
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: { checks-pass: 5 }
---

# Plan: englisch-grossbritannien, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-21. Explore, Plan, Code, Commit.*

## Goal

Kinder im ersten und zweiten Lernjahr Englisch (Stufe 5-6) finden sich auf dem Stadtplan von Millbrook zurecht (Weg erfragen und beschreiben, einkaufen, Schilder lesen), stellen die Britischen Inseln, eine Region und London mit den Römern und der Vielfalt seiner Menschen vor. Die Karte zoomt heraus: Stadtplan, Britische Inseln, London.

## Key decisions

- Archetyp `explainer`: Kinder lesen erklärende Seiten mit Bild und üben dazwischen (Issue: „Einheiten-App über mehrere Stränge“, `subject: englisch`, Format 2).
- Erste Version baut nur Kapitel 1 bis 3 (Stufe 5-6, 9 Bausteine); Kapitel 4 und 5 (Stufe 7-8) kommen als Inkremente (Vorgabe der Startnachricht).
- Hauptfigur heißt Sophie (nicht Lena), kein Josh (Konventionen Abschnitt 7).
- Kapitelreihenfolge innerhalb der Kapitel nach Geschichte, nicht nur nach Schritt: Kapitel 1 Stadt → Schilder → Laden; Kapitel 3 Römer (Londinium) → Sehenswürdigkeiten → Vielfalt (Issue: „am Anfang steht Londinium“). Alle `requires` stehen vorher oder auf der Wiederholungsseite. (guess)
- Wiederholungsseiten (`recap`, ohne Übung): Kapitel 1 `praepositionen-ort` (#475), `imperativ` (#473), `zahlen` (#470); Kapitel 2 `vergleiche` (#476). Kapitel 3 braucht von außen nichts. (aus den `requires` der Karte)
- Neue Orte: Stadtplan von Millbrook (Hauptstraße, Bibliothek, Bäckerei, Bahnhof, Park, Kleidungsladen usw.), Ausflug der Parkers (Cornwall), Stadtrundgang in London. (guess)
- `scope` in `src/app.yaml` und auf jeder Seite (guess): die App hat `open-task`-Aufgaben, der Tutor beurteilt freie Antworten nur nach dem `scope` (`references/structure.md`); darum alle Seiten mit `scope`.
- Straßennamen: „the High Street“ mit Artikel, „Church Road“ und „Mill Lane“ ohne (britisch üblich), überall gleich. (guess)
- Bilder: nur eigene Zeichnungen (CC-BY-4.0); keine Fotos oder Videos, solange Lizenz und Quelle nicht geprüft sind. (guess)

## Notes

**Quelle des Auftrags:** Issue lernapps/apps#478 (Epic #489, Konventionen Kopie in `/tmp/auftraege/orchestrierung/`). Muster: hello-millbrook (#470) und die Vorschauen von #475, #476, #473, #472 (Branch `work`).

**Fach:** Einheiten-App `subject: englisch` (Karte `https://lernapps.net/apps/map/englisch.json`, Fokus `competency`; geöffnet 2026-11-21). Stränge der Seiten: `wortschatz`, `texte`, `landeskunde`. Alle neun Bausteine sind Lücken der Karte (`practisedBy` leer), Band 5-6.

**Bausteine nach Kapitel** („Ich kann“-Sätze aus der Karte, nicht umformuliert):
1. `wege-laeden-schilder` („Wege, Läden und Schilder“): Sammel-Wiederholung `recap: [englisch/praepositionen-ort, englisch/imperativ, englisch/zahlen]` (`das-brauchst-du`), dann `stadt-wegbeschreibung` (wortschatz, Schritt 3; braucht praepositionen-ort, imperativ), `alltagstexte` (texte, Schritt 1), `kleidung-einkaufen` (wortschatz, Schritt 2; braucht zahlen).
2. `britische-inseln` („Die Britischen Inseln“): Wiederholung `recap: englisch/vergleiche` (`das-brauchst-du`), dann `britische-inseln` (landeskunde, Schritt 1), `region-uk` (2), `stadt-land-uk` (6; braucht britische-inseln und vergleiche).
3. `london` („London“): `roemer-in-britannien` (2), `london-sehenswuerdigkeiten` (2), `vielfalt-gb` (1). Alle brauchen nur `britische-inseln` aus Kapitel 2. Keine Wiederholungsseite.
Von außen braucht die Karte: `praepositionen-ort` (#475), `imperativ` (#473), `zahlen` (#470), `vergleiche` (#476); deren Seiten liegen als Vorschau vor, Links gehen auf die Karte. Kapitel 4 und 5 (Stufe 7-8) sind nicht Teil dieser Session; ihre Bausteine bleiben Lücken.

**Didaktik:** Die Karte zoomt heraus und trägt den Explainer: Kapitel 1 ein Stadtplan von Millbrook (Quadratraster, Straßen, Orte mit Namen), Kapitel 2 die Karte der Britischen Inseln (vereinfachte eigene Umrisse, kein Foto), Kapitel 3 ein Plan von London mit Themse und den Halten des Rundgangs. Figuren und Seitenaufbau wie in den Vorgängern (`einstieg`, `neu`, `uebung`, `anwenden`, `weiter`). Geschichte (guess): Kapitel 1 Stadtbummel mit Mrs Parker am Samstag, Kapitel 2 Ausflug der Parkers nach Cornwall in den Herbstferien, Kapitel 3 London mit Mr Hills Klasse (ein Tag; die „Klassenfahrt“ selbst ist Kapitel 4). Neue Orte (Stadtplan von Millbrook, Cornwall-Ausflug, Londoner Rundgang) stehen im Inhaltsführer und werden im Plan-Checkpoint gemeldet.

**Wie die Kinder üben (Muster aus `references/foreign-languages.md`):** Plan lesen und Wege folgen (zuordnen, `ordering`, `language-task` choice/write) → Schilder, Fahrplan und Speisekarte lesen (Text/Tabelle gegeben, Information entnehmen: `single-choice`, `language-task` mode `gap`) → Kleidung und Preise (Wörter, Größe, Preis, Frage und Antwort schreiben) → Landeskunde: Karte beschriften (`matching`, `single-choice`, `true-false` mit Begründung), Region vorstellen (`open-task` mit Punkten) → Diktat und Nachsprechen auf jeder Seite (neue Sätze) → `open-task`.

**Wie sie dorthin kommen und welchen Fehler die Rückmeldung fängt:**
- `stadt-wegbeschreibung`: Kinder gehen den Weg auf dem Plan (Pfeile), leiten Sätze aus turn left/right, go straight on, next to, opposite, behind ab. Fehler: „turn to left“, „go straight“ ohne on, next/near vertauscht, Imperativ mit You.
- `alltagstexte`: Textsorten an Merkmalen erkennen (Schild kurz, Fahrplan Tabelle mit Uhrzeiten, Speisekarte Preise, Flyer Datum/Ort) und gezielt eine Information suchen. Fehler: Uhrzeit/Preis verwechseln, Gleis statt Abfahrt, am ersten Wort hängen bleiben.
- `kleidung-einkaufen`: Laden-Szene mit Preisschild; Kleidung benennen, nach Größe und Preis fragen (How much is …? Have you got … in a larger size?). Fehler: trousers/jeans Singular („a trousers“), How much are/is, £-Zahl schreiben/sprechen.
- `britische-inseln`: Puzzle England/Schottland/Wales/Nordirland mit Hauptstädten; UK, Great Britain, Ireland trennen. Fehler: UK = England, Great Britain = UK mit Nordirland, Ireland = Nordirland, Hauptstädte vertauscht (Dublin/Belfast).
- `region-uk`: eine Region (Cornwall) an Steckbrief-Kärtchen lesen und mit eigenen Sätzen vorstellen (It is in …, You can …). Fehler: Cornwall mit Wales verwechselt, Lake District im Süden.
- `stadt-land-uk`: Vergleich Millbrook/London/Land mit than und as … as. Fehler: bigger then, more busy, as busier as.
- `roemer-in-britannien`: Zeitstrahl Londinium, Hadrian’s Wall, Bath; Was hinterließen die Römer? (Straßen, Mauern, Bäder, London). Fehler: Römer = Normannen/Wikinger, Hadrian’s Wall = Grenze zu Wales.
- `london-sehenswuerdigkeiten`: Plan von London mit Halten; Sehenswürdigkeit zuordnen und mit is/has/you can beschreiben. Fehler: Big Ben = Turm statt Glocke (Hinweis), Tower Bridge/London Bridge, Buckingham Palace/Westminster.
- `vielfalt-gb`: Amirs Familie als Beispiel (Herkunft der Familie, Sprachen zu Hause, Feste); Sätze mit come from / speak. Fehler: „British = white“, Herkunft mit Staatsangehörigkeit gleichsetzen.

**Geprüft und behoben (Musterseite `stadt-wegbeschreibung`):** Lerner-Check mit Sub-Agent (Kind Klasse 5): Osten und Süden waren nicht erklärt (Kompass N im Plan, Himmelsrichtungen in der Bildunterschrift, Aufgabentext sagt, in welche Richtung man schaut); Beispielweg: Marke 1 saß nicht an der Abbiegestelle, Start ohne Punkt, Pfeil endete nicht an der Bäckerei (Marken 1, 2, 3 und Startpunkt neu); „the road“ stand nicht in der Wörter-Tabelle (jetzt „cross the road“); Merke und Wörter-Tabelle wiederholten left/right und next to/opposite (Merke gekürzt). Nicht behebbar (Vorlage): Rückmeldung bei Zuordnung und Auswahl-Lücke („nicht richtig“ ohne Grund), Standardmeldung „Deine Fassung kann trotzdem richtig sein“. Sprachprüfung Englisch/Deutsch mit Sub-Agent: „Turn to the left“ und „Go straight ahead“ sind richtig (jetzt zugelassen, Fehlertext präzisiert), „You turn right“ ist kein Fehler sondern kein Befehl (Aufgabe heißt jetzt „Mach aus jedem Satz einen Befehl“), die Reihenfolge-Aufgabe hatte zwei richtige Sätze (jetzt „Turn left into Church Road“), Genus und Hinweise korrigiert, „Schemaplan“ erklärt.

**Auflagen der Orchestrierung auf der Musterseite und zweiter Lerner-Check (Sub-Agent, Kind Klasse 5):** Beispielweg im Bild ist jetzt ein anderer (park → supermarket mit Turn left), die Lösungen der Übungen sind andere Wege; nur eine Wörter-Tabelle (bakery, post office, opposite, between, into), das Poster „Pfeile und Sätze“ entfiel; die Zuordnung bildet die Orte des Plans ab statt der Tabelle; neue Aufgabe zu Lage mit between und opposite (`wege-lage`); `into the High Street` überall gleich; Merke nennt auch „turn to the left“; Alt-Texte des Hauptplans nennen nur Straßen und Nord/Süd; Punkt 3 der freien Aufgabe gefasst; Inhaltsführer gefüllt. Zweiter Lerner-Check fand: Cue zu `wege-lage` verriet die Antwort (jetzt „…“), Hinweis „auf dem Plan rechts“ in `wege-plan` Item 3 irreführend (entfernt). Bewusst nicht geändert: Rückmeldung der Vorlage bei Auswahl-Lücken und Schreibaufgaben („nicht richtig“ ohne Grund), Einstiegsfrage mit opposite vor der Tabelle (Lösung durch Ausschluss, `info` erklärt es), `explainer-text-load` als Hinweis (510 Wörter in Aufgaben und Meldungen).

**Umfang:** drin: 9 Bausteine, Kapitel 1 bis 3 (2 Wiederholungsseiten, 9 Inhaltsseiten), Wörter aus A1/A2, Aussprache über Hörtexte, `speaking-task`, `open-task`. Draußen: Kapitel 4 und 5, Fotos und Videos (keine Lizenz geprüft), Politik und Tudors/Normannen. Sprache: Deutsch (englische Beispiele), keine englische Fassung (guess, wie die Vorgänger).

**Quellen (alle nur Fakten, CC BY-SA, geöffnet 2026-11-21):** Wikipedia en: `United Kingdom`, `Great Britain`, `British Isles`, `Republic of Ireland`, `Cornwall`, `Lake District`, `London`, `Londinium`, `Hadrian's Wall`, `Roman Baths (Bath)`, `Tower of London`, `Big Ben`, `Buckingham Palace`, `London Eye`, `Tower Bridge`, `British Museum`, `Languages of the United Kingdom`. Nicht geprüft (HTTP 429): `Roman Britain`, `Demography of London`; Zahlen zur Bevölkerung Londons werden nicht verwendet, bis sie geprüft sind. Deutsche Wikipedia und Klexikon nicht gelesen. Karte `https://lernapps.net/apps/map/englisch.json`; Grundwortschatz `https://lernapps.net/apps/map/englisch/grundwortschatz/`. Beispielsätze eigene. Fotos und Videos: keine. Material der Ersteller:in: keines.


## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Du darfst es ausführen!

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

- Goal: „Ich kann mich in einer britischen Stadt zurechtfinden und Großbritannien mit seinen Teilen, mit London und einigen Stationen seiner Geschichte vorstellen.“ Eine Karte, die herauszoomt, trägt den Explainer: zuerst der Stadtplan von Millbrook, dann die Britischen Inseln, dann London. Sophie und die Parkers sind unterwegs: Stadtbummel, Ausflug in eine Region, Klassenfahrt nach London. (Issue 478, Didaktik)
- Learners: Englisch, Stufe 5-6 (erstes und zweites Lernjahr); Vorwissen aus Hello, Millbrook! (#470), Pronomen, Zeiten, Sätze bauen, Dinge/Mengen/Orte, Adjektive/Adverbien (Auftrag und Konventionen).
- Model and focus: hello-millbrook (#470) und die fertigen Vorschauen #475, #472, #473, #476 (Startnachricht); Schwerpunkt: die herauszoomende Karte (Stadtplan von Millbrook, Britische Inseln, London) trägt den Explainer, mit den bekannten Figuren als Beispielen.
- Hurdles: UK, Great Britain und Ireland verwechseln; Klischees; Schilder und Fahrpläne nicht gezielt lesen (aus Issue 478, Kapitel 1 bis 3; Fehlerbilder stehen in Notes).
- Content: aus dem Issue 478 und der Karte; Fakten aus Wikipedia (nur Fakten), eigene Beispielsätze und Zeichnungen; Fotos und Videos nur mit geprüfter CC-Lizenz und Quelle im Inhaltsführer (Startnachricht). Material der Ersteller:in: keines.
- Amount: Kapitel 1 bis 3 (Stufe 5-6, 9 Bausteine); Kapitel 4 und 5 (Stufe 7-8) später als Inkremente (Startnachricht).
- Languages: Deutsch mit englischen Beispielen (Konventionen Abschnitt 4).
- Look and feel: fixed by the archetype.
- Terms: „Ausdruck“ (nie „Wendung“), noun, verb, adjective, sentence; Tabellen „Klassenzimmer-Poster · …“ und „Schulkalender · …“; Anrede „du“ (Konventionen Abschnitt 4).
- Finding the app: Großbritannien, London, Stadtplan, Weg beschreiben, Englisch Landeskunde (guess, aus Titel und Leitidee des Issues).

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Orchestrator-Session (in der Rolle der Ersteller:in): Ja, Plan bestätigt

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

**Wörter:** Quelle ist der Grundwortschatz Englisch (`https://lernapps.net/apps/map/englisch/grundwortschatz/`, A1/A2). Übungen fragen A1/A2-Wörter ab; Wörter außerhalb (Landeskunde: Roman, wall, castle, tower, bridge, museum, palace, island, capital, region; Läden: jumper, trousers, size) stehen vorher in genau einer kurzen Wörter-Tabelle je Seite mit Bedeutung und sind im Inhaltsführer gelistet. Eigennamen (Hadrian's Wall, Londinium) stehen im Text und in der Bildunterschrift.
**Hören und Sprechen:** ja, Stimme `bf_emma`, Skill `lernapps-audio`; je Seite 3 Diktat- und 3 Nachsprechsätze, jeweils neue Sätze (nie im Text, Poster, Merke, Bild oder in einer Aufgabe derselben Seite; Skript prüft das), `regen_audio.py` aus #470, Namen am Satzende zweisilbig.
**Übungsarten wechseln von Seite zu Seite:** Plan oder Karte lesen und zuordnen (`matching`, `single-choice`, `true-false` mit Begründung), Weg und Reihenfolge (`ordering`), Lücke (`language-task` choice/gap), Form mit englischem Cue (`write`), Tabelle füllen (`table`), Text entnehmen, Übersetzen, Korrigieren, Diktat, Nachsprechen, `open-task`. Je Übung `mistakes` mit eigener Meldung, Distraktoren nur echte Lernerfehler; höchstens eine kurze Wörtertabelle je Seite; `(a|b)` für gleichwertige Antworten; `punctuation: ok`.
**Aufbau der Seiten:** Abschnitte `einstieg`, `neu`, `uebung`, `anwenden`, `weiter` wie #476. Wiederholungsseiten: nur `einstieg` mit Text und höchstens einer Tabelle, ohne Übung und ohne `competencies`.
**Bilder (alle eigene Zeichnungen, `CC-BY-4.0`, Quelle „eigene Zeichnung“), Lernhandlung je Bild (`explainer-representation-explained`):** Erzeugt von `.agents/skills/app-content/scripts/make_images.py` (SVG aus Koordinaten; Figuren als `<g id>` aus `millbrook-klassenzimmer.svg` von #470). `stadtplan-millbrook`: Raster mit Straßen und Orten; die Kinder folgen mit dem Finger einem Pfeilweg und lesen daraus Sätze. `schilder-fahrplan-karte`: Schild, Fahrplan, Speisekarte und Flyer als gezeichnete Kärtchen; die Kinder suchen gezielt eine Information. `laden-preisschilder`: Regal mit Preisschildern und Größen. `karte-inseln`: vereinfachte, selbst gezeichnete Umrisse von Great Britain und Ireland, vier Teile eingefärbt, Hauptstädte als Punkte; die Kinder lesen Teile und Hauptstädte ab und trennen UK, Great Britain und Ireland (keine Vorlage aus Atlas oder Wikipedia kopiert). `karte-cornwall`: Skizze der Südwestspitze mit drei Orten. `zeitstrahl-roemer`: Strahl mit AD 43, um 47 bis 50, 122 (nach Prüfung der Quelle). `karte-london`: Themse und die Halte des Rundgangs; die Kinder legen die Reihenfolge fest. `familie-amir`: Szene mit Amirs Familie. Schrift mindestens 16 im 480er viewBox, `alt` nennt nie die Lösung, die Bildunterschrift nennt, wer wer ist. Keine Fotos und Videos (Lizenz und Quelle nicht geprüft).
**Keine Komponente, keine Datendatei** (`prefer-built-in-block`): Karten sind Bilder, die Aufgaben darunter prüfen das Lesen. Grenze: nichts prüft ein Klicken auf der Karte; ein Ziehen-Puzzle England/Schottland/Wales/Nordirland wäre ein Wunsch für die Vorlage, hier `matching` und Auswahl am Bild. Zeitstrahl als Bild; der Block `timeline` erst ab Kapitel 5 mit Datendatei.
**Voraussetzungen, die die App nicht übt:** Kapitel 1 `praepositionen-ort`, `imperativ`, `zahlen` (eine Sammel-Wiederholungsseite); Kapitel 2 `vergleiche` (eine Wiederholungsseite); Kapitel 3 keine.
**Seiten, eine Zeile je Seite (Einstieg · Wechsel · Belohnung · Geschichte):**
- `das-brauchst-du` (K1, ohne Übung): Sophie und Mrs Parker gehen am Samstag in die Stadt; Text, je Baustein ein Link zur Karte, Tabelle „Klassenzimmer-Poster · Das brauchst du für den Stadtplan“.
- `stadt-wegbeschreibung` (Musterseite): Sophie sucht die Bibliothek (Frage am Plan) · Plan lesen, Weg ordnen, Weg schreiben · Sophie kommt an · weiter: Schilder an der Straße.
- `alltagstexte`: Schild „Closed“ an der Tür der Bäckerei, welche Textsorte? · Merkmale erkennen, Fahrplan und Speisekarte gezielt lesen · Sophie findet die Abfahrt und das Essen · weiter: Laden.
- `kleidung-einkaufen`: Preisschild lesen (£, Zahlen) · Kleidung benennen, nach Größe und Preis fragen, Dialog im Laden · Sophie kauft eine Mütze für Peter (guess) · weiter: Wochenende, Ausflug.
- `britische-inseln` (K2): Mr Hill hängt eine Karte auf, Millbrook liegt in England · Karte lesen, zuordnen, wahr oder falsch · Kinder sortieren UK, Great Britain, Ireland · weiter: Ausflug der Parkers.
- `region-uk`: Peter fragt, wo Cornwall liegt · Steckbrief lesen, Region vorstellen · eigene Vorstellung · weiter: Vergleich Stadt und Land.
- `stadt-land-uk`: Ellie sagt „London is bigger than Millbrook“ · Vergleiche mit than und as … as auf Stadt und Land · eigener Vergleichstext · weiter: London.
- `roemer-in-britannien` (K3): Mr Hill: London ist fast 2000 Jahre alt, Londinium · Zeitstrahl lesen, zuordnen, Hinterlassenschaften · Kinder erzählen, was die Römer hinterlassen haben · weiter: Rundgang.
- `london-sehenswuerdigkeiten`: Karte von London mit den Halten · Orte zuordnen und beschreiben, Rundgang ordnen · eigene Karte für Peter · weiter: Menschen in London.
- `vielfalt-gb`: Amir stellt seine Familie vor · lesen, entscheiden, schreiben · Rückblick auf die drei Kapitel (Schulkalender · Rückblick Kapitel 1 bis 3).
**Ein Kapitel später ergänzen:** Kapitel 4 und 5 sind eigene Seiten (Stufe 7-8: Chat-Form, Reisen, Klischees, 1066, Tudors, Politik); Karte und Zeitstrahl in `make_images.py` erweitern, Poster um Zeilen ergänzen; für Kapitel 5 eine Datendatei `src/data/` und der Block `timeline`.

## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [x] Load skill `lernapps-explainer`.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Musterseite Kapitel 1 `stadt-wegbeschreibung` komplett: App-Rahmen (app.yaml, Kapitel wege-laeden-schilder), Bilder `stadtplan-millbrook` und Szene (make_images.py), alle Abschnitte, Übungen, 6 Audiosätze, Inhaltsführer
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [x] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
      Creator: Orchestrator-Session (in der Rolle der Ersteller:in): Die anderen Seiten dürfen folgen, sobald die Auflagen auf der Musterseite umgesetzt sind
- [x] Wiederholungsseite `das-brauchst-du` Kapitel 1 (praepositionen-ort, imperativ, zahlen), ohne Übung
- [x] Seite `alltagstexte` mit Bild der Schilder, Fahrplan und Speisekarte, Übungen und 6 Audiosätzen
- [x] Seite `kleidung-einkaufen` mit Laden-Bild, Übungen, 6 Audiosätzen und Selbsteinschätzung Kapitel 1
- [x] Kapitel 2: Wiederholungsseite `das-brauchst-du` (vergleiche) und Seite `britische-inseln` mit Karte der Inseln, Übungen, Audio
- [x] Seite `region-uk` (Cornwall) mit Kartenskizze, Übungen, Audio
- [x] Seite `stadt-land-uk` mit Vergleichen, Übungen, Audio, Selbsteinschätzung Kapitel 2
- [x] Kapitel 3: Seite `roemer-in-britannien` mit Zeitstrahl (Römer-Fakten gegen Wikipedia prüfen), Übungen, Audio
- [x] Seite `london-sehenswuerdigkeiten` mit Karte von London, Übungen, Audio
- [x] Seite `vielfalt-gb` mit Amirs Familie, Rückblick Kapitel 1 bis 3, Selbsteinschätzung Kapitel 3, Audio
- [x] Skript-Prüfung über alle Seiten: Hörsätze neu, Wörter vorher eingeführt, Distraktoren, mistakes je Item, Länge; Wiederholungsseiten und Karten-Verweise
<!-- tasks: pages (10 added): the other pages or screens, after the pattern -->
- [x] Update the content guide so that it describes the app as built (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [x] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [ ] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
