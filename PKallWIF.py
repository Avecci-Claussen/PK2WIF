import binascii
import ecdsa
import hashlib
import base58

def convert_privkey_to_WIF_compressed(privkey):
    # Add prefix 80 and suffix 01 to the private key (for mainnet)
    extended_key = "80" + privkey + "01"
    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    
    # Add checksum to the extended key
    final_key = extended_key + second_sha256[:8]
    
    # Convert to base58
    WIF_compressed = base58.b58encode(binascii.unhexlify(final_key))
    
    return WIF_compressed.decode()

# Your private key
privkey = "000000000000000000000000000000000000000000000000B133920D55215593"

# Convert private key to SegWit WIF
print(convert_privkey_to_WIF_compressed(privkey))
