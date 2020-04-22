# texmake

Small python program and support files for automatically generating sensible folder layout and latex data for usage exercises.

## Usage

Requires: Python3

To use, just clone the repository to the desired location.
```
git clone https://github.com/Conzel/texmake/
```

Execute the file texmake.py. The rest happens interactively

1.  First, a configuration will be created. This is in readable json and can also be edited later.
2.  After every start thereafter, the script will ask you for the number of the current exercise sheet and the number of exercises.
  ```
sheet_x
│   main.tex
└───exercises
│   │   exercise_1.tex
│   │   exercise_2.tex
|   |   ...
```
The main.tex file contains the preamble, the code for the header as well as the includes of the exercises. To edit the exercises, please just work with the exercise_x files.

## Konfiguration

There are two files for configuration. One is the "config.json" file, which is interactively created. It contains metadata about the students like Number of Immatriculation, Names... You can later edit this one by hand, should something change or if you made a mistake at creation.

The next one is the "skeleton.tex" file. This one creates the preamble for the main file. You can add various usepackages as you need in this. The provided skeleton file is just a recommendation and can be replace at will. To apply the changes of the skeleton file, you will have to re-create the exercise folder.
