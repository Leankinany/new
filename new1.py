import time
import sys


print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(.1)

    
print_slow("hi i am leen")    
