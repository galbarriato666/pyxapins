"""Exercici 11
Realitza un programa que mostri la "distància" entre dos nombres entrats per teclat.
Nota: la "distància entre dos nombres" és el valor absolut de la seva diferència.
Per exemple: distància (5,3) = / 5 - 3 / = 2, distància (15,22) = / 15 - 22 / = 7"""

import math 
n1 = int(input("n1 "))
n2 = int(input("n2 "))

print("Distancia entre n1 y n2 es:", abs(n1-n2))
