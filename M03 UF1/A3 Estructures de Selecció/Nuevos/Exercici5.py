"""Realitza un programa que demani un nom d'usuari i una contrasenya. Si l'usuari és "pepe" i
la contrasenya "asdasd", el programa mostrarà el missatge "Has entrat a el sistema". En cas
contrari es mostrarà un missatge d'error (com per exemple, "Usuari / password incorrecte")"""

usr = input("User: ")
pwd = input("Pwd: ")

usr = usr.lower()
pwd = pwd.lower()

if usr == "pepe":
    if pwd == "asdasd":
        print("Has entrat al sistema")
else:
    print("usuari o password incorrecte")