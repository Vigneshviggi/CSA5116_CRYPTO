# EXP-24: Find the Private Key in RSA

import math

n = 3599
e = 31

p = None
for candidate in range(2, math.isqrt(n) + 1):
    if n % candidate == 0:
        p = candidate
        break

if p is None:
    raise ValueError("n is prime; no factor pair found.")

q = n // p
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

print("p =", p)
print("q =", q)
print("n =", n)
print("Phi(n) =", phi)
print("Public exponent e =", e)
print("Private exponent d =", d)
