# texmake

Small python program and support files for automatically generating sensible folder layout and latex data for usage exercises.
German language only.

## Verwendung

Benötigt: Python3

Zur Verwendung muss einfach das Repository an den gewünschten Platz geklont werden:
```
git clone https://github.com/Conzel/texmake/
```

Danach wird die file "texmake.py" ausgeführt. Die restliche Erstellung passiert interaktiv. 

1.  Zuerst wird eine Konfigurationsdatei erstellt. Diese kann auch danach beliebig editiert werden. 
2.  Beim jedem weiteren Start von "texmake.py" wid die Nummer des derzeitigen Blattes sowie die Anzahl der Aufgaben abgefragt. Daraufhin wird folgende Ordnerstruktur erstellt:
  ```
sheet_x
│   main.tex
└───exercises
│   │   exercise_1.tex
│   │   exercise_2.tex
|   |   ...
```
Die main.tex file beinhaltet die Präambel, den Code für den Header sowie Eintrittspunkte für die files im exercise Ordner. Zur Bearbeitung der Aufgaben müssen dann einfach die exercise_x.tex Aufgaben bearbeitet werden. Die main.tex file fügt diese bei der Kompilierung automatisch an die richtige Stelle ein.

## Konfiguration

Es gibt zwei Dateien, die zur Konfigurierung verwendet werden. Einmal die "config.json" Datei, die interaktiv erstellt wird. Diese kann jederzeit auch manuell bearbeitet werden und stellt die Header-Informationen zur Verfügung.

Außerdem gibt es die "skeleton.tex" Datei. Diese stellt die Präambel für die main.tex Datei zur Verfügung. In diese können nach Belieben weitere Präambel-Definitionen (usepackages etc.) reingeschrieben werden, die benötigt werden. Die zur Verfügung gestellte skeleton.tex Datei ist nur eine persönliche Empfehlung und kann jederzeit komplett ersetzt werden. Veränderungen werden nicht interaktiv übertragen, um Änderungen zu übernehmen muss der alte Ordner des Übungsblatts gelöscht und über "texmake.py" neu erstellt werden.
