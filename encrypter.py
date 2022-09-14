import os

from cryptography.fernet import Fernet


def generate_key():
    print("Generating a new key...")
    key = Fernet.generate_key()
    file = open('secret.key', 'wb')
    file.write(key)
    file.close()
    print('Key generated!')


def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text)


def decrypt_text(text, key):
    f = Fernet(key)
    return f.decrypt(text)


def load_key():
    if not os.path.isfile('secret.key'):
        print("No existing key found.")
        generate_key()

    key_file = open("secret.key", "rb")
    key = key_file.read()
    key_file.close()

    print("Key Loaded")
    return key


def start():
    key = load_key()

    if key:
        if os.path.isfile("source.txt"):
            print("Encrypting file")
            source_file = open("source.txt")  # default mode is r
            dest_file = open("source.enc.txt", "wb")
            contents = source_file.read().encode()
            source_file.close()
            contents = encrypt_text(contents, key)
            dest_file.write(contents)
            dest_file.close()
            os.remove("source.txt")
        elif os.path.isfile("source.enc.txt"):
            print("Decrypting file")
            source_file = open("source.enc.txt")  # default mode is r
            dest_file = open("source.txt", "w")
            contents = source_file.read().encode()
            source_file.close()
            contents = decrypt_text(contents, key)
            dest_file.write(contents.decode())
            dest_file.close()
            os.remove("source.enc.txt")
        else:
            print("Nothing to do")


start()
