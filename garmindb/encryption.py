from cryptography.fernet import Fernet
import json
def generate_key():
    return Fernet.generate_key()

def encrypt_data(data, key):
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data

def save_encrypted_json(data, filename, key):
    encrypted_data = encrypt_data(json.dumps(data), key)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def load_encrypted_json(filename, key):
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = decrypt_data(encrypted_data, key)
    return json.loads(decrypted_data)
#
# # Example usage:
# if __name__ == "__main__":
#     # Generate a key (you should store this securely, not hardcode it)
#     key = generate_key()
#
#     # Your JSON data
#     json_data = {"name": "John", "age": 30, "city": "New York"}
#
#     # Encrypt and save to file
#     save_encrypted_json(json_data, "encrypted_data.json", key)
#
#     # Load and decrypt from file
#     decrypted_data = load_encrypted_json("encrypted_data.json", key)
#
#     # Display the decrypted data
#     print("Decrypted Data:", decrypted_data)
