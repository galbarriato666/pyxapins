"""
Emmanuel Manzanilla García
17/11/2021
ASIXc1b M03 UF1

Exercici 1
1. Programa que demana a l'usuari la introducció de 10 nombres sencers i ha de mostrar,
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""

contZeros = 0
contNegatius = 0
contPositius = 0

for i in range(10):
    numero = int(input("Introduzca un número ")) #Se pide los datos despues del for range, asi lo pide diez veces:
    if numero == 0:
      contZeros = contZeros +1
    elif numero < 0:
      contNegatius = contNegatius +1
    else numero > 0:
      contPositius = contPositius +1

contZeros = print("Número de ceros = " +str(contZeros))
contNegatius = print("Números Negativos = " +str(contNegatius))
contPositius = print("Números Positivos = " +str(contPositius))

demanem dades
comprovació dades
processem
mostrem resultats
