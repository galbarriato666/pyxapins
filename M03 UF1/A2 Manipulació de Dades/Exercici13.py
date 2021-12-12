"""Exercici 13
Escriu un programa que llegeixi un nombre i tot seguit calculi i mostri l'arrel quadrada i
cúbica d'aquest número. Desafortunadament, Python3 no té cap funció predefinida que
calculi l'arrel cúbica, però sí que pots utilitzar l’operador que “fa l’operació inversa” …"""

n1 = int(input("n1 ")) #raiz cuadrada es elevar a 0.5 y cubica a 0.333

print("L'arrel cúbica és", round(n1 ** 0.333,2), "y la raiz cuadrada és", round(n1 ** 0.5,2) )