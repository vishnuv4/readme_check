This is a script that will check if lines in the following format are present in the readme.
Depending on the config dict in checker.py, it'll see which items are missing and which are extra.
Works with windows on powershell.

Internal repo: Not to be shared with students. The idea is to configure a checker for each lab assignment and provide it in each student's Github classroom repo. If they have the ```readme_check``` folder and the ```check.ps1``` script, they will be able to see which items they have remaining in the assignment.

To create the executable, make the changes you want to to the ```check.py``` script and run ```.\compile```.

To run this script, open a powershell terminal in the repo root and run ```.\check```

S1: Test

S2: Test

S3: Lorem ipsum

R1: Placeholder text

R3: TEST

R4: Blah

C1: project\part_a.c

V1: Test

R6: Test

R7: Another test

C2: project\src\part_d.c

V2: Test

R5: I'm running out of placeholder text ideas

R10: Test

R11: Test

R2: < insert ESE 5190 stuff here >

R12: Test