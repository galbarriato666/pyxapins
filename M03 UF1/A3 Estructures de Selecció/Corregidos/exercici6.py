"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani una cadena per teclat, que comprovi si està escrita en majúscules o no 
    i aleshores mostri un missatge en conseqüència.
"""
cad = input("Entra una cadena:")
if cad == cad.upper():
    print("La cadena està en majúscules")
else:
    print("La cadena no està en majúscules")
