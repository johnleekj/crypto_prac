# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:26:05 2020

@author: john lee
"""
import codecs

message = "1c0111001f010100061a024b53535009181c"
messagebytes = codecs.decode(message, 'hex')

key = "686974207468652062756c6c277320657965"
keybytes = codecs.decode(key,'hex')

combined = zip(messagebytes, keybytes)

cipher = b''

for b1, b2 in zip(messagebytes, keybytes):
    cipher += (bytes([b1^b2]))
    
print(cipher.decode())

def xor_byte_strings(input_bytes_1, input_bytes_2):
    xord_bytes = b''
    for b1, b2 in zip(input_bytes_1, input_bytes_2):
        xord_bytes += (bytes([b1^b2]))
    return xord_bytes

print(xor_byte_strings(messagebytes, keybytes))