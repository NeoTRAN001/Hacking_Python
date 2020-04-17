#_*_ coding: utf8 _*_

from subprocess import check_output
import subprocess

info = check_output('lshw', stderr=subprocess.STDOUT)

open_info = open('test.txt', 'w+')
open_info.write(info)
open_info.close()