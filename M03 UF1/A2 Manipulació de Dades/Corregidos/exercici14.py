"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Donat un nombre de dues xifres, escriu el programa que permet mostrar el nombre de manera "invertida".
    Per exemple, si l'usuari introdueix 14, el programa hauria de mostrar 41.
"""

num = int(input("Entra un número de dues xifres:"))
decenes = num // 10
unitats = num % 10
print("Número inverit:", str(unitats) + str(decenes))
