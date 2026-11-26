# EXP-30: CBC-MAC Forgery Demonstration
# Install: pip install pycryptodome
# Demonstrates the CBC-MAC extension weakness for a fixed one-block message.

from Crypto.Cipher import AES

key = b"1234567890123456"
X = b"HELLO12345678901"  # exactly one 16-byte block

aes = AES.new(key, AES.MODE_ECB)

# CBC-MAC of one-block message X with an all-zero initial state.
T = aes.encrypt(X)

# Forge a two-block message: X || (X XOR T)
second_block = bytes(x ^ t for x, t in zip(X, T))
forged_message = X + second_block

# Calculate CBC-MAC of the forged two-block message.
state = bytes(16)
for i in range(0, len(forged_message), 16):
    block = forged_message[i:i+16]
    state = aes.encrypt(bytes(a ^ b for a, b in zip(block, state)))

print("Original one-block MAC:", T.hex())
print("Forged two-block MAC:  ", state.hex())
print("Forgery successful:", state == T)
print("Forged message (hex):", forged_message.hex())
