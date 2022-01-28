# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 18:15:47 2020

@author: john lee
"""

# Repeating key XOR



def repeating_key_xor(message_bytes, key):
    
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else: 
            index += 1
    return output_bytes

def main():
    encrypted = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    ciphertext = repeating_key_xor(message, key)
    print(ciphertext.hex())
    if (ciphertext.hex() == encrypted):
        print('working')
    
if __name__ == '__main__':
    main()
                               