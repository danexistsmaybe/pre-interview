from subprocess import run, CompletedProcess
from time import *

from pathlib import Path
from sys import argv

# ============================= Functions for Running the Queries ==============================

# Parses the result of running cvc5
def parse_query_result(result : CompletedProcess):
	# Check if it timed out
	if result.returncode != 0: return "TIMEOUT", '0'		# records runtime as zero

	answer = result.stdout[:-1].upper()						# omit the newline

	resultlist = result.stderr.split("\n")					# stats are in stderr for some reason
	for stat in resultlist[1:]:								# parse the various stats
		if stat.split(' = ')[0] == "global::totalTime":		# find runtime
			runtime = stat.split(' = ')[1][:-2]				# records runtime as a string, omitting 'ms'
	return answer, runtime

# Runs cvc5 on a query via its path
def test_query(querypath, timelimit = 10000):
	timelimitarg = f"--tlimit={timelimit}"
	result = run(["cvc5/bin/cvc5.exe", querypath, timelimitarg, "--stats"], capture_output=True, text=True)
	
	# returns result, time
	return parse_query_result(result)

# Iteratively calls test_query on every .smt2 file in a directory
def test_query_dir(directory, timelimit = 10000):
	results = []	# output buffer

	for file in Path(directory).iterdir():
		file = str(file)

		# Just in case there is junk in the directory
		if file[-5:] != ".smt2":
			print(f"Skipping {file} as it does not appear to be a .smt2 file.")
			continue
		# Otherwise print a quick status message
		print(f"Processing file {file}...")

		# Run the query
		result, runtime = test_query(file, timelimit)
		
		# Store the result
		results.append([file.split('\\')[-1], result, runtime])

	return results

# ============================= Functions for Formatting the Output ==============================

def write_query_results(_results):
	# Reformat each row as a csv string
	results = []
	for row in _results:
		results.append(','.join(row))	# I have heard that joining lists is more efficient :)

	# Write the results to the output file
	with open("results.csv", 'w') as file:
		file.write(
			"QueryName,Result,ElapsedTime\n" + ('\n'.join(results)) # joins header with rows
		)

# ====================================== Main ===============================================
def main(argv):
	# Handle arguments
	if len(argv)>1: querydirectory = argv[1]
	else: 			querydirectory = "queries"

	if len(argv)>2: timelimit = int(argv[2])
	else: 			timelimit = 10000
	

	results = test_query_dir(querydirectory, timelimit)
	write_query_results(results)
	



















if __name__ == "__main__":
	main(argv)




# Talking points:
#	- 