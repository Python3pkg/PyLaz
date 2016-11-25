from PyLaz.PyLaz import *
import signal
import os
import time

global cont
def receive_signal(signum,stack):
    global cont
    print("SIGINT")
    cont = False

cont = True

signal.signal(signal.SIGINT,receive_signal)

lazurite = PyLaz()

result = lazurite.init()

result = lazurite.begin(36,0xabcd,100,20)
result = lazurite.rxEnable()

while cont:
    result = lazurite.available()
    if result > 0:
        print(lazurite.read())
    try:
        result = lazurite.send(0xabcd,0x5f59,"hello")
        print (result)
    except Exception as e:
        print (e)

    time.sleep(1)

result = lazurite.close()
result = lazurite.remove()

