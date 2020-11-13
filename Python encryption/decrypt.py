from cryptography.fernet import Fernet

def load_key():

    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):

    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == '__main__':
    decrypt_message()
    
