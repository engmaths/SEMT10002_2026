'''
PART 1
If you put an initial amount of money, $P$ (typically known as the *principal*) in a fixed-rate savings account with interest rate $r$, each year, 
the amount in your account will be multiplied by an amount $(1+r)$.

Write a function to calculate how much money you would have if you invested £20,000 in an account paying 5% interest for 10 years. Do this with a loop rather than the analytical expression we give you.
Your code should print out the balance of the account after each year. 
You can check your code against the analytical calculation $F = P(1+r)^t$.

'''

def calculate_interest(initial_deposit, interest_rate, time):
    pass #Write your code here

def test_calculate_interest():

    initial = 100
    interest_rate = 0.5
    time = 5
    if calculate_interest(initial, interest_rate, time) != initial * (1+interest_rate)**time:
        print("Error! - test 1 fails")

    initial = 100
    interest_rate = 0.0
    time = 5
    if calculate_interest(initial, interest_rate, time) != initial * (1+interest_rate)**time:
        print("Error! - test 2 fails")

    initial = 0
    interest_rate = 0.1
    time = 15
    if calculate_interest(initial, interest_rate, time) != initial * (1+interest_rate)**time:
        print("Error! - test 3 fails")

    initial = 100
    interest_rate = 0.1
    time = 0
    if calculate_interest(initial, interest_rate, time) != initial * (1+interest_rate)**time:
        print("Error! - test 4 fails")

test_calculate_interest()

'''
Part 2
Next, write some code to calculate how long I'd have to leave my money invested before I had £100,000.
'''

#Your code goes here