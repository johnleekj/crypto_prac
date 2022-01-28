# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:42:35 2020

@author: john lee
"""

# AES in ECB mode

import base64

from Crypto.Cipher import AES

def decrypt_ecb_cipher(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    key = b'YELLOW SUBMARINE'
    with open('7.txt') as fh:
        ciphertext = base64.b64decode(fh.read())
    message = decrypt_ecb_cipher(ciphertext, key)
    print(message)
    
if __name__ == '__main__':
    main()