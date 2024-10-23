# Hack'in Tregor Day - ENSSAT CyberClub presentation

Source code for the demo of the ENSSAT CyberClub presentation during the [Hack'in Tregor Day](https://hackintregor.softr.app).

## Presentation
For more information on the concepts in this challenge, read the [presentation slides](presentation/Presentation.pdf).

## Creating the challenge
Run :
```bash
chmod u+x make_chall.sh

./make_chall.sh
```

This will generate a zip file `chall.zip` containing the challenge files (two images).

## Scripts

Four script are present in the folder `scripts` :
- `generate_random_image.py` : it generates an image with pixels of random colors ;
- `xor_two_images.py` : it apply `xor` between two images ;
- `hide_text.py` : hides a message in an image ;
- `read_hidden_text.py` : reads a message hidden by the previous script.

To use any script, run
```bash
python3 [script name]
```
to get the help.

Then run :
```bash
python3 [script name] [arguments]
```
with the right arguments.
