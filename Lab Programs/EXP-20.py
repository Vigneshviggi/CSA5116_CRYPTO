# EXP-20: Demonstrate Error Propagation in ECB and CBC Modes
# Install: pip install pycryptodome

from Crypto.Cipher import DES

key = b"12345678"
iv = b"abcdefgh"
plaintext = b"ABCDEFGH" + b"IJKLMNOP" + b"QRSTUVWX"

# CBC encryption
cbc = DES.new(key, DES.MODE_CBC, iv)
ciphertext = bytearray(cbc.encrypt(plaintext))

# Introduce one bit error in the first ciphertext block (C1)
ciphertext[0] ^= 1

# CBC decryption
cbc_dec = DES.new(key, DES.MODE_CBC, iv)
cbc_result = cbc_dec.decrypt(bytes(ciphertext))

print("CBC original plaintext:", plaintext)
print("CBC after error:       ", cbc_result)
print("P1 is corrupted; the corresponding bit in P2 changes.")
print("P3 and later blocks are unaffected.")

# ECB comparison
ecb = DES.new(key, DES.MODE_ECB)
ecb_ciphertext = bytearray(ecb.encrypt(plaintext))
ecb_ciphertext[0] ^= 1
ecb_result = DES.new(key, DES.MODE_ECB).decrypt(bytes(ecb_ciphertext))

print("\\nECB original plaintext:", plaintext)
print("ECB after error:       ", ecb_result)
print("Only the corresponding plaintext block (P1) is affected.")

print("\\nA bit error in source plaintext P1 affects all subsequent CBC")
print("ciphertext blocks because CBC encryption is chained.")
