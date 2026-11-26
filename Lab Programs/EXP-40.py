# EXP-40: Monoalphabetic Substitution Frequency Attack
# Alternate version of EXP-37: frequency ranking plus several
# candidate mappings formed by swapping adjacent frequency guesses.
# These are rough candidates, not guaranteed language-analysis results.

from collections import Counter

ENGLISH_ORDER = "etaoinshrdlcumwfgypbvkjxqz"

cipher = input("Enter ciphertext: ")
top_n = int(input("Enter number of possible plaintexts: "))

counts = Counter(ch.lower() for ch in cipher if ch.isalpha())
cipher_order = [ch for ch, _ in counts.most_common()]

def decode(mapping):
    result = ""
    for ch in cipher:
        if ch.isalpha():
            value = mapping.get(ch.lower(), ch.lower())
            result += value.upper() if ch.isupper() else value
        else:
            result += ch
    return result

candidates = []
base_mapping = dict(zip(cipher_order, ENGLISH_ORDER))
candidates.append(("Frequency order", decode(base_mapping)))

# Try small variations in the frequency assignment.
for i in range(min(len(cipher_order) - 1, 25)):
    letters = list(ENGLISH_ORDER)
    letters[i], letters[i + 1] = letters[i + 1], letters[i]
    mapping = dict(zip(cipher_order, letters))
    candidates.append((f"Swap {i + 1}", decode(mapping)))

seen = set()
shown = 0
for label, text in candidates:
    if text not in seen:
        seen.add(text)
        shown += 1
        print(f"{shown}. {label}: {text}")
        if shown >= top_n:
            break

print("\\nNote: Frequency analysis alone is approximate. A reliable")
print("substitution solver needs dictionary and n-gram language scoring.")
