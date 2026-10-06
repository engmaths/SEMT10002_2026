# =============================================================================
# Exercise 2 - Floating Point Comparisons
# =============================================================================
#
# Try running the piece of code below.
#
# Note that we get a (seemingly) incorrect answer -- algebraically, both
# expressions should equal 5/9. But when we ask Python if they are equal, it
# says no ("False"). We'll soon see in detail why this is (essentially,
# floating point numbers aren't represented exactly on a computer).
#
# A better way to compare whether two floats are equal is to see whether the
# difference between them is small ("small" will be context-dependent, but
# let's assume less than 10^-5 for today). Re-write the code below to do the
# comparison correctly.
# =============================================================================

e = 5/9
f = (1/3)*5*(1/3)
print('e is', e)
print('f is', f)
print(e == f)  # fix this line, or add something better below
