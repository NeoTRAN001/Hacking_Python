#_*_ coding: utf8 _*_$

import sys
import requests
import argparse
from os import path
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description='Subir un archivo por metodo post')
parser.add_argument('-f', '--file', help='Ruta del archivo a subir')
parser = parser.parse_args()

def main():
    if parser.file:
        if path.exists(parser.file):
            file = open(parser.file, 'rb')
            headers = {'User-Agent' : 'Firefox'}
            petition = requests.post(url='https://curso--python-0-prueba-pentest.000webhostapp.com/index.php', files={'uploaded_file':file})

            if parser.file in petition.text:
                cprint('Respuesta:', 'yellow', end=' ')
                cprint(petition.text, 'magenta', end='\n\n')
                cprint('\nArchivo subido con exito!', 'cyan', end='\n\n')
            else:
                cprint('\n\nFallo al subir el archivo', 'red', end='\n\n')
        else:
            cprint('\n\nNo existe el archivo', 'red', end='\n\n')
    else:
        cprint('\n\nSe necesita un archivo para subir', 'red', end='\n\n')

if __name__ == '__main__':
    try:
       main()
    except:
         print('Saliendo...')
