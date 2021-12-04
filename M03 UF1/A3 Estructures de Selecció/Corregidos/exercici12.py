"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Implementa un programa que donat un any entrat per teclat digui si és de traspàs. 
    La regla per determinar-ho és:
    - Un any és de traspàs si és un nombre divisible per 4, sense ser divisible per 100, 
    llevat que sent divisible per 100 també sigui divisible per 400.

    Per exemple, l'any 2000 va ser de traspàs, ja que tot i ser divisible per 100 també ho era per 400 
    (òbviament complia la primera condició, ser divisible per 4) En canvi l'any 2100 no serà de traspàs, 
    ja que és divisible per 100 però no per 400.
"""

year = int(input("Entra l'any:"))
if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
    print("És any de traspàs.")
else:
    print("No és any de traspàs.")
