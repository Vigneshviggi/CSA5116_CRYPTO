# EXP-26: RSA Key Generation, Encryption and Decryption
# Demonstrates that changing e and d while reusing n is not safe
# after the old private key has been leaked.

import math

p, q = 11, 17
n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = pow(e, -1, phi)

message = 5
ciphertext = pow(message, e, n)
decrypted = pow(ciphertext, d, n)

print("Modulus n:", n)
print("Public key (e, n):", (e, n))
print("Private exponent d:", d)
print("Message:", message)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted)

print("\\nTheory: If the private key is leaked, generate new primes")
print("and a completely new modulus n. Merely choosing new e and d")
print("with the same n is not a safe recovery strategy.")
