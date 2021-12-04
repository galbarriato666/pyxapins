"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

edad = int(input("Qué edad tienes, majadero?: "))
sueldo = float(input("Ok, y cuánto cobras cabrón?: "))

if edad >= 16 and sueldo >= 1000:
    print("Ale guapete, a tributar ")
else:
    print("Enga monstruo, a seguir viviendo la vida a la bartola")