# EXP-31: CMAC Subkey Generation
# Rb constants: 64-bit block = 0x1B; 128-bit block = 0x87.

def left_shift_one(value, block_bits):
    mask = (1 << block_bits) - 1
    return (value << 1) & mask

def generate_subkeys(block_bits, cipher_output):
    if block_bits == 64:
        rb = 0x1B
    elif block_bits == 128:
        rb = 0x87
    else:
        raise ValueError("Only 64-bit and 128-bit blocks are supported.")

    if not 0 <= cipher_output < (1 << block_bits):
        raise ValueError("Cipher output does not fit the block size.")

    msb_mask = 1 << (block_bits - 1)
    k1 = left_shift_one(cipher_output, block_bits)
    if cipher_output & msb_mask:
        k1 ^= rb

    k1_msb = 1 << (block_bits - 1)
    k2 = left_shift_one(k1, block_bits)
    if k1 & k1_msb:
        k2 ^= rb

    return k1, k2

bits = int(input("Enter block size (64 or 128): "))
l_value = int(input("Enter E(K, 0) as a hexadecimal number: "), 16)

k1, k2 = generate_subkeys(bits, l_value)
width = bits // 4

print("Rb =", hex(0x1B if bits == 64 else 0x87))
print("K1 =", format(k1, "0{}X".format(width)))
print("K2 =", format(k2, "0{}X".format(width)))

print("\\nExplanation:")
print("Left shift multiplies the bit string by x in GF(2^n).")
print("If the most significant bit was 1, reduction modulo the")
print("CMAC polynomial is performed by XOR with Rb.")
