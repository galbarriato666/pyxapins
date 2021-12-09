"""Exercici 13

Escriu un programa que llegeixi un nombre i tot seguit calculi i mostri l'arrel quadrada i cúbica d'aquest número.
Desafortunadament, Python3 no té cap funció predefinida que calculi l'arrel cúbica, però sí que pots utilitzar l’operador que “fa l’operació inversa”

"""
import math
numerox = float(input("Introdueixi nº "))


calculquadrat = math.sqrt(numerox)
calculcubic = numerox ** (1 / 3)
print("L'arrel quadrada del nº introduit és " + str(calculquadrat))
print("L'arrel cubica del nº introduit és " + str(round(calculcubic,2)))