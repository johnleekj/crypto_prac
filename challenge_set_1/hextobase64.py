# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:12:31 2020

@author: john lee
"""

import codecs

hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
byte = codecs.decode(hex, 'hex')
print(byte)
print(b64)

def hextob64(hex):
    cipher = codecs.encode(codecs.decode(hex,'hex'), 'base64').decode()
    return cipher

print(hextob64(hex))
    