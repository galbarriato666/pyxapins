"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")


if (gender.lower == "m" and name.lower() > "m") or (gender.lower == "h" and name.lower < "n"):
    print("Tu grupo es A ")
else:
     print("Tu grupo es B ")
