#_*_ coding: utf8 _*_
import sys
import requests
from termcolor import colored ,cprint
from bs4 import BeautifulSoup

def main():
    url = "https://curso--python-0-pruebas.000webhostapp.com/"
    header = {'User-Agent':'Firefox'}
    petition = requests.get(url=url, headers=header)
    soup = BeautifulSoup(petition.text,'html5lib')

    i = 1

    for link in soup.find_all('link'):
        if '/wp-content/themes/' in link.get('href'):
            them = link.get('href')
            them = them.split('/')
            if 'themes' in them:
                pos = them.index('themes')
                theme = them[pos+1]
                print("Tema en uso: " + theme)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('Saliendo', 'magenta', end='\n\n')
        exit()
