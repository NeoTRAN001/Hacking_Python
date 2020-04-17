#_*_ coding: utf8 _*_

import os
import subprocess

devnull = open(os.devnull, 'w')
# Mandar el resultado al devnull para no mostrar en la terminal
#sub_process = subprocess.call(['ping', '-c', '2', '1.1.1.1'], stdout=devnull, stderr=subprocess.STDOUT)
sub_process = subprocess.call(['ping', '1.1.1.1'], stdout=devnull, stderr=subprocess.STDOUT)


if(sub_process == 1):
    print("El proceso se ha ejecutado de forma correcta")
else:
    print("El proceso ha fallado")