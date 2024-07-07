This is a script that will check if lines in the following format are present in the readme.
Depending on the config dict in checker.py, it'll see which items are missing and which are extra.
Works with windows on powershell.

Internal repo: Not to be shared with students. The idea is to configure a checker for each lab assignment and provide it in each student's Github classroom repo. Things to include:
- The readme_check folder for each lab assignment
- The check.bat script
- gitignore with readme_check_logs included

To create the executable, make the changes you want to to the ```check.py``` script and run ```.\compile```.

To run the executable, open a powershell terminal in the repo root and run ```.\check```

===========================================================================

Example README.md with common errors a student might make 

:S1: Test

:S2: Test

:S3: Some image

:R1: 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet facilisis magna etiam tempor orci eu lobortis elementum nibh. Augue neque gravida in fermentum et sollicitudin. Id volutpat lacus laoreet non curabitur gravida arcu. Risus viverra adipiscing at in tellus integer feugiat. Habitasse platea dictumst quisque sagittis purus sit amet volutpat. Aliquet bibendum enim facilisis gravida neque convallis a cras. Massa ultricies mi quis hendrerit dolor magna eget est lorem. Fermentum posuere urna nec tincidunt praesent. Vitae auctor eu augue ut lectus arcu bibendum at varius. Aliquam id diam maecenas ultricies mi. In metus vulputate eu scelerisque felis. In vitae turpis massa sed. Bibendum at varius vel pharetra vel turpis nunc eget lorem. Libero justo laoreet sit amet.

:R9: 

:C1: code.c

:V1: Test

:R6:Test

:R27: 

:R7: Another test

:R1: This is a duplicate

:I2:

Some image here

:C2: project\src\part_d.c

Random filler text here.

:R5: I'm running out of placeholder text ideas

:R10: Test

Screenshot here.

This is the answer to :R11:.

Blah blah blah

:R2: < insert ESE 5190 stuff here >

:R12: Test

:R3: Blah

:R4: Test

:R1: Test

:R8: Test