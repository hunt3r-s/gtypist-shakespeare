# A Python script to convert .txt files into .typ files
# For use in creating custom lessons in Gnu Typist
# Author: Hunter Smith
# Python Version: 3.10.9
import random
import os
from pathlib import Path

def remove_double_S(lines):
    """Remove the duplicated S: marker that occurs on some lines"""
    for i in range(len(lines)):
        lines[i] = lines[i].replace("S:S:", "S:")
    for i in range(len(lines)):
        lines[i] = lines[i].replace(" :S:", " :")
    return lines

def format_txt(filename):
    """Format the input .txt file.

    (1.) Splits lines > 60 characters
    (2.) Appends a " :" in front of new lines
    (3.) Randomly splits drills between 6 and 14 lines
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

        new_lines = []
        drill_length = 0  # track the number of lines since the last S:
        for i, line in enumerate(lines):
            if len(line) > 60:
                # Break lines
                split_line = [line[j:j+60] for j in range(0, len(line), 60)]
                for l in split_line:
                    if i % random.randint(4, 12) == 0:
                        # Split drills
                        new_lines.append("S:" + l.strip() + "\n")
                        drill_length = 0
                    else:
                        # Format lines
                        new_lines.append(" :" + l.strip() + "\n")
                        drill_length += 1
            else:
                if i % random.randint(4, 12) == 0:
                    # Split drills
                    new_lines.append("S:" + line.strip() + "\n")
                    drill_length = 0
                else:
                    # Format lines
                    new_lines.append(" :" + line.strip() + "\n")
                    drill_length += 1

            # Limit the minimum and maximum drill lengths
            if "S:" in line:
                drill_length = 0
            elif drill_length > 10:
                new_lines.append("S:\n")
                drill_length = 0
            elif drill_length < 6:
                new_lines.append(" :" + "\n")
                drill_length += 1

        new_lines = remove_double_S(new_lines)
        new_lines = make_lesson(new_lines, "Hamlet")
        with open(os.path.splitext(filename)[0] + ".typ", 'w') as f:
            f.writelines(new_lines)


def make_lesson(lines, title):
    """Add .typ markup

    (1.) Inserts header comment
    (2.) Inserts scene titles and their header comments
    (3.) Inserts prompt for next lesson
    """
    current_act = 1
    current_scene = 1
    i=1

    new_lines = []
    table_lines = []
    all_lines = []

    table_lines.append(" :DEMO_0  \"1:         Warmup\"\n")
    for line in lines:
        if line.startswith(" :ACT ") or line.startswith("S:ACT "):
            current_act = ''.join(x for x in line if x.isdigit())
        if line.startswith(" :Scene ") or line.startswith("S:Scene "):
            current_scene = ''.join(x for x in line if x.isdigit())
            table_lines.append(f" :DEMO_{i}  \"{i+1}:         Act {current_act} Scene {current_scene}\"\n")
            new_lines.append(f"Q:Continue to Act {current_act} Scene {current_scene}?[Y/N]\n")
            new_lines.append("N:MENU\n")
            new_lines.append(f"G:DEMO_{i}\n")
            new_lines.append("#------------------------------------------------------------------------------\n\n")
            new_lines.append("#------------------------------------------------------------------------------\n")
            new_lines.append(f"# Act {current_act} Scene {current_scene}\n")
            new_lines.append("#------------------------------------------------------------------------------\n")
            new_lines.append(f"*:DEMO_{i}\n")
            new_lines.append(f"B:Act {current_act} Scene {current_scene}\n")
            new_lines.append(f"T:This lesson covers Act {current_act} Scene {current_scene} of Shakespeare’s {title}\n")
            new_lines.append("E: 2.5%\n")
            new_lines.append("S:\n")
            i = i + 1

        new_lines.append(line)

    # Combine all lines and return as single string
    all_lines.append(f"""# GNU Typist - improved typing tutor program for UNIX systems
# Copyright (C) 1998  Simon Baldwin (simonb@sco.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This lesson was written by Hunter Smith | https://github.com/hunt3r-s
#
#
#------------------------------------------------------------------------------
# {title}
#------------------------------------------------------------------------------\n""")
    all_lines.append("*:MENU\n")
    all_lines.append(f"M: \"{title}\"\n")
    all_lines.extend(table_lines)
    all_lines.append("""#------------------------------------------------------------------------------
# Warmup
#------------------------------------------------------------------------------
*:DEMO_0
B:Warmup
T:In this lesson, you will type the entire play of
 :{title}, by William Shakespeare.
 :This play contains between 20,000 and 50,000 words
 :Since these lessons were automatically generated, you may encounter
 :lessons thst are split at unintuitive points. I like to think these add to the challenge.\n""".format(title=title))
    all_lines.extend(new_lines)
    return "".join(all_lines)


#filename = "hamlet.txt"
#format_txt(filename)

folder = 'shakespeare'
files = [f for f in os.listdir(folder) if f.endswith('.txt')]
for file in files:
    format_txt(folder + '/' + file)
