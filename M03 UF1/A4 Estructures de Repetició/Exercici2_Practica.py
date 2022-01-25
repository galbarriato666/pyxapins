"""
Emmanuel Manzanilla García
24/11/2021
ASIXc1b M03 UF1

Exercici 3

Crea una aplicació que permet endevinar un número.
L'aplicació genera un nombre “aleatori” de l'1 al 100.
A continuació, l’aplicació va demanant números i va responent si el nombre a endevinar és més gran o més petit que la introduït,
a més dels intents que et queden (tens 10 intents per encertar-lo).
El programa acaba quan s'encerta el número (a més et diu quants intents has necessitat per encertar-lo),
si s'arriba al límit d'intents, l’aplicació et mostra el número que havia generat."""



import random

numero = random.randint(1, 100)
intentos = 10
numuser = 0

while numuser != numero:
    numuser = int(input("Intenta adivinar el número (de 1 a 100): "))
    if numuser == numero:
        print("Bingo")

    else:
        print("no era ese ª ")
        intentos -= 1
        if intentos == 0:
            print("* ce muere *")
        else:
            print("te quedan", intentos, " intentos")
            if numuser > numero:
                print("És más pequeño")
            else:
                print("És más grande")