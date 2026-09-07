from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

# Initialize key
cipher = Fernet(key)

# Define secret message
secret_message = "hewwo >:3c"

# Encrypt message
message_bytes = secret_message.encode("utf-8")
cipher_text = cipher.encrypt(message_bytes)

# Print results
print(f"Original: {secret_message}")
print(f"Encrypted: {cipher_text}")
print(f"Key: {key.decode()}")

# Decrypt the message
decrypted_bytes = cipher.decrypt(cipher_text)
decrypted_message = decrypted_bytes.decode('utf-8')

print(f"Decrypted: {decrypted_message}")