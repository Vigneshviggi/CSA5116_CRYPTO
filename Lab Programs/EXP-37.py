# EXP-37: Monoalphabetic Substitution Frequency Attack
# Frequency mapping gives an approximate candidate, not guaranteed
# top-N plaintexts. Full substitution solving needs n-gram search.

from collections import Counter

ENGLISH_ORDER = "etaoinshrdlcumwfgypbvkjxqz"

cipher = input("Enter ciphertext: ")
top_n = int(input("How many possible plaintexts? "))

counts = Counter(ch.lower() for ch in cipher if ch.isalpha())
cipher_order = [ch for ch, count in counts.most_common()]
mapping = dict(zip(cipher_order, ENGLISH_ORDER))

candidate = ""
for ch in cipher:
    if ch.isalpha():
        decoded = mapping.get(ch.lower(), ch.lower())
        candidate += decoded.upper() if ch.isupper() else decoded
    else:
        candidate += ch

print("\\nApproximate frequency-based plaintext:")
print(candidate)
print("\\nFrequency mapping (cipher -> estimated plaintext):")
for source in cipher_order:
    print(source, "->", mapping[source])

print("\\nRequested top results:", top_n)
print("This simple frequency method produces one estimate.")
print("It does not guarantee", top_n, "distinct ranked solutions.")
