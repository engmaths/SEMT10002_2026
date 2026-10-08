def determinant(a, b, c, d):
    return a*d - b*c

def solve(a, b, c, d, e, f):

    det = determinant(a, b, c, d)

    if det != 0:
        x = (e*d - b*f) / determinant(a, b, c, d)
        y = (a*f - e*c) / determinant(a, b, c, d)

        return (x, y)

    return None, None

    # ==== Do not edit below this line ====

#Basic case
if determinant(2, 1, 1, 3) == 5:
    print("Test 1 passed")
else:
    print("Test 1 failed")
    exit()

#Singular
if determinant(1, 2, 2, 4) == 0:
    print("Test 2 passed")
else:
    print("Test 2 failed")
    exit()

#Basic case
x, y = solve(2, 1, 1, 3, 5, 10)

if x ==1 and y == 3:
    print("Test 3 passed")
else:
    print("Test 3 failed")

x, y = solve(1, 2, 2, 4, 3, 6)

if x is None and y is None:
    print("Test 4 passed")
else:
    print("Test 4 failed")

print("All tests passed -- well done")
