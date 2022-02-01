"""
Emmanuel Manzanilla García
1r ASIXcB
19/01/2022

2. Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les  posicions senars.

Per aconseguir nombres aleatoris en Python podem utilitzar la funció random.randint(limitInferior,limitSuperior)

Program to generate a random number between 0 and 9
importing the random module
import random
print(random.randint(0,9))

"""
import random


pares =[]
impares = []

sumpares = 0
sumimpares = 0
for vuelta in range(100):
    num = random.randint(1, 50)

    if vuelta % 2 == 0:
        pares.append(num)
        sumpares = sumpares + num #
    else:
        impares.append(num)
        sumimpares = sumimpares + num



mediapares = sumpares / len(pares)
mediaimpares = sumimpares / len(impares)

print(mediapares)
print(mediaimpares)

