#_*_ coding: utf8 _*_

import sys
import requests
import argparse
from os import path
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description='Script de cifrado cesar')
parser.add_argument('-c', '--cipher', help='Ingresar el mensaje a cifrar')
parser.add_argument('-d', '--decipher', help='Ingresar el mensaje a descifrar')
parser.add_argument('-n', '--number', help='Número de espacios en el que se recorrera cada letra')
parser = parser.parse_args()

def cipher():
    cprint('\n\nResult:', 'yellow', end=' ')
    for letter in parser.cipher:
        ascii_value = ord(letter)
        new_letter = chr(int(ascii_value) + int(parser.number))
        cprint(new_letter, 'green', end='')

    cprint('\n\nTanks for use !!', 'cyan', end='\n\n')

def decipher():
    cprint('\n\nResult:', 'yellow', end=' ')

    for letter in parser.decipher:
        ascii_value = ord(letter)
        new_letter = chr(int(ascii_value) - int(parser.number))
        cprint(new_letter, 'green', end='')

    cprint('\n\nTanks for use !!', 'cyan', end='\n\n')

def main():
    if parser.cipher and parser.number:
        cipher()
    elif parser.decipher and parser.number:
        decipher()
    else:
        cprint('\nDebe de ingresar los parámetros adecuados', 'red', end='\n\n')

if __name__ == '__main__':
    main()
