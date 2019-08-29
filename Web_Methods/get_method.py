#__*__ coding: utf8 __*__

import sys
import requests
import argparse
from termcolor import colored, cprint

parser = argparse.ArgumentParser(description="Detector de Headers")
parser.add_argument('-t', '--target', help='Dirección HTTP del objetivo')
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            i = 1
            url = requests.get(url=parser.target)
            headers = dict(url.headers)

            cprint(' ==== Conexión aceptada ====', 'cyan', end='\n\n')

            for line in headers:
                cprint(i, 'magenta', end=" ")
                print(line + ' : ' + headers[line])
                i = i + 1
        except:
            pass
    else:
        cprint('\n\nNo hay objetivo', 'red', end='\n\n')

if __name__ == '__main__':
    main()