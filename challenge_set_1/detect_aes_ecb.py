# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:32:07 2020

@author: john lee
"""

def count_repetitions(ciphertext, block_size):
    chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
    number_of_repetitions = len(chunks) - len(set(chunks))
    result = {
        'ciphertext': ciphertext,
        'number of repetitions': number_of_repetitions
    }
    return result

def main():
    ciphertext = [bytes.fromhex(line.strip()) for line in open('8.txt')]
    block_size = 16
    repetitions = [count_repetitions(cipher, block_size) for cipher in ciphertext]
    
    most_repetitions = sorted(repetitions, key=lambda x: x['number of repetitions'], reverse=True)[0]
    
    print('ciphertext: {}'.format(most_repetitions['ciphertext'].hex()))
    print('repeating blocks: {}'.format(most_repetitions['number of repetitions']))
    
if __name__ == '__main__':
    main()