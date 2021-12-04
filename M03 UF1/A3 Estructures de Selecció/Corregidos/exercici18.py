"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Escriu un programa que donat un dia de la setmana (com a número, de l'1 a l'7), escrigui
    el dia corresponent en lletres. 
    Si introduïm un nombre que no sigui de l'1 a l'7, el programa mostrarà un missatge d'error.
"""

dia = int(input("Entra un dia de la setmana (1-7):"))
if dia == 1:
    print("Dilluns")
elif dia == 2:
    print("Dimarts")
elif dia == 3:
    print("Dimecres")
elif dia == 4:
    print("Dijous")
elif dia == 5:
    print("Divendres")
elif dia == 6:
    print("Dissabte")
elif dia == 7:
    print("Diumenge")
else:
    print("Dia incorrecte")
