"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani un nom d'usuari i una contrasenya. Si l'usuari és "pepe" i la contrasenya "asdasd", el     programa mostrarà el missatge "Has entrat a el sistema". En cas contrari es mostrarà un missatge d'error (com per
    exemple, "Usuari / password incorrecte")
"""
usuari = input("Introdueix l'usuari:")
password = input("Introdueix el password:")
if usuari == "pepe" and password == "asdasd":
    print("Has entrat al sistema")
else:
    print("Usuari/password incorrecte")
