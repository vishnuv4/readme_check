This is a script that will check if lines in the following format are present in the readme.
Depending on the config dict in checker.py, it'll see which items are missing and which are extra.
Works with windows on powershell.

Internal repo: Not to be shared with students. The idea is to configure a checker for each lab assignment and provide it in each student's Github classroom repo. Things to include:
- The readme_check folder for each lab assignment
- The check.ps1 script
- gitignore with readme_check_logs included

To create the executable, make the changes you want to to the ```check.py``` script and run ```.\compile```.

To run this script, open a powershell terminal in the repo root and run ```.\check```

S1: Test

S2: Test

S3: Lorem ipsum

R1: Placeholder text

R9: test

C1: code.c

V1: Test

R6:Test

R200: 

R7: Another test

C2: project\src\part_d.c

Random filler text here.

R5: I'm running out of placeholder text ideas

R10: Test

Screenshot here.

R11: Test

R2: < insert ESE 5190 stuff here >

R12: Test