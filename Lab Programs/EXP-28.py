# EXP-28: Diffie-Hellman Key Exchange

q = 23
a = 5

alice_secret = 6
bob_secret = 15

alice_public = pow(a, alice_secret, q)
bob_public = pow(a, bob_secret, q)

alice_shared = pow(bob_public, alice_secret, q)
bob_shared = pow(alice_public, bob_secret, q)

print("Public prime q:", q)
print("Public base a:", a)
print("Alice sends:", alice_public)
print("Bob sends:", bob_public)
print("Alice shared key:", alice_shared)
print("Bob shared key:", bob_shared)
print("Keys match:", alice_shared == bob_shared)

print("\\nIf they exchange x^a mod q instead of a^x mod q,")
print("the standard Diffie-Hellman shared-key equality does not follow.")
print("Use authenticated Diffie-Hellman to prevent man-in-the-middle attacks.")
