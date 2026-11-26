# EXP-22: S-DES Encryption and Decryption using CBC Mode

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]
S0 = [[1, 0, 3, 2], [3, 2, 1, 0],
      [0, 2, 1, 3], [3, 1, 3, 2]]
S1 = [[0, 1, 2, 3], [2, 0, 1, 3],
      [3, 0, 1, 0], [2, 1, 0, 3]]

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def generate_keys(key):
    p = permute(key, P10)
    left, right = p[:5], p[5:]
    left, right = left[1:] + left[:1], right[1:] + right[:1]
    k1 = permute(left + right, P8)
    left, right = left[2:] + left[:2], right[2:] + right[:2]
    k2 = permute(left + right, P8)
    return k1, k2

def sbox(value, box):
    row = int(value[0] + value[3], 2)
    col = int(value[1] + value[2], 2)
    return format(box[row][col], "02b")

def fk(bits, key):
    left, right = bits[:4], bits[4:]
    expanded = xor(permute(right, EP), key)
    s = sbox(expanded[:4], S0) + sbox(expanded[4:], S1)
    return xor(left, permute(s, P4)) + right

def encrypt_block(block, k1, k2):
    x = fk(permute(block, IP), k1)
    x = x[4:] + x[:4]
    return permute(fk(x, k2), IP_INV)

def decrypt_block(block, k1, k2):
    x = fk(permute(block, IP), k2)
    x = x[4:] + x[:4]
    return permute(fk(x, k1), IP_INV)

def cbc_encrypt(data, key, iv):
    k1, k2 = generate_keys(key)
    result, previous = "", iv
    for i in range(0, len(data), 8):
        block = xor(data[i:i+8], previous)
        encrypted = encrypt_block(block, k1, k2)
        result += encrypted
        previous = encrypted
    return result

def cbc_decrypt(data, key, iv):
    k1, k2 = generate_keys(key)
    result, previous = "", iv
    for i in range(0, len(data), 8):
        block = data[i:i+8]
        result += xor(decrypt_block(block, k1, k2), previous)
        previous = block
    return result

key = "0111111101"
iv = "10101010"
plaintext = "0000000100100011"

ciphertext = cbc_encrypt(plaintext, key, iv)
decrypted = cbc_decrypt(ciphertext, key, iv)

print("Key:", key)
print("IV:", iv)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
