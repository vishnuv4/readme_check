This is a script that will check if lines in the following format are present in the readme.
Depending on the config dict in checker.py, it'll see which items are missing and which are extra.
Works with windows on powershell.

To create an exe out of a python script, run ```pip install pyinstaller``` and then ```pyinstaller check.py```.
Then copy the contents of the ```dist\``` folder into the ```readme_check\``` folder

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