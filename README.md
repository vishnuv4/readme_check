# About

This is a script that will help students keep track of their progress in assignments. In grad school we work in small chunks of time, whenever we get a chance - and sometimes if you don't work on something for a few days you can't remember where you left off. Or at least, I can't. So it's a quality of life thing that helps students stay on top of their assignments. 

It'll check for missing answers, duplicate answers, and extra answers.

# Requirements

Python 3.12. Might work with lower versions too but it was developed on 3.12. Works with Windows on powershell.

# Usage

We will configure a checker for each lab assignment and provide it in each assignment's skeleton repo. Things to include:
- The readme_check folder for each lab assignment
- The check.bat script
- gitignore with readme_check_logs included

# Try it out

- First, double click the ```check.bat``` script. Or run ```.\check.ps1``` in a powershell terminal. 
- You'll see an output. Try to fix the readme according to the messages until you're done.
- The question configuration is defined in check.py - look for a dictionary named "config" at the top of that file and see that it is consistent with what the checker tells you.
- The .bat and .ps1 script both run an executable in the readme_check folder - that's just the python script in .exe format.
- To create the executable, make the changes to the config struct. Run ```.\compile```. This create a virtual environment with the required packages and then creates an executable out of the python script in the readme_check folder.
- Repeat the first two steps to see the new configuration.

===========================================================================

## Example README.md (with common errors a student might make)

(S1) Test

(S2) Test

(R1) 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Amet facilisis magna etiam tempor orci eu lobortis elementum nibh. Augue neque gravida in fermentum et sollicitudin. Id volutpat lacus laoreet non curabitur gravida arcu. Risus viverra adipiscing at in tellus integer feugiat. Habitasse platea dictumst quisque sagittis purus sit amet volutpat. Aliquet bibendum enim facilisis gravida neque convallis a cras. Massa ultricies mi quis hendrerit dolor magna eget est lorem. Fermentum posuere urna nec tincidunt praesent. Vitae auctor eu augue ut lectus arcu bibendum at varius. Aliquam id diam maecenas ultricies mi. In metus vulputate eu scelerisque felis. In vitae turpis massa sed. Bibendum at varius vel pharetra vel turpis nunc eget lorem. Libero justo laoreet sit amet.

(C1) code.c

(V1) Test

(R6)Test

(R27) An answer

(R1) Yet another answer

(I2)

Some image here

(C2) project\src\part_d.c

Random filler text here.

(R5)

Blah blah blah

(R9) A meaningless answer that still counts in the software because it isn't a full autograder.

(R7) Empty answers "count" too because it only looks for this tag.

(R8)

(R10) I'm running out of placeholder text ideas

(R2) < insert ESE 5190 stuff here >

(R3) Blah

(R4) Test

(I1)

Image here

(S4)

(C3)