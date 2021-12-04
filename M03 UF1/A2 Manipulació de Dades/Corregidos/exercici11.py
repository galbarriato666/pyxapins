"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Realitza un programa que mostri la "distància" entre dos nombres entrats per teclat.

    Nota: la "distància entre dos nombres" és el valor absolut de la seva diferència.

    Per exemple: distància (5,3) = / 5 - 3 / = 2, distància (15,22) = / 15 - 22 / = 7
"""

num1 = int(input("Entra el número 1:"))
num2 = int(input("Entra el número 2:"))
print("Distància:", abs(num1 - num2))
