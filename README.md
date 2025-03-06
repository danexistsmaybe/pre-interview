# Pre-interview

### Daniel Evans

## A Fun Fact About Me
I am endeavoring to learn how to back flip and play guitar this semester.

## Requirements
The only requirements for the Python script are Python 3.x.x and cvc5.

## How To Run The Script
Before running the script, ensure that cvc5.exe is in the location `cvc5/bin` relative to the main directory. You can also make it an environment variable and replace the path in the code.

The script can be run with either the command `python run-queries.py` or `python run-queries.py <querydirectory> <timelimitms>`. Defaults are `queries` and 60000ms.

## Notes
1. Output is stored in `results.csv` and times are recorded in milliseconds.
2. Tasks 3 and 4 are represented by the two functions executed in `main`. Task 2 is a sub-step of task 3.

## Extras
I made two extra versions of the script. Out of curiosity, I wanted to see what would happen if I used multiprocessing to iterate through the directory. I also wanted to try my hand at a shell language, so I made a version in PowerShell. Neither of these extra scripts were requested as part of the given task -- I made them for myself out of curiosity -- so I put them in the `extras` folder.