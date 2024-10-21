#!/bin/bash

##-Init
x=768
y=768
img="src/img1.png"

msg="This is the flag !"

##-make challenge
mkdir chall

echo "Generating the key image ..."
./scripts/generate_random_image.py chall/key.png $x $y || exit

echo "Hiding the flag in a temp image ..."
./scripts/hide_text.py "$img" "$msg" tmp/text_hidden.png || exit

echo "Xoring ..."
./scripts/xor_two_images.py chall/key.png tmp/text_hidden.png chall/xor.png || exit

zip -rv chall.zip chall/
