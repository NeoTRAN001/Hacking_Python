#_*_ coding: utf8 _*_

import sys
import argparse
from Wappalyzer import WebPage, Wappalyzer
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description='Analizar tecnologías de una Web con Wappalyzer')
parser.add_argument('-a', '--address', help='Web Address')
parser = parser.parse_args()

def main():
    wap = Wappalyzer.latest()
    try:
        if parser.address:
            web = WebPage.new_from_url(parser.address) # URL de la web que se va a escanear
            tecnologias = wap.analyze(web) # Dar un formato a la respuesta en forma de lista

            for t in tecnologias:
                cprint('Tecnología detectada:', 'yellow', end=' ')
                print(t)
        else:
            cprint('\nNecesito una dirección web', 'red', end='\n\n')
    except:
        cprint('\nHa ocurrido un error', 'red', end='\n\n')

if __name__ == '__main__':
    try:
        main()
    except:
        cprint('\nSaliendo...', 'red', end='\n\n')
        exit()
