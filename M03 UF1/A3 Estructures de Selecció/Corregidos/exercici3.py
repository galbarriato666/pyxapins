"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Implementa un programa que demani a l'usuari un nombre per pantalla i indiqui si és parell o senar.
"""
num = int(input("Entra el nombre:"))
if num % 2 == 0:
    print("És parell")
else:
    print("És senar")