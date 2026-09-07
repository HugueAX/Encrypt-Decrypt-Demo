from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Generate a Public/Private Key Pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Define secret message
secret_message = "hewwo >:3c"
message_bytes = secret_message.encode('utf-8')

# Encrypt message using public key
encrypted_message = public_key.encrypt(
    message_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Original: {secret_message}")
print(f"Encrypted: {encrypted_message}")
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

# Decrypt message using private key
decrypted_bytes = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decode back to a readable string
decrypted_message = decrypted_bytes.decode('utf-8')
print(f"Decrypted PLaintext: {decrypted_message}")

