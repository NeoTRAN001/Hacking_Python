#!_*_ coding: utf8 _*_

import requests
from os import path
from progress.bar import Bar
from termcolor import colored, cprint

def banner():
    b =  """
 __    __        ___  ___
/ / /\ \ \      / __\/ __\  |
\ \/  \/ /____ / _\ /__\//  |
 \  /\  /_____/ /  / \/  \  |
  \/  \/      \/   \_____/  |
 Wordpress por fuerza bruta |
 ___________________________|

    """

    return b

def main():
    if path.exists("wp_plugins.txt"):
        url = "https://curso--python-0-pruebas.000webhostapp.com/"
        file = open("wp_plugins.txt", 'r')
        file = file.read().split('\n')
        list = []
        b = Bar("Working...", max=len(file))

        for plugin in file:
            b.next()
            try:
                petition = requests.get(url=(url + '/' + plugin))
                if petition.status_code == 200:
                    final = url + '/' + plugin
                    list.append(final.split('/')[-2])
            except:
                cprint('\n\nNo se ha podido acceder al sitio de forma correcta', 'red', end='\n\n')
        b.finish()

        for plugin in list:
            cprint('Plugin encontrado: ', 'cyan', end=plugin )
    else:
        cprint('\n\nEl archivo wp_plugins.txt no se ha encontrado, y es necesario para realizar el método de fuerza bruta', 'grey', 'on_yellow', end='\n\n')

if __name__ == '__main__':
    try:
        cprint(banner(), 'yellow', end="")
        main()
    except KeyboardInterrupt:
        exit()
