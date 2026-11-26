# EXP-39: Additive Cipher Letter Frequency Attack
# Tests all 26 possible shifts and ranks results using English
# letter-frequency chi-square scores.

from collections import Counter

ENGLISH = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
    0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
    0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
    0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
    0.01974, 0.00074
]

def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result

def score(text):
    letters = [ch.lower() for ch in text if ch.isalpha()]
    n = len(letters)
    if n == 0:
        return float("inf")
    counts = Counter(ord(ch) - ord("a") for ch in letters)
    return sum((counts[i] - n * ENGLISH[i]) ** 2 / (n * ENGLISH[i])
               for i in range(26) if ENGLISH[i] > 0)

cipher = input("Enter ciphertext: ")
top_n = int(input("Enter number of top plaintexts: "))

results = []
for shift in range(26):
    plain = decrypt(cipher, shift)
    results.append((score(plain), shift, plain))

results.sort(key=lambda item: item[0])

for rank, (value, shift, plain) in enumerate(results[:top_n], 1):
    print(f"{rank}. Shift={shift}, Score={value:.2f}, Plaintext={plain}")
