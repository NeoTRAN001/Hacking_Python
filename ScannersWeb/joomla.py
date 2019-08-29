#_*_ coding: utf8 _*_

import wget
from xml.etree.ElementTree import parse
from termcolor import colored, cprint

def main():
    # Descargar el archivo xml
    download = wget.download(url='http://curso-python-0-pruebas-pentest-joomla.000webhostapp.com/administrator/manifests/files/joomla.xml')
    file = parse('joomla.xml')
    # Buscar la versión mediante la etiqueta correspondiente en el XML
    for element in file.findall('version'):
        version = element.text

    cprint('\n\nVersion: ', 'yellow', end=version + '\n\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
