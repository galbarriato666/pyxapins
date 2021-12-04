"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Escriu el programa que demani a l'usuari el valor de dues variables A i B, intercanviï els seus valors i finalment
    els mostri.
"""
a = input("Entra el valor de la variable A:")
b = input("Entra el valor de la variable B:")
aux = a
a = b
b = aux
print("Nou valor de A:", a)
print("Nou valor de B:", b)
