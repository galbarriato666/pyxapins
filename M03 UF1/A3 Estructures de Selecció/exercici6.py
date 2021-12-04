"""
Emmanuel Manzanilla García
26/10/2021
ASIXc1b M03 UF1

Exercici 6

Realitza un programa que demani una cadena per teclat, que comprovi si està escrita en majúscules o no i aleshores mostri un missatge en conseqüènc
"""

cadena = input("Introduzca cadena de texto ")

#if cadena == cadena.upper():  MAAAAL
if cadena.isupper(): #esto despues del if ya hace de igual, no hace falta ponerle el igual a la cadena, ya me hace la equivalencia y puedo pasar al print para que ejecute
    print("Està en majúscules")
else:
    print("No està en majúscules")
