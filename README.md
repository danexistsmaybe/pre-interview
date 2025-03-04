# Pre-interview

### Daniel Evans

## A Fun Fact About Me
I am endeavoring to learn how to back flip and play guitar this semester.

## Requirements
The only requirements for the Python script are Python 3.x.x and cvc5. For the PowerShell script, you would need to be on Windows.

## How To Run The Script(s)
### Python
Before running the script, ensure that cvc5.exe is in the location `cvc5/bin` relative to the main directory. You can also make it an environment variable and replace the path in the code.

The script can be run with either the command `python run-queries.py` or `python run-queries.py <querydirectory> <timelimitms>`. Defaults are `queries` and 1000ms.

### PowerShell
I wanted to try doing it in a shell language because I am less familiar with them, but I would like to learn more. In order to run my attempt at the script in PowerShell, just execute `./run-queries1.ps1` in the terminal.

## Notes
1. Output is stored in `results.csv` and times are recorded in milliseconds.
2. Tasks 3 and 4 are represented by the two functions executed in `main`. Task 2 is a sub-step of task 3.