from subprocess import run, CompletedProcess
from multiprocessing import Pool
from time import *

from pathlib import Path
from sys import argv



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
def test_query(args):
	querypath, timelimit = args

	timelimitarg = f"--tlimit={timelimit}"
	result = run(["cvc5/bin/cvc5.exe", querypath, timelimitarg, "--stats"], capture_output=True, text=True)
	
	# returns result, time
	return parse_query_result(result)






# Calls test_query on every .smt2 file in a directory in batches of five
def test_query_dir(directory, timelimit = 10000):
	results = []		# output buffer

	files = list(str(file) for file in Path(directory).iterdir())
	N = len(files)
	bs = 5				# batch size

	for f in range(0, N, bs):
		batch = files[f:f+bs]
		print("Processing batch ", f//bs, " of ", N//bs - 1)
		b = len(batch)
		pool = Pool(processes = b)

		times = pool.map(test_query, zip(batch, [timelimit]*b))
		pool.close()
		pool.join()
		
		for i in range(len(batch)):
			results.append([batch[i].split('\\')[-1], times[i][0], times[i][1]])
	
	return results





# Converts a 2D list of results into csv data and writes to a file
def write_query_results(_results):
	# Reformat each row as a csv string
	results = []
	for row in _results:
		results.append(','.join(row))	# I have heard that joining lists is more efficient :)

	# Write the results to the output file
	with open("results-parallel.csv", 'w') as file:
		file.write(
			"QueryName,Result,ElapsedTime\n" + ('\n'.join(results)) # joins header with rows
		)





# Main
def main(argv):
	# Handle arguments
	if len(argv)>1: querydirectory = argv[1]
	else: 			querydirectory = "queries"

	if len(argv)>2: timelimit = int(argv[2])
	else: 			timelimit = 10000
	
	start = time()
	# Task 3
	results = test_query_dir(querydirectory, timelimit)
	# Task 4
	write_query_results(results)
	print("Total time taken was", (time() - start)/60)
	





if __name__ == "__main__":
	main(argv)


