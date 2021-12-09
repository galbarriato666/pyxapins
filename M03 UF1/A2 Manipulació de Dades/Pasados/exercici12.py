"""Exercici 12
Implementa un programa que demani per teclat dos punts del pla i tot seguit calculi i mostri la distància entre ells.

Notes:

Un punt del pla es representa amb un parell de números. Per exemple, el punt A es representarà pels números x1 i y1, i el punt B pels números x2 i y2
La fórmula de la distància entre dos punts A i B és:

distància(A,B) = √( (x2 - x1)2 + (y2 - y1)2)"""

from math import sqrt


x1 = int(input("x1?"))
y1 = int(input("y1?"))
x2 = int(input("x2?"))
y2 = int(input("y2?"))

distancia = abs(sqrt(       pow((x2-x1),2)          ) + pow ((y2-y1),2))
print("La distancia entre estos dos puntos es " + str(distancia))

#l'arrel quadrada de dos potencies que s'estàn sumant entre si'
#sqrt es raiz cuadrada
#distancia =abs(distancia (abs es valor absoluto, esta seria la forma sencilla
#para ahorrar espacio se pone asi e
