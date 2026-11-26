# EXP-19: Triple DES Encryption and Decryption using CBC Mode
# Install: pip install pycryptodome

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

key = DES3.adjust_key_parity(b"123456789012345678901234")
iv = b"12345678"
plaintext = b"HELLO WORLD"

cipher = DES3.new(key, DES3.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

print("Plaintext:", plaintext.decode())
print("Encrypted:", ciphertext.hex())

decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), DES3.block_size)

print("Decrypted:", decrypted.decode())
print("Security: 3DES is stronger than single DES.")
print("Performance: single DES is faster, but both are legacy algorithms.")
print("For new applications, use AES instead.")
