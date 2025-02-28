# Pre-interview

### Daniel Evans

## A Fun Fact About Me
I have climbed on top of five major buildings on campus.

## Requirements
The only requirements for the Python script are Python 3.x.x and cvc5.

## How To Run The Script
Before running the script, ensure that cvc5.exe is in the location `cvc5/bin` relative to the main directory. You can also make it an environment variable and replace the path in the code.

In order to run the script, you can simply enter `python run-queries.py` from the main directory, depending on your python environment variable. In this case, the script will assume a query path of `queries` and a time limit of 1000 milliseconds. However, I have also included the option to add an argument for the query directory and another for the time limit (but only if the query directory is specified). Thus, you can also run the script with `python run-queries.py <querydirectory> <timelimit>`.

## A Few Notes
Output is stored in `results.csv` and times are recorded in milliseconds.

$x^2$
