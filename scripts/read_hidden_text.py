#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##-Imports
from sys import argv
from sys import exit as sysexit 

from PIL import Image

##-Main
def convert_from_base(n: list[int], base: int) -> int:
    '''
    Convert `n` from base `base` to base 10.

    - n    : the number, e.g [4, 12] for 7c in base 16 (little endian) ;
    - base : the base in which the number is written.
    '''

    return sum(x * base**k for k, x in enumerate(reversed(n)))

def get_digit_from_col(col: int, base: int = 2) -> int:
    '''Returns the hidden digit from `col`.'''

    b = base + 1 # To read the `base` (delimiters)

    return col % b

def convert_msg_back(msg_enc: list[int], base: int = 2) -> str:
    '''
    The below description is for the inverse direction.

    Convert `msg` in a list of numbers in the base `base`.

    Delimiter between chars : `base`.
    End delimiter : `base, base, base, base`.

    For example, in base 2 : 'ab' -> [97, 98] -> [1100001, 1100010] -> [1, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2]
    '''

    while msg_enc[-1] == base: #Removing the trailing [base, base, base, base].
        msg_enc = msg_enc[:-1]

    msg_sep = [[]] # [[1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0]] useful when base > 10
    for k in msg_enc:
        if k == base:
            msg_sep.append([])
        else:
            msg_sep[-1].append(k)

    int_lst = [convert_from_base(n, base) for n in msg_sep]
    ret = ''.join(chr(k) for k in int_lst)

    return ret

def read_message(fn_in: str, base: int = 2) -> str:
    '''Reads the message hidden in the image'''

    im = Image.open(fn_in)
    pix = im.load()

    enc_msg = []

    i = 0
    j = 0
    while i < im.size[0] and j < im.size[1]:
        for col in pix[i, j]:
            enc_msg.append(get_digit_from_col(col, base))

        if len(enc_msg) >= 2 and (
                (enc_msg[-1] == base and enc_msg[-2] == base)
                or (enc_msg[-2] == base and enc_msg[-3] == base)
                or (enc_msg[-3] == base and enc_msg[-4] == base)
            ): # End of the message
            break
        
        # Increment
        if j == im.size[1] - 1:
            j = 0
            i += 1
        else:
            j += 1

    print(enc_msg)
    return convert_msg_back(enc_msg, base)

##-Run
if __name__ == '__main__':
    if len(argv) < 2:
        print(f'Usage: {argv[0]} fn_in [base=2]')
        sysexit()

    if len(argv) >= 3:
        base = int(argv[2])
    else:
        base = 2

    print(read_message(argv[1], base))

