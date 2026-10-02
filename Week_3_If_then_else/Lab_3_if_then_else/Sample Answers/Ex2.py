'''
## Exercise 2 - Collatz Conjecture

Starting from any integer n, apply the rules: if even divide by 2, if odd multiply by 3 and add 1.
The Collatz conjecture states that if we follow this sequence, we will eventually reach one.
Although this problem looks simple, mathematicians are yet to prove it's true. 

We can use Python to explore this question numerically, seeing that at least for small number it seems to hold.

Write some code that counts the number of steps it takes a given starting number to reach one.
Then write some additional code to see which starting number under 1000 takes the most steps to reach 1. 
'''

# initialise value
n = 1000

# for loop so (1) there's a timeout and (2) have a counter
# could easily do it with while as well
for ii in range(100000): 
    if n%2==0:
        # even
        n = n/2
    else:
        # odd
        n = 3*n + 1
    print('Step',ii,'n is',n)
    if n==1:
        break
# I suppose we might have timed out or disproved the conjecture, so check
if n==1:
    print('Reached 1 in',ii+1,'steps')
else:
    print('Done',ii+1,'steps and given up on reaching 1')

# tracker for max steps
max_steps = 0
max_start = 0

# now run it for numbers up to 1000
for jj in range(1000):
    n = jj+1 # offset for n to count 1 to 1000
    for ii in range(100000): 
        if n%2==0:
            # even
            n = n/2
        else:
            # odd
            n = 3*n + 1
        #print('Step',ii,'n is',n)
        if n==1:
            print('Converged in',ii+1,'steps from',jj+1)
            if n==1 and ii+1>max_steps:
                max_steps = ii+1
                max_start = n
            break
print('Longest convergence was',max_steps,'steps, starting from',max_start)
