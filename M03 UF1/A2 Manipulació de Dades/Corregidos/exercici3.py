"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Donats els catets a i b d'un triangle rectangle, escriure el codi Python que calcula la seva hipotenusa.
    Recordar que la hipotenusa es calcula de la següent manera (Teorema de Pitàgores):

    c2 = a2 + b2 , on c és la hipotenusa. Per tant  c = √(a2 + b2)
"""

import math
catet1 = float(input("Entra el catet 1:"))
catet2 = float(input("Entra el catet 2:"))
hipotenusa = math.sqrt(catet1 ** 2 + catet2 ** 2)
print("La hipotenusa és",hipotenusa)
