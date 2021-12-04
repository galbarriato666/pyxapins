"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani per teclat el nombre obtingut en llançar un dau de sis cares 
    i tot seguit mostri el nombre en lletres corresponent a la cara oposada a el nombre introduït.
    Per exemple, si l’usuari entra un 5, aleshores el programa contestarà “dos”.

    Recordar que les cares oposades d'un dau de sis cares són: 1-6, 2-5 i 3-4.

    El programa ha de controlar que el nombre del dau introduït és major o igual que 1 
    i menor o igual que 6. Si no és així, el programa mostrarà el missatge: 
    "ERROR: nombre incorrecte.".
"""

nombre = int(input("Introdueix el nombre que ha sortit:"))
if nombre == 1:
    print("SIS")
elif nombre == 2:
    print("CINC")
elif nombre == 3:
    print("QUATRE")
elif nombre == 4:
    print("TRES")
elif nombre == 5:
    print("DOS")
elif nombre == 6:
    print("U")
else:
    print("Error: nombre incorrecte.")
