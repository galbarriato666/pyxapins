"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Escriu un programa que llegeixi un nombre i tot seguit calculi i mostri l'arrel quadrada i cúbica d'aquest número.
    Desafortunadament, Python3 no té cap funció predefinida que calculi l'arrel cúbica, però sí que pots utilitzar
    l’operador que “fa l’operació inversa” …
"""

import math
num = int(input("Entra el número:"))
print("Arrel quadrada:",math.sqrt(num))
print("Arrel cúbica:",num ** (1 / 3))
