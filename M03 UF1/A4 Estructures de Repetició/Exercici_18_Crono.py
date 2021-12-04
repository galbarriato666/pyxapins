"""
Emmanuel Manzanilla García
24/11/2021
ASIXc1b M03 UF1

Exercici 18
Exercici 18
Fer un programa que mostri per pantalla un cronòmetre, indicant les hores, minuts i segons.
Ajuda: feu servir la funció “sleep” del mòdul “time” per fer una pausa d’un segon de manera que
a pantalla es vegi avançar el temps segon a segon.
"""
from time import sleep
hores = 0
minuts = 0
segons = 0

while True:
    if segons == 60:
        segons = 0
        minuts = minuts +1
        if minuts == 60:
            minuts = 0
            hores = hores +1
            if hores == 24:
                segons = 0
                minuts = 0
                hores = 0
    if segons < 10:
        print(str(hores)+":"+str(minuts)+":0"+str(segons))
    else:
        print(str(hores)+":"+str(minuts)+":"+str(segons))
    if minuts < 10:
        print(str(hores)+":0"+str(minuts)+":"+str(segons))
    else:
        print(str(hores)+":"+str(minuts)+":"+str(segons))
    segons = segons +1
    sleep(1)


