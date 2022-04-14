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

#lista = []
pares =[]
impares = []

sumpares = 0 #hago esta referencia para usarla en el if
sumimpares = 0
for vuelta in range(100): #numero de vueltas (repeticiones)
    num = random.randint(1, 50) #No necesito que se me guarde num. Esta variable es de 100 vueltas, generame numeros entre 1 y 50
    #lista.append(num) #aqui hacemos un append a lista para que los vaya guardando, aunque no pide ni lo usaremos mas, solo de referencia.

    if vuelta % 2 == 0: #esta 'vuelta' es el for entero con el random randint ya hecho
        pares.append(num) #añadimos las vueltas de randit pares para luego poder sumarlas
        sumpares = sumpares + num #va sumando reiterativamente los numeros en la variable sumpares
    else: #es impar pq es todo lo demas que es lo contrario
        impares.append(num)
        sumimpares = sumimpares + num

    #si la posicion de los 100 numeros entre 1-50 es divisible % 2 = 0

mediapares = sumpares / len(pares)
mediaimpares = sumimpares / len(impares)

print(mediapares)
print(mediaimpares)

