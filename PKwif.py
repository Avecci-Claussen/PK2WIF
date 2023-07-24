import hashlib
import base58

private_key = "000000000000000000000000000000000000000000000000B133920D55215593"

# Add the prefix '80' to indicate a private key
extended_key = "80" + private_key

# Perform SHA-256 hash
hash_1 = hashlib.sha256(bytes.fromhex(extended_key)).digest()

# Perform SHA-256 hash again
hash_2 = hashlib.sha256(hash_1).digest()

# Get the first 4 bytes of the second hash (checksum)
checksum = hash_2[:4]

# Append the checksum to the extended key
extended_key += checksum.hex()

# Convert the extended key to base58 encoding
wif = base58.b58encode(bytes.fromhex(extended_key)).decode()

print("WIF:", wif)
