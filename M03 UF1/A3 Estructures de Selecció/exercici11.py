"""
Emmanuel Manzanilla García
26/10/2021
ASIXc1b M03 UF1

Exercici 11

Escriu un programa que llegeixi per pantalla la longitud dels tres costats d'un triangle. El programa ha de ser capaç de determinar de quin tipus de triangle es tracta.

Tingueu en compte que:
Si es compleix el teorema de Pitàgores, llavors és triangle rectangle
Si només dos costats del triangle són iguals llavors aquest és isòsceles
Si els tres costats són iguals llavors és un equilàter
Si no es compleix cap de les condicions anteriors, és un triangle escalè.
"""

import math

LADO1 = float(input("Introduzca el lado 1 del triangulito "))
LADO2 = float(input("Introduzca el lado 2 del triangulito "))
LADO3 = float(input("Introduzca el lado 3 del triangulito "))

HIPOTENUSA = LADO3 = math.sqrt (pow(LADO1,2) + pow(LADO2,2))

if LADO1 == LADO2 and LADO2 == LADO3:
    print("TRIANGULO EQUILATERO")
elif LADO1 == LADO2 or LADO2 == LADO3 or LADO3 == LADO1:
    print("TRIANGULO ISÓSCELES")
    #COMPROVAR SI ÉS RECTANGLE PQ TAMBÉ POT SER-HO
if LADO1 == HIPOTENUSA or LADO2 == HIPOTENUSA or LADO3 == HIPOTENUSA:
        print("TRIANGULO RECTANGULO PITAGORAS")
else:
     print("TRIANGULO ESCALENO")
