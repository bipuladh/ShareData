import pyAesCrypt as crypt 
import os

BUFFER_SIZE = 64 * 1024

def enc_dec(src, des, password, enc=True):
    if enc == True:
        crypt.encryptFile(src, des, password, BUFFER_SIZE)
    else:
        crypt.decryptFile(src, des, password, BUFFER_SIZE)


def encryptfile(src_path,dest_path,password):
    #Encryptfile
    des_file = (str(src_path)).split(os.path.sep)[-1] + '.aes'
    des_path = os.path.join(dest_path,des_file)
    enc_dec( src_path, des_path, password, enc=True)

def decryptfile(src_path, dest_path, password):
    des_file= '.'.join( (str(src_path)).split(os.path.sep)[-1].split('.')[:-1] )
    des = os.path.join(dest_path,des_file)
    enc_dec(src_path, des, password, enc = False)



