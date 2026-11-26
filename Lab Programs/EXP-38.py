# EXP-38: Recover a 2x2 Hill Cipher Key from Known Plaintext
# Install: pip install sympy
# Supply two plaintext and corresponding ciphertext blocks.
# Each block contains two letters; A=0, ..., Z=25.

from sympy import Matrix

def letters_to_nums(text):
    text = text.upper()
    if len(text) != 2 or not text.isalpha():
        raise ValueError("Each block must contain exactly two letters.")
    return [ord(ch) - ord("A") for ch in text]

def mod_inverse_matrix(matrix, modulus):
    determinant = int(matrix.det()) % modulus
    if __import__("math").gcd(determinant, modulus) != 1:
        raise ValueError("Plaintext matrix is not invertible modulo 26.")
    return matrix.inv_mod(modulus)

p1 = input("Known plaintext block 1 (2 letters): ")
p2 = input("Known plaintext block 2 (2 letters): ")
c1 = input("Matching ciphertext block 1 (2 letters): ")
c2 = input("Matching ciphertext block 2 (2 letters): ")

try:
    # Columns are the two known plaintext/ciphertext vectors.
    P = Matrix.hstack(Matrix(letters_to_nums(p1)), Matrix(letters_to_nums(p2)))
    C = Matrix.hstack(Matrix(letters_to_nums(c1)), Matrix(letters_to_nums(c2)))

    P_inv = mod_inverse_matrix(P, 26)
    K = (C * P_inv).applyfunc(lambda x: int(x) % 26)

    print("Recovered Hill key matrix:")
    print(K)
except Exception as error:
    print("Could not recover key:", error)
