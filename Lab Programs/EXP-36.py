# EXP-36: Affine Caesar Cipher
# Encryption: C = (a*p + b) mod 26
# Valid a values must be relatively prime to 26.

import math

def encrypt(text, a, b):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            p = ord(ch) - base
            result += chr((a * p + b) % 26 + base)
        else:
            result += ch
    return result

def decrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Invalid a: gcd(a, 26) must be 1.")
    inverse = pow(a, -1, 26)
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            c = ord(ch) - base
            result += chr((inverse * (c - b)) % 26 + base)
        else:
            result += ch
    return result

text = input("Enter plaintext: ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if math.gcd(a, 26) != 1:
    print("Encryption is not one-to-one for this value of a.")
    print("Choose a from 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.")
else:
    cipher = encrypt(text, a, b)
    print("Ciphertext:", cipher)
    print("Decrypted:", decrypt(cipher, a, b))
