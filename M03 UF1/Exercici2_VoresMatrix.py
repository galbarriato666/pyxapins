"""
Emmanuel Manzanilla García
1r ASIXcB - A5 + Pp3 : Exercici2
01/02/2022

"""

matrix = 0
f0 = 0
c0 = 1

while f0 != c0:
    f0 = int(input("\n Nºde fileres, per favore: \n"))
    c0 = int(input("\n Nºde columnes, per favore: \n"))
    if c0 != f0:
        print("El nº de columnes ha de ser el mateix que el de fileres. Comença de 9! ")
    else:
        matrix = c0

for filera in range(matrix):
    for columna in range(matrix):
        if columna == 0 or columna == matrix - 1 or filera == matrix - 1 or filera == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()
print("\nEnd of program")
