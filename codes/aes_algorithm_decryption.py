from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABi7_Hb9qVT5A31PNwuS5YOk1A1vZgSB1F8F7UYRCx1nI-Eer5N2bbtl2roTfTmdwRWbgH78URC5z_hP-5wBVbd9wCB4wE5Fkd5F1AqBUzwAj110fs=')