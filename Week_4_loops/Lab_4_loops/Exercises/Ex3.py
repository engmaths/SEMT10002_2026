'''
The function below is *supposed* to calculate the factorial
n! = 1 x 2 x 3 x ... x n, so `factorial(4)` should give
1x2x3x4 = 24.

It doesn't work — some of the tests below fail. **Don't rewrite it from scratch.** Instead:
1. Run it and look at what it actually returns.
2. Work out *why* — trace it by hand for `n = 3`, writing down `result` after each iteration.
3. Make the smallest change you can to fix it.

'''

def factorial(n):
    result = 1
    for ii in range(n):
        result = result * ii
    return result


# === Do not edit below this line ===
if abs(factorial(0) - 1) < 1e-5:
    print('factorial(0) passed')
else:
    print('factorial(0) FAILED: got', factorial(0), 'expected 1')

if abs(factorial(1) - 1) < 1e-5:
    print('factorial(1) passed')
else:
    print('factorial(1) FAILED: got', factorial(1), 'expected 1')

if abs(factorial(4) - 24) < 1e-5:
    print('factorial(4) passed')
else:
    print('factorial(4) FAILED: got', factorial(4), 'expected 24')

if abs(factorial(6) - 720) < 1e-5:
    print('factorial(6) passed')
else:
    print('factorial(6) FAILED: got', factorial(6), 'expected 720')