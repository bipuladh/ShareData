import os
from simplecrypt import encrypt, decrypt


def encryptString(password, data):
    return encrypt(password, data)

def decryptByte(password, data):
    db = decrypt(password, data)
    return db.decode()