'''
## Exercise 1 - compound interest

Write some code to calculate how much money you would have if you invested £20,000 in an account paying 5% interest
and left it for 5 / 10 / 20 years. 

Next, write some code to calculate how long I'd have to leave my money invested before I had £100,000.
'''

# your code here

rate = 0.05

balance = 20000

for yy in range(5):
    balance = balance*(1+rate)
    print('After',yy+1,'year(s), balance is',balance)

# reset for the time to 100k
balance = 20000
target = 100000
yy = 0

while balance < target:
    balance = balance*(1+rate)
    print('After',yy+1,'year(s), balance is',balance)
    yy = yy + 1 # while loop doesn't come with a counter, so have to track year count in own code
print('It will take',yy,'years to make £100k')
