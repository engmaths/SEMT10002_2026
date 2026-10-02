# =============================================================
# Exercise 4 - Complex numbers
# =============================================================
#
# Complex numbers of the form z = a + i*b where i = sqrt(-1), are
# used throughout mathematics and engineering. In Python we can
# represent a complex number with two variables - one for the real
# part (a) and one for the imaginary part (b). Let's write some
# functions for processing complex numbers.
#
# 1. Write complex_sum(a, b, c, d) which returns TWO values: the
#    real and imaginary parts of
#    z3 = z1 + z2 = (a + bi) + (c + di).
#
# 2. Write complex_product(a, b, c, d) which returns the real and
#    imaginary parts of
#    z3 = z1 * z2 = (a + bi)(c + di) = (ac - bd) + (ad + bc)i.
#
# 3. Write modulus_squared(a, b) which returns a^2 + b^2.
#
# 4. Using ONLY calls to your functions, verify the identity
#    |z1 * z2|^2 = |z1|^2 * |z2|^2 for z1 = 1.1 + 2.3i and
#    z2 = 0.7 + 1.9i. Your verification should be a single boolean
#    expression - and remember from week 1 that comparing floats
#    with == is risky. Check the difference is less than 1e-5.
# =============================================================


# Your code here
def complex_sum(a, b, c, d):
    return a+c, b+d

def complex_product(a, b, c,d):
    return (a*c-b*d), (a*d+b*c)

def modulus_squared(a, b):
    return a**2 + b**2

z1_squared = modulus_squared(1.1, 2.3)
z2_squared = modulus_squared(0.7, 1.9)
z1_squared_z2_squared = z1_squared * z2_squared

print("z1 squared:", z1_squared)
print("z2 squared:", z2_squared)
print("product of z1^2 and z2^2:", z1_squared_z2_squared)

z1_z2_real, z1_z2_imag = complex_product(1.1, 2.3, 0.7, 1.9)
print("Real part of z1 * z2:", z1_z2_real)
print("Imaginary part of z1 * z2:", z1_z2_imag)

z1_z2_squared = modulus_squared(z1_z2_real, z1_z2_imag)
print("Modulus of z1 * z2:", z1_z2_squared)

print("Identity is:", abs(z1_z2_squared - z1_squared_z2_squared) < 1E-5)
