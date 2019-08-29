#_*_ coding: utf8 _*_
import sys
import requests
from termcolor import colored ,cprint
from bs4 import BeautifulSoup

def main():
    url = "https://curso--python-0-pruebas.000webhostapp.com/"
    header = {'User-Agent':'Firefox'}
    petition = requests.get(url=url, headers=header)
    soup = BeautifulSoup(petition.text, 'html5lib')
    # Buscar dentro del archivo html todas las etiquetas meta
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator': # generator es como wordpress identifica la versión
            version = v.get('content')
    cprint('\n\nVersion: ', 'yellow', end='')
    cprint(version, 'white', end='\n\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('\nSaliendo', 'magenta', end='\n\n')
        exit()
