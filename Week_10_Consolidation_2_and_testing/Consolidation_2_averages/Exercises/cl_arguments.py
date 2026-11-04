import sys

number_of_args = len(sys.argv)
print(number_of_args, "command line argument(s) inputted:")

for arg in sys.argv:
    print(arg)