# EXP-34: Padding for ECB, CBC and CFB data blocks/segments

def bit_padding(message, size):
    if not message or any(bit not in "01" for bit in message):
        raise ValueError("Message must be a non-empty binary string.")
    if size <= 0:
        raise ValueError("Block/segment size must be positive.")

    padded = message + "1"
    while len(padded) % size != 0:
        padded += "0"
    return padded

message = input("Enter plaintext in binary: ").strip()
size = int(input("Enter block or segment size: "))

try:
    padded = bit_padding(message, size)
    print("Original plaintext:", message)
    print("Padded plaintext:  ", padded)
    print("Number of padding bits:", len(padded) - len(message))
except ValueError as error:
    print("Error:", error)

print("\\nMotivation: Always adding padding, even to a complete final")
print("block, makes the padding convention unambiguous and lets the")
print("receiver identify that padding is present.")
