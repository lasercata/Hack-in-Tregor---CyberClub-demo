#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##-Imports
from sys import argv
from sys import exit as sysexit 

from PIL import Image

##-Util

##-Main
def xor(msg: list[int], key: str) -> list[int]:
    '''Xor `msg` with `key` and return the result.'''

    key_enc = list(key.encode())

    ret = [0] * len(msg)
    for k, v1 in enumerate(msg):
        ret[k] = msg[k] ^ key_enc[k % len(key_enc)]

    return ret

def xor_image(fn_in_1: str, fn_in_2: str, fn_out: str, transparency=False) -> None:
    '''
    Xor two images and saves the result in a new image.
    Can deal with transparency.

    - fn_in_1 : the first image to xor ;
    - fn_in_2 : the second image to xor ;
    - fn_out  : where to write the result.
    '''

    #---Opening images
    im_1 = Image.open(fn_in_1)
    im_2 = Image.open(fn_in_2)
    pix_1 = im_1.load()
    pix_2 = im_2.load()

    #---Getting min size and creating image to save result
    enc_size = (min(im_1.size[0], im_2.size[0]), min(im_1.size[1], im_2.size[1]))
    if transparency:
        enc_img = Image.new('RGBA', enc_size)
    else:
        enc_img = Image.new('RGB', enc_size)

    enc_pix = enc_img.load()

    #---Xoring each pixel
    for i in range(enc_size[0]):
        for j in range(enc_size[1]):
            try:
                r1, g1, b1, t1 = pix_1[i, j]
                r2, g2, b2, t2 = pix_2[i, j]

            except ValueError:
                r1, g1, b1 = pix_1[i, j]
                r2, g2, b2 = pix_2[i, j]

                t1 = 255
                t2 = 255

            if transparency:
                enc_pix[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2, t1)
            else:
                enc_pix[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

    #---Writing result
    # enc_img.show()
    enc_img.save(fn_out)

def xor_image_simple(fn_in_1: str, fn_in_2: str, fn_out: str) -> None:
    '''
    Xor two images and saves the result in a new image.

    - fn_in_1 : the first image to xor ;
    - fn_in_2 : the second image to xor ;
    - fn_out  : where to write the result.
    '''

    #---Opening images
    im_1 = Image.open(fn_in_1)
    im_2 = Image.open(fn_in_2)
    pix_1 = im_1.load()
    pix_2 = im_2.load()

    #---Getting min size and creating image to save result
    enc_size = (min(im_1.size[0], im_2.size[0]), min(im_1.size[1], im_2.size[1]))
    enc_img = Image.new('RGB', enc_size)

    enc_pix = enc_img.load()

    #---Xoring each pixel
    for i in range(enc_size[0]):
        for j in range(enc_size[1]):
            r1, g1, b1 = pix_1[i, j]
            r2, g2, b2 = pix_2[i, j]

            enc_pix[i, j] = (r1 ^ r2, g1 ^ g2, b1 ^ b2)

    #---Writing result
    enc_img.save(fn_out)

##-Run
if __name__ == '__main__':
    if len(argv) < 4:
        print(f'Usage: {argv[0]} fn_in_1 fn_in_2 fn_out')
        sysexit()

    xor_image(argv[1], argv[2], argv[3])

