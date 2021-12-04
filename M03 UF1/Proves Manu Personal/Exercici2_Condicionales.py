"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

contraseña = str(input("Introduzca su contraseña, jefe "))

confirmacion = "jamacuco16"

if confirmacion == contraseña.lower(): #aqui lo que hacemos es que el input lo convertimos forzosamente a minusculas para
#que coincida con la variable almacenada (confirmacion) (Ojito con el orden de la ecuacion)
    print("Adelante Jeff")

