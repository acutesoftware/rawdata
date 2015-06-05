# time_generate.py
# script to check times of generating data using various methods

import sys
import time_utils as tst

import os
sys.path.append('..\\rawdata')
import generate


def main():
	tst.time_function('generate', 9000, 'generate_password', 80)
	tst.time_function('generate', 90, 'random_letters', 10000)
	tst.time_function('generate', 900, 'random_letters', 1000)
	tst.time_function('generate', 90, 'random_hex_string', 10000)   # much faster than random_letters
	tst.time_function('generate', 900, 'random_hex_string', 1000)
	
	# test table creation
	colLabel = ['Start', 'Finish', 'Purch_YR', 'password', 'born', 'lives', 'name', 'Friend',  'Quote', 'Interest', 'Height', 'Weight', 'Score']
	colTypes = ['DATE', 'DATE', 'DATE',  'STRING', 'PLACE', 'PLACE','PEOPLE','PEOPLE', 'WORD', 'WORD', 'INT', 'INT', 'INT']
	#tbl = random_table(600,13, colTypes, colLabel)
	
	tst.time_function('generate', 1, 'random_table', 13, 60, colTypes, colLabel)
	# generateTestData.random_table - ran 3 tests :
	#   tot=10.68 avg=3.559 min=3.524 max=3.628
	
	
	#tst.time_function('generateTestData', 10, 'random_table', 13, 600000, colTypes, colLabel)
	#check_timings_list_comprehension_vs_loops(colTypes, colLabel)

def check_timings_list_comprehension_vs_loops(colTypes, colLabel):
	# get a table and time different methods of display
	tbl = generate.random_table( 13, 60, colTypes, colLabel)
	results = []
	avgTime, totTime, minTime, maxTime = tst.time_function('generate', 10, 'show_table', tbl)
	results.append({'function':'show_table', 'avgTime': avgTime})
	print('--- Results Summary --- ')
	for r in results:
		print(r['function'], r['avgTime'])

	
if __name__ == '__main__':
	main()
	
	