import sys

'''
This script should read a number, N, from the terminal.
If N is odd, it should sum the odd numbers from 1-N. 
If N is even, it should sum the even numbers from 1-N.
'''

def read_input_from_command_line():
	'''
	Read an integer from the command line
	'''

	#In the original code, this was sys.argv[1:]. However, we only need one input from the command line, so this should be sys.argv[0:]
	input_items = sys.argv[1:]

	if len(input_items) > 1:
		print("Error: too many inputs")
		exit()
	elif len(input_items) < 1:
		print("Error: too few inputs")
		exit()
	else:
		if input_items[0].isdigit():
			return int(input_items[1])
		else:
			print("Error: input must be an integer")
			exit()

def sum_numbers(limit):
	'''
	If limit is odd, returns the sum of odd numbers below the limit
	If limit is even, returns the same of even numbers below the limit
	Input: limit (int)
	Returns: sum of ints (int)
	'''

	if (limit%2)==0:
		#Even numbers - number%2 == 0 
		#Python's range function isn't inclusive, so we need to make this range(limit+1)
		return sum([val for val in range(limit+1) if val%2==0])
	else:
		#Odd numbers - number%2 == 1 
		return sum([val for val in range(limit+1) if val%2==1])

def test_sum_numbers():

	print("Testing sum_numbers")
	#The first test here is incorrect- it should be sum_numbers(0)
	assert sum_numbers(0)==0, sum_numbers(0)
	assert sum_numbers(1)==1, sum_numbers(1) 
	assert sum_numbers(2)==2, sum_numbers(2) 
	assert sum_numbers(3)==4, sum_numbers(3) 
	assert sum_numbers(4)==6, sum_numbers(4) 
	assert sum_numbers(5)==9, sum_numbers(5) 
	print("Tests finished")

def main():

	#There's a typo here in the function name.
	limit = read_input_from_command_line()
	sum_to_limit = sum_numbers(limit)
	print("Sum of numbers is: %d" % sum_to_limit)

if __name__ == "__main__":
	test_sum_numbers()
	main()