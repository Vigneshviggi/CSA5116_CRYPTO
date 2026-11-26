# EXP-33: DES Encryption and Decryption
# Install: pip install pycryptodome
# DES is obsolete and should only be used for learning.

from Crypto.Cipher import DES

key = b"12345678"          # 8 bytes; DES uses 56 effective key bits
plaintext = b"ABCDEFGH"    # exactly one 64-bit block

cipher = DES.new(key, DES.MODE_ECB)
ciphertext = cipher.encrypt(plaintext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)

print("Plaintext:", plaintext)
print("Key:", key.hex())
print("Ciphertext:", ciphertext.hex().upper())
print("Decrypted:", decrypted)
