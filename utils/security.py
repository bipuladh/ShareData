import os
from simplecrypt import encrypt, decrypt


def encryptString(data,password):
    return encrypt(password, data)

def decryptByte(data, password):
    db = decrypt(password, data)
    return db.decode()