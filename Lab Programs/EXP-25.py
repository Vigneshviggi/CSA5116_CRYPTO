# EXP-25: RSA Common-Factor Check using GCD
import math

n = int(input("Enter RSA modulus n: "))
m = int(input("Enter the known plaintext block: "))

g = math.gcd(m, n)

print("GCD =", g)
if 1 < g < n:
    print("A non-trivial factor of n was found:", g)
    print("Other factor:", n // g)
    print("This can allow the RSA modulus to be factored.")
elif g == n:
    print("The plaintext block is a multiple of n; this does not reveal")
    print("a non-trivial factor by itself.")
else:
    print("No common factor greater than 1 was found.")
