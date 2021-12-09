"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Exercici 11
Realitza un programa que mostri la "distància" entre dos nombres entrats per teclat.

Nota: la "distància entre dos nombres" és el valor absolut de la seva diferència.

Per exemple: distància (5,3) = / 5 - 3 / = 2, distància (15,22) = / 15 - 22 / = 7

"""
import math
n1 = float(input("Introdueixi nº 1 "))
n2 = float(input("Introdueixi nº 2 "))

calcul = abs(n1 - n2)

print("El valor absoluto es: " + str(round(calcul,None)))