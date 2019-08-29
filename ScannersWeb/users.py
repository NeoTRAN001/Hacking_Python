#_*_ coding: utf8 _*_

import json
import urllib
from termcolor import colored, cprint

def main():
    url = urllib.urlopen('https://curso--python-0-pruebas.000webhostapp.com/wp-json/wp/v2/users')

    for u in json.loads(url.read()):
        user = u['slug']

    cprint('\nUser: ', 'cyan', end=user+"\n\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
