# EXP-32: DSA signatures and the effect of a per-signature random k
# Install: pip install pycryptodome

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

key = DSA.generate(1024)
message = b"Cryptography practical experiment"

hash_value = SHA256.new(message)

signer1 = DSS.new(key, "fips-186-3")
signature1 = signer1.sign(hash_value)

# A fresh DSS signer generates a fresh per-signature nonce k.
signer2 = DSS.new(key, "fips-186-3")
signature2 = signer2.sign(SHA256.new(message))

print("Message:", message.decode())
print("DSA signature 1:", signature1.hex())
print("DSA signature 2:", signature2.hex())
print("DSA signatures are different:", signature1 != signature2)

verifier = DSS.new(key.public_key(), "fips-186-3")
verifier.verify(SHA256.new(message), signature1)
verifier.verify(SHA256.new(message), signature2)
print("Both DSA signatures are valid.")

print("\\nImplication: DSA signatures normally differ because a fresh")
print("secret nonce k is used. Reusing or exposing k can reveal the")
print("private signing key. RSA PKCS#1 v1.5 signatures are deterministic")
print("for the same key and message; RSA-PSS uses random salt by default.")
