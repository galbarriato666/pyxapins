"""
Emmanuel Manzanilla García
26/10/2021
ASIXc1b M03 UF1

Exercici 5
Realitza un programa que demani un nom d'usuari i una contrasenya.
Si l'usuari és "pepe" i la contrasenya "asdasd", el programa mostrarà el missatge "Has entrat a el sistema".
En cas contrari es mostrarà un missatge d'error (com per exemple, "Usuari / password incorrecte")
"""

usuari = input("Introdueixi usuari ")
contrasenya = input("Introdueixi contrasenya ")

if usuari == "pepe" and contrasenya == "adsads":
    print("HAS ENTRAT AL SISTEMA :D")
elif contrasenya != "asdasd":               #con el != hago una negación.
    print("contraseña incorrecta")
elif usuari != "pepe":
    print("usuario incorrecto")
else:
    print("usuario y password incorrecto")
