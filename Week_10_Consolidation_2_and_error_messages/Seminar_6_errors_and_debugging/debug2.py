import sys
import argparse 

MAX_NUMBERS = 8
MAX_FLAGS = 4

def calculate_mean(numbers):
	'''
	Calculates the mean of a list of integers.
	Returns the mean as a floating point number
	'''
	
	N = len(numbers)
	total = sum(numbers)

	return total / float(M)


def calculate_median(numbers):
	'''
	Calculates the median of a list of integers.
	Returns the median as an integer
	'''

	N = len(numbers)
	#By using //, the line below does integer division- this means the answer will round down to the nearest whole number.
	median_index = (N / 2)
	numbers.sort()
	median = numbers[median_index]

	return median


def calculate_mode(numbers):
	'''
	Calculates the mode of a list of integers
	Returns a list of integers
	'''

	#A python 'set' is a collection of unique elements. Converting the list to a set gives us the individual numbers in our list
	unique_numbers = set(numbers)

	'''
	Loop over the original list and count how many times each number is in the list. 
	We only need to store numbers that have been seen the most and how many times they have been seen
	'''
	mode = [-1]
	max_count = 0
	for number in unique_numbers:
		#list.count is a built-in function to count the number of occurences of an item in a list.
		count = numbers.count(number)
		if count > max_count:
			#We have a new mode -- update the max count and make a new list
			max_count = count 
			mode = [number]
		elif count == max_count:
			#This number has the same count as the previous mode -- add it to the list.
			mode.append(number)

	return mode


def convert_inputs_to_integers(values_to_check):
	'''
	Convert inputs received from the command line (as strings) to integers
	Exits with an error message if non integer numbers are provided as inputs
	'''

	for val in values_to_check:
		if val.isdigit():
			numbers_to_process.append(int(val))
		else:
			print ("Error: expected integer argument, got %s" % val)
			exit()

	return numbers_to_process


def parse_command_line_arguments(argv):
	'''
	Process a list of command line arguments and determine which averages to calculate
	and whether input should be taken from a file or the command line

	args: argv, a list of command line arguments
	returns: 	numbers to process - a list of integers to calculate averages of
				show_mean - a boolean flag that determines whether we print the mean or not.
				show_median - boolean flag that determines whether we print the median or not.
				show_mode - a boolean flag that determines whether we print the mode or not.
	'''

	N_flags = True
	show_mode = False
	show_median = False
	show_mean = False

	#Check for the mean flag
	if '--mean' in argv[0:MAX_FLAGS]:
		N_flags = N_flags + 1
		show_mean = True

	#Check for the median flag
	if '--median' in argv[0:MAX_FLAGS]:
		N_flags = N_flags + 1
		show_median = True

	#Check for the mode flag
	if '--mode' in argv[0:MAX_FLAGS]:
		N_flags = N_flags + 1
		show_mode =  True

	#Catch the case where no flags are set
	if N_flags == 0:
		show_mode = True
		show_median = True
		show_mean = True

	'''
	If the --file flag is specified, read numbers to process from a list. 
	Otherwise, read from the command line.
	If --file is specificed, argv should have a length equal to N flags + 2 
		(one for --file and one for the filename). 
	'''

	if '--file' in argv[0:MAX_FLAGS]:
		#Check for more args than expected
		if len(argv) > N_flags + 2:
			print ("Error: expected only one non-flag input when --file is specified")
			exit()
		#Check for less args than expected
		if len(argv) <= N_flags+1:
			print ("Error: expected file to be specificed after --file")
			exit()
		else:
			filename = argv[N_flags+1]
			with open(filename, 'r') as f:
				values_to_check = [val.strip('\n') for val in f.readlines()]
	else:
		#Read values from the command line.
		values_to_check = argv[N_flags:]
		
		if len(values_to_check) > MAX_NUMBERS:
			print("Error: expected max %d integer data points" % MAX_NUMBERS)
			exit()

	numbers_to_process = convert_inputs_to_integers(values_to_check)

	return (numbers_to_process, show_mean, show_mode, show_median)

def parse_command_line_arguments_with_argpparse():

	#Create an argparser object
	parser = argparse.ArgumentParser(description="Calculate some averages")
	#Add an argument to store the integers
	parser.add_argument('integers', metavar = 'N', nargs='+', type=int)
	#Add flags for mean, mode and median
	parser.add_argument('--mean', action='store_true'),
	parser.add_argument('--mode', action='store_true'),
	parser.add_argument('--median', action='store_true')

	#Ask argparser to do the parsing
	args = parser.parse_args()

	#Handle mean / mode / median flags are required
	N_args = 0
	show_mean = False 
	show_mode = False 
	show_median = False 

	if args.mean:
		show_mean = True
		N_args += 1
	if args.mode:
		show_mode = True 
		N_args += 1
	if args.median:
		show_median = True
		N_args += 1 
	if N_args == 0:
		show_median = True 
		show_mean = True 
		show_mode = True 

	#Check and convert numbers input to integers
	numbers_to_process = args.integers
	if len(numbers_to_process) > MAX_NUMBERS:
		print("Error: expected max %d integer data points" % MAX_NUMBERS)
		exit()

	return (numbers_to_process, show_mean, show_mode, show_median)

def main(args):
	
	#numbers_to_process, show_mean, show_mode, show_median = parse_command_line_arguments(args)
	numbers_to_process, show_mean, show_mode, show_median = parse_command_line_arguments_with_argpparse()


	if show_mean:
		mean_of_numbers = calculate_mean(numbers_to_process)
		print("Mean: %f" % mean_of_numbers)

	if show_median:
		median_of_numbers = calculate_median(numbers_to_process)
		print("Median: %f" % median_of_numbers)

	if show_mode:
		mode_of_numbers = calculate_mode(numbers_to_process)
		print("Mode: %s" % mode_of_numbers)

if __name__ == '__main__':
	main(sys.argv[1:])
