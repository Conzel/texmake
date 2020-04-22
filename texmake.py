#!/usr/bin/python3
import json
import os

# ------------------------ data_section -------------------------------------------------------------------------------
# contain tex data segments that need to be added in the header
AUFGABEN_DEFINITION = r'\newcommand{\Exercise}[1]{{ \vspace*{0.5cm}' \
                      + "\n" r'\textsf{\textbf{Exercise #1}}' \
                      + "\n" + r'\vspace*{0.2cm}' + "\n\n" r'} }' + "\n"
TEIL_DEFINITION = r'\newcommand{\Part}[1]{{ \vspace*{0.2cm}' \
                  + "\n" r'\textsf{\textbf{(#1}}' \
                  + "\n" + r'\vspace*{0.2cm}' + "\n\n" r'} }' + "\n"
# ---------------------------------------------------------------------------------------------------------------------

_BASE_DIR = dir_path = os.path.dirname(os.path.realpath(__file__))


def generate_config():
    """Interactively constructs json config from user input. """
    config = {}
    print("Enter the following values... ")
    config["lecture"] = input("Name of the lecture: ")
    config["tutor"] = input("Name of the tutor: ")
    config["semester"] = input("Current Semester: ")
    config["folder_name"] = input("Name of the folder (without numbering, e.g. sheet, week...): ")
    config["base_folder"] = input("The folder where the exercises should be created (. for this folder): ")
    num_student = int(input("Number of students working together: "))
    config["student_list"] = []
    for i in range(1, num_student + 1):
        name = input("Enter name of student %d: " % i)
        number = input("Enter number of immatriculation of student %d: " % i)
        student = {"name": name, "number": number}
        config["student_list"].append(student)
    with open("config.json", "w+") as outfile:
        json.dump(config, outfile, indent=4)
    return


def create_base_file(num_exercises, num_sheet, skeleton_file_name="../skeleton.tex", exercise_subfolder="exercises",
                     config_file_name="../config.json"):
    """Creates a tex base file, consisting of:
        - skeleton: pastes user defined preamble at the top
        - head: contains information about the user (gained from the config file), does the design of the base
        - body: contains stubs, where imports from the exercise sheets are placed
    Input:
        num_exercises: int
        num_sheet: int
    Output:
        base file with name "main.tex"
    """
    out_string = ""
    # loads skeleton file as header (skeleton should contain preamble, but no actual document text!
    with open(skeleton_file_name, "r") as skeleton_file:
        skeleton_content = skeleton_file.read()
        out_string += skeleton_content + "\n"

        # import/fancyhdr is needed to place the exercise files in the main file
        if r'\usepackage{import}' not in skeleton_content:
            out_string += r'\usepackage{import}' + "\n"

        if r'\usepackage{fancyhdr}' not in skeleton_content:
            out_string += r'\usepackage{fancyhdr}' + "\n"

    # gets json file that was generated using generate_config
    with open(config_file_name, "r") as config_file:
        config_dict = json.load(config_file)

    # constructs header from config_files, adds it to out_string
    out_string += r'\lhead{\sf \large %s' % config_dict["lecture"]
    for student in config_dict["student_list"]:
        out_string += r'\\ \small %s - %s' % (student["name"], student["number"])
    out_string += "}\n"
    out_string += r'\rhead{\sf %s \\ Tutor: %s}' % (config_dict["semester"], config_dict["tutor"]) + "\n"
    out_string += r'\pagestyle{fancy}' + "\n"

    # defines custom commands
    out_string += AUFGABEN_DEFINITION + TEIL_DEFINITION

    # sets author and title, uses first student listed as author
    out_string += "\n" + r'\title{Exercise Sheet %d}' % num_sheet \
                  + "\n" + r'\author{%s}' % config_dict["student_list"][0]["name"] + "\n"

    # bold title on the exercise sheet itself
    out_string += "\n" + r'\begin{document}' + "\n" \
                  + r'\vspace*{0.2cm}' + "\n" \
                  + r'\begin{center}' + "\n" + r'\LARGE \sf Exercise Sheet %d' % num_sheet + "\n" \
                  + r'\end{center}' + "\n" \
                  + r'\vspace*{0.2cm}' + "\n"

    # create stubs for exercise imports
    for i in range(1, num_exercises + 1):
        out_string += "\n" + r'\Exercise %d' % i + "\n" + r'\import{%s/}{exercise_%d.tex}' % (exercise_subfolder, i) \
                      + "\n"

    # doucment finished, write outstring to file
    out_string += "\n" + r'\end{document}'

    with open("main.tex", "w+") as f:
        f.write(out_string)

    return


def create_exercise_files(num_exercises, exercise_subfolder="exercises"):
    """
    Creates the exercise files, which are imported into main (see "create_base_file").
    The function creates one folder for every exercise on the current sheet and places a stub file in it
    """
    if os.path.exists(exercise_subfolder):
        raise ValueError("Exercise folder already exists for this exercise. Aborting function to not overwrite data.")

    os.mkdir(exercise_subfolder)
    os.chdir(exercise_subfolder)
    for i in range(1, num_exercises + 1):
        with open("exercise_%d.tex" % i, "w+") as file:
            file.write(r'\textbf{This exercise is still missing.}')
    os.chdir("..")


if __name__ == "__main__":
    print("Checking for Skeleton file...")
    if not os.path.exists("skeleton.tex"):
        print("No skeleton file has been detected. Please create a file named skeleton.tex,"
              + " only containing your desired preamble. This will act as a template for further files.")

    print("Checking for Configuration file...")
    if not os.path.exists("config.json"):
        print("No config has been detected. A new one will be interactively created. Follow the instructions.")
        generate_config()
        print("The config file has been created. Please restart the program if you wish to continue.")
        exit()

    num_sheet = int(input("Please input the number of the exercise sheet: "))

    with open("config.json", "r") as config_file:
        config = json.load(config_file)
        sheet_folder = config["folder_name"] + ("%02d" % num_sheet)
        os.chdir(config["base_folder"])
    if os.path.exists(sheet_folder):
        raise ValueError("There exists already a folder for this sheet: %s." % sheet_folder
                         + "Please delete it and restart the program.")

    os.mkdir(sheet_folder)
    os.chdir(sheet_folder)

    num_exercises = int(input("Please input the number of exercises on this sheet: "))
    create_base_file(num_exercises, num_sheet, skeleton_file_name=os.path.join(_BASE_DIR, "skeleton.tex"),
                     config_file_name=os.path.join(_BASE_DIR, "config.json"))
    create_exercise_files(num_exercises)
