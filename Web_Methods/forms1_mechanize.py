#_*_ coding: utf8 _*_

import sys
import argparse
import mechanize
from bs4 import BeautifulSoup
from termcolor import colored, cprint
# Definir los parámetros que vamos a recibir
parser = argparse.ArgumentParser()
parser.add_argument('-b','--buscar',help='Opción a buscar')
parser = parser.parse_args()

def main():
    if parser.buscar:
        bus = mechanize.Browser() # Creamos un objeto de tipo navegador
        bus.set_handle_robots(False) # Para que no haga seguimiento del txt y de algún error
        bus.set_handle_equiv(False)
        # Configurar el tipo de navegador que vamos a utilizar y abrir el sitio web
        bus.addheaders = [('User-Agent', 'Firefox')]
        bus.open("https://www.google.com")
        # Recorrer todos los formularios que nos da google
        cprint('------- Estructura del formulario de google -------', 'yellow', end='\n')
        for n in bus.forms():
            cprint(n, 'white', end='\n')
        cprint('---------------------------------------------------', 'yellow', end='\n')

        bus.select_form(nr=0)
        bus['q'] = parser.buscar # Variable de busqueda del formulario de Google
        # Ejecutar la busqueda
        bus.submit()
        # Mostrando respuesta
        cprint('\n\n------- Respuesta de la busqueda sin formato -------', 'cyan', end='\n\n')
        cprint(bus.response().read(), 'white', end='\n\n')
        # Dando formato a la respuesta
        p = BeautifulSoup(bus.response().read(), 'html5lib')
        i = 1
        cprint('\n\n------- Respuesta de la busqueda con formato -------', 'green', end='\n')
        for link in p.find_all('a'):
            cprint(i, 'cyan', end=' ')
            cprint(link.get('href'), 'white', end='\n\n')
            i = i + 1
    else:
        cprint('\n\nNo ha ingresado una palabra a buscar', 'red', end='\n\n')

if __name__ == '__main__':
    try:
        main()
    except:
        print('Saliendo...')
        exit()
