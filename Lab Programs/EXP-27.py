# EXP-27: Demonstrate why encrypting each letter separately with RSA is weak

# Small demonstration values only; never use these keys for security.
n = 3233
e = 17

message = input("Enter alphabetic message: ").upper()
ciphertext = []

for ch in message:
    if ch.isalpha():
        m = ord(ch) - ord("A")
        ciphertext.append(pow(m, e, n))

print("Ciphertext blocks:", ciphertext)

# Since each letter is one of only 26 possible values, try all values.
recovered = ""
for c in ciphertext:
    found = "?"
    for m in range(26):
        if pow(m, e, n) == c:
            found = chr(m + ord("A"))
            break
    recovered += found

print("Recovered using 26-value search:", recovered)
print("Attack: encrypt all 26 possible letters with the public key")
print("and compare each result with the corresponding ciphertext block.")
