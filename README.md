Gnutypist Lessons
---


  [GNU Typist](https://www.gnu.org/software/gtypist/) is a typing tutor frokm the [GNU
  Project](https://www.gnu.org/). It provides a command line interface
  with guided typing lessons. It also provides a method of constructing
  your own lessons. This is a collection of Shakespeare's plays, converted into
  GNUtypist files.

# Requirements

-   [GNU Typist](https://www.gnu.org/software/gtypist/)

# Usage

Download this repository as a .zip file, place the desired .typ lessons
in `/gnu-typist/share/gtypist`.
Individual .typ files are located in `/shakespeare`.

# Development
The Python script [txt2typ.py](txt2py.py) was used to create these lessons.
Due to the script's dependance on the format of the input text, it can not be used to
generate lessons from other texts. However, the changes required would be rather minimal,
i.e, splitting lessons based on another marker other than "ACT" or "Scene"

# Lessons
Each of Shakespeare's plays are divided into .typ files. The lessons are divided
by current Act and Scene. So each scene counts as 1 lesson. The exception to this
is in "Shakespeare's Soliloquies" where all of the soliloquies are to be typed as one lesson.


# Authors

-   [\@hunt3r-s](https://github.com/hunt3r-s)

# Acknowledgements
- Thank you to the [Folger Shakespeare Library](https://shakespeare.folger.edu/) for providing well formatted
renditions of Shakespeare's plays, in plain text, free of charge.

# License
  Copyright (C)  2023  Hunter Smith.
  Permission is granted to copy, distribute and/or modify this document
  under the terms of the GNU Free Documentation License, Version 1.2
  or any later version published by the Free Software Foundation;
  with no Invariant Sections, no Front-Cover Texts, and no Back-Cover
  Texts.  A copy of the license is included in the section entitled ``GNU
  Free Documentation License''.
