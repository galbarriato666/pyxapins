"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""
n1 = float(input("Introduzca el primer número "))
n2 = float(input("Introduzca el segundo número "))

if n1 != 0 and n2 != 0:
    print(int((n1/n2)))
else:
    print("No se puede dividir entre cero, campeón")