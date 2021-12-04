"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

#A number is even if it is perfectly divisible by 2.
# When the number is divided by 2, we use the remainder operator % to compute the remainder.
# If the remainder is not zero, the number is odd.

num = float(input("Introduzca num "))

if (num % 2) == 0:
    print("Hey, el número " + str(int(num)) + " es número par")
else:
    print("ERROR MADAFAKA: El número " +str(int(num)) + " es un puto impar, jodido ignorante")
