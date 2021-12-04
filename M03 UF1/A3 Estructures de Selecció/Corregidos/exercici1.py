"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Escriu un programa que demani per teclat dos nombres i mostri un missatge que digui si el primer és més 
    gran que el segon o bé que no ho és.
"""
num1 = int(input("Entra el primer nombre:"))
num2 = int(input("Entra el segon nombre:"))
if num1 > num2:
    print("El primer nombre és mayor que el segon")
else:
    print("El primer nombre NO és mayor que el segon")
