# EXP-21: Padding for ECB, CBC and CFB Modes

def pad_bits(data, block_size):
    if not data or any(bit not in "01" for bit in data):
        raise ValueError("Enter a non-empty binary string.")
    if block_size <= 0:
        raise ValueError("Block size must be positive.")

    padded = data + "1"
    while len(padded) % block_size != 0:
        padded += "0"
    return padded

plaintext = input("Enter binary plaintext: ").strip()
block_size = int(input("Enter block/segment size: "))

try:
    result = pad_bits(plaintext, block_size)
    print("Original:", plaintext)
    print("Padded:  ", result)
    print("Padding bits added:", len(result) - len(plaintext))
except ValueError as error:
    print("Error:", error)

print("\\nMotivation: Always padding makes the end of the message")
print("unambiguous, including when the original message fills a block.")
