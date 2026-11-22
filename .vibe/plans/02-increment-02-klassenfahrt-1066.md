---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, as in the app's first plan. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: explore
# prePushFailures: failed pre-push runs of this increment, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Increment: increment-02-klassenfahrt-1066

<!--
For you, the assistant. One increment of a published app: new competencies, chapters, pages, rounds, questions, or a
correction. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Content method and Retrospective, in the creator's
  language. Delete the comment of a section once the section is filled.
- The first version's decisions stand: archetype, content method, content guide. Never change an earlier plan.
- Work on the branch `increment/<NN>-<short name>`. Until Commit everything is local: push nothing.
-->

*Started 2026-11-22. Explore, Plan, Code, Commit.*

## Goal

Jugendliche der Stufe 7-8 (13 bis 14) reisen mit Sophie und der Klasse nach London (Fahrkarten, U-Bahn, Pläne lesen, London als Großstadt, Klischees hinterfragen) und lernen anhand von Lesestücken, was 1066 geschah, was die Tudors bedeuteten und wie Großbritannien heute regiert wird. Die Karte bekommt eine Zeitleiste.

## Key decisions

- Inkrement `increment/02-klassenfahrt-1066`: Kapitel 4 „Klassenfahrt nach London“ und 5 „Von 1066 bis Westminster“ (Stufe 7-8) im selben Repository, Archetyp und Inhaltsführer der ersten Version gelten (Startnachricht, Konventionen Abschnitt 8).
- Form wie Abschnitt 8: Sophie 13 bis 14, ein **Lesestück** je Seite (150 bis 300 Wörter: Chat, Reisebericht, Blogeintrag, kurzer Sachtext), Vorwissen-Frage, Randglossar, Aufgaben in drei Stufen (Verstehen, Belegen mit Zeile, Meinung), Schreib- oder Sprechauftrag; ein Bild nur wo es etwas zeigt.
- Eigentexte nach Fakten; keine fremden Sätze; jede Tatsache mit geöffneter Quelle im Inhaltsführer, sonst weglassen.
- Das erste Bündel (Kapitel 1 bis 3) bleibt unverändert; neue Seiten, Bilder und Audio kommen dazu, `src/app.yaml` bekommt die Kapitel 4 und 5.
- Wiederholungsseite nur für `uhrzeit` (#470) vor `reisen-verkehr` (aus `requires`); alle anderen Voraussetzungen stehen in Kapitel 1 bis 5. (aus der Karte)
- Zeitleiste: Block `timeline` mit Datendatei `src/data/ereignisse.yaml` (Römer bis heute), die Seite `von-1066-bis-westminster` zeigt sie. (guess)
- `scope` bleibt auf allen Seiten (wie die erste Version, wegen `open-task`).
- Heikle Themen (Politik, Klischees, Herkunft): neutral, mehrere Sichtweisen, kein Belehren, keine erfundenen Angaben zu Religion oder Herkunft realer Gruppen.

## Notes

**Quelle des Auftrags:** Issue lernapps/apps#478 (Kapitel 4 und 5), Konventionen Abschnitt 7 und 8, Muster: die erste Version dieser App (Kapitel 1 bis 3, Plan von Millbrook, Schemakarten, `make_images.py`, Hörliste). Karte `https://lernapps.net/apps/map/englisch.json` (Einheiten-App `subject: englisch`, Band 7-8).

**Neue Bausteine nach Kapitel** („Ich kann“-Sätze aus der Karte, nicht umformuliert):
4. `klassenfahrt-london` („Klassenfahrt nach London“): Wiederholung `recap: englisch/uhrzeit` (`das-brauchst-du`, #470), dann `reisen-verkehr` (wortschatz, Schritt 1; braucht uhrzeit), `london-heute` (landeskunde, 1; braucht london-sehenswuerdigkeiten und vielfalt-gb, beide in Kapitel 3), `stereotype` (landeskunde, 1; braucht vielfalt-gb).
5. `von-1066-bis-westminster` („Von 1066 bis Westminster“): `normannen-1066` (landeskunde, 1; braucht roemer-in-britannien), `tudors` (2; braucht normannen-1066), `politik-uk` (1; braucht britische-inseln). Reihenfolge nach der Zeit: Normannen → Tudors → Politik heute (Westminster am Ende, wie das Issue sagt).
Von außen braucht die Karte nur `uhrzeit` (#470) für Kapitel 4.

**Form (Abschnitt 8):** Ein Lesestück je Seite, 150 bis 300 Wörter, Sophie 13 bis 14: Kapitel 4 Nachrichten und Chats der Klassenfahrt (Reisebericht, Ticket-Dialog, Blogeintrag, Diskussion), Kapitel 5 kurze Sachtexte mit Zeitleiste (eigene Texte nach Fakten) und ein Schaubild. Aufbau jeder Seite: Vorwissen-Frage, Lesestück in Abschnitten mit Randglossar (Tabelle „Randglossar“ oder `definition`), Aufgaben in drei Stufen (Verstehen, Belegen mit Zeile, Meinung), Schreib- oder Sprechauftrag, Hörsätze nur in kurzen Abschnitten; höchstens etwa 25 Items. Die Länge des Lesestücks zählt nicht zu den 350 Wörtern Erklärtext.

**Wie die Jugendlichen dorthin kommen und welchen Fehler die Rückmeldung fängt (eine Zeile je Baustein):**
- `reisen-verkehr`: Chat der Klasse mit Mr Hill (Zug von Millbrook nach London, Abfahrtszeit, Gleis, U-Bahn-Fahrkarte), dann Dialog am Schalter (a single or return ticket, which platform); sie entnehmen Zeiten (Uhrzeit aus der Wiederholung) und kaufen selbst eine Fahrkarte. Fehler: single/return verwechselt, „Which platform leaves the train?“, `by train` / `with the train`, Abfahrt/Ankunft.
- `london-heute`: Blogeintrag oder Reisebericht von Sophie über einen Tag in London (Themse, Westminster, Straßen, Märkte, Museen); London als Großstadt der vielen Sprachen und Orte, Zentrum von Wirtschaft (Büros, Banken, Hafen/Stadt) und Kultur (Theater, Museen); nur Fakten mit Quelle, keine Bevölkerungszahlen ohne Beleg. Fehler: London als nur „Touristenstadt“, Verwechslung von Wirtschaft und Kultur, Zahlen ohne Beleg.
- `stereotype`: Chat der Klasse: Was denken Briten über Deutsche, was Deutsche über Briten (Tea, Rain, „always punctual“ ohne Wertung); die Jugendlichen unterscheiden Beobachtung, Verallgemeinerung („all“, „always“, „never“) und Vorurteil und prüfen eine Aussage an Beispielen aus London. Neutral, ohne Belehrung. Fehler: „All British people drink tea“ als Tatsache, ein Einzelfall als Beleg, „some“ und „all“ verwechselt.
- `normannen-1066`: Sachtext „Hastings 1066“ (14 Oktober 1066, Harold Godwinson, William of Normandy, Tower of London), Zeitleiste; die Jugendlichen leiten ab, wie Französisch Englisch veränderte (Middle English, Anglo-Norman French). Wörter wie beef/cow oder pork/pig nur, wenn eine geöffnete Quelle sie belegt. Fehler: 1066 mit den Römern oder Wikingern verwechselt, „William became king in Hastings“.
- `tudors`: Kurztext über Henry VIII (König 1509 bis 1547, sechs Ehen, Church of England) und Elizabeth I (Königin 1558 bis 1603, letzte Tudor); Zeitleiste; was bedeutete das für England. Fehler: Henry und Elizabeth vertauscht, Jahreszahlen ohne Reihenfolge.
- `politik-uk`: Schaubild König (Charles III) – Parlament (House of Commons, House of Lords) – Premierminister (Regierungschef); wer macht was; neutral, keine Parteien, keine Wertung. Fehler: König regiert allein, Premierminister = Staatsoberhaupt, Parlament = nur ein Haus.

**Umfang:** drin: 6 Bausteine (Kapitel 4 und 5), 2 Kapitel, 1 Wiederholungsseite, Zeitleiste mit Datendatei, Hörtexte in kurzen Abschnitten. Draußen: Fotos und Videos (keine geprüfte Lizenz), Parteien und Wahlen, USA/Kanada/Australien (#484), die Reformation im Detail, Elizabethan-Theater.

**Quellen (alle nur Fakten, CC BY-SA, geöffnet 2026-11-22, Wikipedia en):** `William the Conqueror` (erster normannischer König, 1066 Sieg bei Hastings über Harold Godwinson), `Battle of Hastings` (14. Oktober 1066, rund 11 km nordwestlich von Hastings, nahe Battle, East Sussex), `Norman Conquest`, `Middle English` (nach 1066, Einfluss des Anglo-Norman French), `Tower of London` (gegründet gegen Ende 1066, White Tower 1078), `Henry VIII` (König 22. April 1509 bis 1547, sechs Ehen, Bruch mit der römisch-katholischen Kirche, Church of England), `Elizabeth I` (Königin 17. November 1558 bis 1603, letzte Tudor-Monarchin), `Parliament of the United Kingdom` (House of Commons, House of Lords, Souverän, Palace of Westminster), `Monarchy of the United Kingdom` (seit 8. September 2022 King Charles III), `Prime Minister of the United Kingdom` (Regierungschef, braucht das Vertrauen des House of Commons), `Constitutional monarchy`, `Palace of Westminster`, `London Underground` (nur Fakten ohne Zahlen), `Stereotype` (Begriff). **Nicht geöffnet (HTTP 429):** `Tudor period`, `Anglo-Norman language`, `History of the English language`, Zahlen zu London (Bevölkerung, Wirtschaft). Nur zugelassene Textquellen (VOA, Wikinews) wären als Ganzes übernehmbar; ich schreibe Eigentexte nach Fakten und übernehme keine Sätze. Material der Ersteller:in: keines. Deutsche Wikipedia und Klexikon nicht gelesen.



## Explore

<!--
- All content questions belong here; Plan maps the answers onto the app. Ask; write no code.
- Skip what earlier answers or the app already tell. At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Read the README of the archetype's template (its path is in skill `lernapps-app`): what the app can do now.
      Tell the creator what is new, if it matters for this increment.
- [x] Load the content guide `.agents/skills/app-content/SKILL.md` and read the earlier plans in `.vibe/plans/`: what
      the app teaches, how its content is made, what is open.
- [x] Interview, one topic per question, the creator's words under "Answers": which competencies, chapters or rounds,
      for which school years; hurdles and examples; the amount; any change of look and feel or of terms. No answer:
      ask once more, then write your assumption with "(guess)".
- [x] Load skill `lernapps-content-research`. Research what the content guide does not cover. Write under "Notes":
      the new competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" the didactic approach per competency and the scope (in, out, data range).
- [x] The increment needs a kind of content the guide does not cover (a new page structure, screen, component or kind
      of exercise): load skills `lernapps-explainer-design` and `lernapps-exercise-patterns`. Else skip this task.
- [ ] **Checkpoint:** research. Show in plain words: the new competencies by chapter, the didactic approach, the
      scope, every "(guess)", the sources and what is unchecked. Stop and wait. Changes: change them, then ask again.

### Answers

- Auftrag (Issue 478, Kapitel 4 und 5): „Ich kann eine Reise organisieren, London als vielfältige Großstadt beschreiben und Klischees über Länder hinterfragen.“ und „Ich kann erklären, was 1066 geschah, die Bedeutung der Tudors beschreiben und sagen, wie Großbritannien heute regiert wird.“ Kapitel 4: „Die Klasse reist mit Zug und U-Bahn; die Kinder kaufen Fahrkarten und lesen Pläne. In London sammeln sie Klischees über Briten und Deutsche und prüfen sie an dem, was sie sehen.“ Kapitel 5: „Erweitert die Karte um eine Zeitleiste. Orte bekommen Geschichte: Hastings, der Tower, Westminster. Die Zeitleiste endet im Parlament von heute: König, Parlament und Premierminister als Schaubild.“
- Orchestrator-Session (in der Rolle der Ersteller:in), 2026-11-22: „Baue die Kapitel 4 und 5 als Inkrement … hier tragen Lesestücke die Seiten … Quellen: Eigentexte nach Fakten; VOA, Wikinews als erlaubte Textquellen … Geschichtsfakten nur mit geöffneter Quelle im Inhaltsführer. Vorschau-Pull-Request offen lassen, nichts nach main, kein Katalogeintrag.“

## Plan

<!--
- Map the new content onto the app with the guide's patterns. The creator confirms the plan in one read.
- After the yes you work on your own.
-->

### Tasks

- [ ] Load skill `lernapps-content-growth`. Add the tasks of Code as slices, one per competency, in the guide's
      order, one call each: `npx --no -- lernapps plan add --at slices "<task>"`. Say in each which sub-agent may
      write it in parallel, if any.
- [ ] Write "Content method": the guide's patterns, figures and components per slice. Anything new: map it as skill
      `lernapps-explainer-design` says, and say why the guide's patterns do not fit.
- [ ] Draw a sketch of each new component or interactive exercise, in `.vibe/sketches/`.
- [ ] Show the creator, short: goal, new competencies by chapter, slices; in plain words what learners see and do and
      what is new. At most 2 questions.
- [ ] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.

### Content method

<!-- One line each: the guide's patterns, figures and components used, and where; anything new, what it does and
cannot. Something new goes into the guide in the slice that adds it. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

## Code

<!--
- Build locally on the branch, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first.
-->

### Tasks

- [ ] `git switch -c increment/<NN>-<short name>` from `main`. Commit this plan on it.
- [ ] Load skill `lernapps-cli`. Update the app as its section "Update" says. Commit the update alone and fix its
      findings before any content. The update replaces the `lernapps-*` skills: read again those you use.
- [ ] Load skill `lernapps-explainer` and the content guide.
- [ ] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [ ] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
<!-- tasks: slices: one per competency, as written in Plan -->
- [ ] **Checkpoint:** the pattern page, after the first slice. A slice in a pattern the app already has: show it to
      the creator and go on. A new pattern: load skill `lernapps-learner-check`, do its learner check, fix what it
      finds, then ask the creator whether the others may follow it, and wait.
- [ ] Update the content guide so that it describes the app as it is now (`app-content-matches`).
- [ ] Run `npx --no -- lernapps check` until it passes.
- [ ] Look at every changed screen, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.

## Commit

<!--
- Publish with the creator's yes. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
-->

### Tasks

- [ ] If pages or exercises changed, load skill `lernapps-explainer-self-assessment` and update the self-assessment
      as it says. Commit.
- [ ] Load skill `lernapps-github`. Push the branch, open the preview pull request and see its checks to green, as it
      says.
- [ ] **Checkpoint:** publish. Show what the increment adds and the preview link. Ask whether it may go online. Stop
      and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: the pull request squash-merged into
      `main`, the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm the new content. Never use a derived address.
- [ ] The app is listed and its entry changes (school years, summary): load skill `lernapps-listing` and write the
      changed entry. Else skip this task.
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it. A push of only `.vibe/` publishes nothing.
- [ ] **Checkpoint:** list. The entry changed: open the pull request to the catalog as skill `lernapps-listing`
      says, without asking first, see it to "bestanden", then show the creator the pull request and its result. The
      entry did not change: tell the creator that the catalog updates the app by itself.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

## Retrospective

<!-- At the end of Commit. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, content guide, messages or answers, and your choice. "None" if none. -->
