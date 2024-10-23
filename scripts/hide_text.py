#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##-Imports
from sys import argv
from sys import exit as sysexit 

from PIL import Image

##-Util
def convert_to_base(n: int, b: int) -> list[int]:
    '''
    From https://stackoverflow.com/a/28666223

    Converts `n` from base 10 to `b`.
    '''

    if n == 0:
        return [0]

    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    return digits[::-1]

##-Main
def hide_in_color(x: int, col: int, base: int = 2) -> int:
    '''
    Hides `x` in the LSB of `col`.

    - x    : an int in [0 ; `base` - 1] (the digit to hide) ;
    - col  : an int in [0 ; 255] ;
    - base : the base of the number to hide.
    '''

    b = base + 1 # To write the delimiters (`base`)

    ret = b * (col // b) + x

    if ret > 255:
        ret = b * ((col - b) // b) + x

    return ret

def convert_msg(msg: str, base: int = 2) -> list[int]:
    '''
    Convert `msg` in a list of numbers in the base `base`.

    Delimiter between chars : `base`.
    End delimiter : `base, base, base, base`.

    For example, in base 2 : 'ab' -> [97, 98] -> [1100001, 1100010] -> [1, 1, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2]
    '''

    ret = []

    for l in msg:
        ret += convert_to_base(ord(l), base)
        ret.append(base) # Adding a delimiter between chars

    ret.append(base)
    ret.append(base)
    ret.append(base)
    
    return ret

def hide_message_in_image(fn_in: str, msg: str, fn_out: str, base: int = 2) -> None:
    '''Hides `msg` in the LSB of the image colors pixels.'''

    im = Image.open(fn_in)
    pix = im.load()

    enc_img = im.copy()
    enc_pix = enc_img.load()

    enc_msg = convert_msg(msg, base)
    # print(enc_msg)

    k = 0
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            val = list(pix[i, j])

            # val = [r, g, b]
            enc_val = []

            for v in val:
                if k < len(enc_msg):
                    enc_val.append(hide_in_color(enc_msg[k], v, base))
                else:
                    enc_val.append(v)

                k += 1

            enc_pix[i, j] = tuple(enc_val)

            if k >= len(enc_msg):
                break

        if k >= len(enc_msg):
            break

    enc_img.save(fn_out)

##-Run
if __name__ == '__main__':
    if len(argv) < 4:
        print(f'Usage: {argv[0]} fn_in msg fn_out [base=2]')
        sysexit()

    if len(argv) >= 5:
        base = int(argv[4])
    else:
        base = 2

    hide_message_in_image(argv[1], argv[2], argv[3], base)

