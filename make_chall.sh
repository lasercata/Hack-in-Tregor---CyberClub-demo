#!/bin/bash

##-Init
x=768
y=768
img="src/img1.png"

key_img_fn="2b.png"
xored_img_fn="xor_not_2b.png"

msg="This is the flag !"

##-make challenge
mkdir chall

echo "Generating the key image ..."
./scripts/generate_random_image.py chall/$key_img_fn $x $y || exit

echo "Hiding the flag in a temp image ..."
./scripts/hide_text.py "$img" "$msg" tmp/text_hidden.png 10 || exit

echo "Xoring ..."
./scripts/xor_two_images.py chall/$key_img_fn tmp/text_hidden.png chall/$xored_img_fn || exit

zip -rv chall.zip chall/
