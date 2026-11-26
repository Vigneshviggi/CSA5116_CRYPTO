# EXP-35: One-Time-Pad Version of the Vigenere Cipher

def encrypt(plaintext, key):
    result = ""
    j = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = key[j]
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

def decrypt(ciphertext, key):
    result = ""
    j = 0
    for ch in ciphertext:
        if ch.isalpha():
            shift = key[j]
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base - shift) % 26 + base)
            j += 1
        else:
            result += ch
    return result

plaintext = input("Enter plaintext: ")
key = list(map(int, input("Enter key stream numbers separated by spaces: ").split()))

letter_count = sum(ch.isalpha() for ch in plaintext)
if len(key) != letter_count or any(k < 0 or k > 25 for k in key):
    print("Enter exactly", letter_count, "key values between 0 and 25.")
else:
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    print("Decrypted:", decrypt(ciphertext, key))
