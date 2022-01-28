# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:57:16 2020

@author: john lee
"""

# Break repeating-key XOR
import base64

def get_english_score(input_bytes):
    """Compares each input byte to a character frequency 
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language.
    """

    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes

def bruteforce_single_char_xor(ciphertext):
    """Performs a singlechar xor for each possible value(0,255), and
    assigns a score based on character frequency. Returns the result
    with the highest score.
    """
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        score = get_english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
            }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'], reverse=True)[0]

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

def calculate_hamming_distance(input_byte_1, input_byte_2):
    distance = 0
    for b1, b2 in zip(input_byte_1, input_byte_2):
        difference = b1 ^ b2
        
        for bits in bin(difference):
            if bits == '1':
                distance += 1
    return distance

def break_repeating_key_xor(ciphertext):
    
    avg_hamming_dist = []
    
    for keysize in range(2, 41):
        
        distances = []
        
        chunks = [ciphertext[i: i+keysize] for i in range(0, len(ciphertext), keysize)]
        
        while True:
            try:
                chunk_1 = chunks[0]
                chunk_2 = chunks[1]
                
                distance = calculate_hamming_distance(chunk_1, chunk_2)
                distances.append(distance/keysize)
                
                del chunks[0]
                del chunks[1]
            
            except Exception as e:
                break
        
        result = {
            'key': keysize,
            'avg dist': sum(distances)/len(distances)
            }
        
        avg_hamming_dist.append(result)
        
    potential_key_size = sorted(avg_hamming_dist, key=lambda x: x['avg dist'])[0]['key']
    key = b''
    
    for i in range(potential_key_size):
        block = b''
        
        for j in range(i, len(ciphertext), potential_key_size):
            block += bytes([ciphertext[j]])
        
        key += bytes([bruteforce_single_char_xor(block)['key']])
    
    potential_message = (repeating_key_xor(ciphertext, key), key)
    return potential_message

def main():
    with open('6.txt') as input_file:
        ciphertext = base64.b64decode(input_file.read())
    result, key = break_repeating_key_xor(ciphertext)
    print("Key: {} /nMessage: {}".format(key,result))
    
if __name__ == '__main__':
    main()
    
        
    
                
                
        