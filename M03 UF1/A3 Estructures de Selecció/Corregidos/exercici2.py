"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Crea un programa que llegeixi un nombre per pantalla i mostri en pantalla un missatge que digui si és positiu,
    negatiu o igual a zero.
"""    
num = int(input("Entra el nombre:"))
if num == 0:
    print("És igual a 0")
else:
    if num > 0:
        print("És positiu")
    else:
        print("És negatiu")