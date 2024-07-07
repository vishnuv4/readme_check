This is a script that will check if lines in the following format are present in the readme.
Depending on the config dict in checker.py, it'll see which items are missing and which are extra.

To run this script, open a powershell terminal in the repo root and run ```.\check```

Note: if you use linux or another operating system, feel free to modify the ```check.ps1``` script to work with your OS - but do not change anything inside the ```readme_check``` folder.

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