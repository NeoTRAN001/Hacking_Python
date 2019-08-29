#_*_ coding: utf8 _*_

import sys
import argparse
from os import path
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description='Cipher by numerical base')
parser.add_argument('-m', '--message', help='Message')
parser.add_argument('-f', '--file', help='[read] or [write]')
parser.add_argument('-a', '--address', help='Address file')
parser.add_argument('-b', '--base', help='Numerical base')
parser.add_argument('-o', '--option', help='[Cipher] or [Decipher]')
parser = parser.parse_args()

def write(op):
    if parser.address:
        file = open(parser.address, 'w')
        if op == 'c':
            file.write(cipher(parser.message))
        elif op == 'd':
            file.write(decipher(parser.message))
        file.close()


def read(op):
    if parser.address:
        if path.exists(parser.address):
            file = open(parser.address, 'rb')
            cprint('Resultado:', 'yellow', end='\n')
            if op == 'c':
                for line in file:
                    cprint(cipher(line), 'white', end='\n')
            elif op == 'd':
                for line in file:
                    cprint(decipher(line), 'white', end='\n')

        else:
            cprint('\n\nEl archivo no se ha encontrado', 'red', end='\n\n')

    return None

def cipher(message):
    new_word = ''

    if parser.base:
        for letter in message:
            ascii_value = ord(letter)
            new_letter = ''
            if parser.base == '2':
                new_letter = bin(ascii_value)
            elif parser.base == '8':
                new_letter = oct(ascii_value)
            elif parser.base == '10':
                new_letter = str(ascii_value)
            elif parser.base == '16':
                new_letter = hex(ascii_value)

            new_word = new_word + ' ' + new_letter

        return new_word
    else:
        cprint('\n\nNecesitas una base númerica para continuar', 'red', end='\n\n')

    return 'Nop'

def decipher(message):
    new_word = ''

    if parser.base:
        for letter in message.split(' '):
            try:
                new_letter = int(letter, int(parser.base))

                new_word = new_word + chr(new_letter)
            except:
                cprint(new_word, 'white', end='')

        return new_word
    else:
        cprint('\n\nNecesitas una base númerica para continuar', 'red', end='\n\n')

    return 'Nop'

def option(op):
    if parser.file:
        if parser.file == 'read':
            read(op)
        elif parser.file == 'write':
            write(op)
        else:
            cprint('Ingresar un valor valido a la bandera -f', 'red', end='\n\n')
    else:
        if parser.message:
            if op == 'c':
                cprint('\n\nResult:', 'yellow', end=' ')
                print(cipher(parser.message))
            elif op == 'd':
                cprint('\n\nResult:', 'yellow', end=' ')
                print(decipher(parser.message))

def main():
    if parser.option:
        if parser.option == 'Cipher':
            option('c')
        elif parser.option == 'Decipher':
            option('d')

if __name__ == '__main__':
    main()
