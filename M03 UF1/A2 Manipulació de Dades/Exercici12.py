""" 
Exercici 12
Implementa un programa que demani per teclat dos punts del pla i tot seguit calculi i mostri
la distància entre ells.
Notes:
● Un punt del pla es representa amb un parell de números. Per exemple, el punt A es
representarà pels números x1 i y1, i el punt B pels números x2 i y2
● La fórmula de la distància entre dos punts A i B és:
distància(A,B) = √( (x2 - x1)2 + (y2 - y1)
2
)
"""

x1 = float(input("x1 "))
y1 = float(input("y1 "))
x2 = float(input("x2 "))
y2 = float(input("y2 "))

print("La distancia de un punto a otro es", (((x2-x1) **2) + ((y2-y1) **2)  ** 0.5))


