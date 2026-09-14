import sys

def convert_to_float(string):
	return float(string)

def convert_to_string(number):
	return str(number)

def multiply_numbers(number1, number2):
	return number1 * number2 

def main():

	data1 = sys.argv[1]
	data2 = sys.argv[2]

	print(multiply_numbers(convert_to_float(data1), convert_to_string(data2)))


if __name__ == "__main__":
	main()