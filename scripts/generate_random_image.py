#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##-Imports
from sys import argv
from sys import exit as sysexit 

from random import randint

from PIL import Image

##-Util

##-Main
def generate_random_image(fn_out: str, size: tuple[int, int], transparency=False) -> None:
    '''Generates an image of size `size` filled with random pixels.'''

    if transparency:
        img = Image.new('RGBA', size)
    else:
        img = Image.new('RGB', size)

    pix = img.load()

    for i in range(size[0]):
        for j in range(size[1]):
            if transparency:
                pix[i, j] = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))
            else:
                pix[i, j] = (randint(0, 255), randint(0, 255), randint(0, 255))

    # enc_img.show()
    img.save(fn_out)

##-Run
if __name__ == '__main__':
    if len(argv) < 4:
        print(f'Usage: {argv[0]} fn_out x y')
        sysexit()

    generate_random_image(argv[1], (int(argv[2]), int(argv[3])))

