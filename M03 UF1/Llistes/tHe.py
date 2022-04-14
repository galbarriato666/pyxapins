'''
Emmanuel Manzanilla García
01 / 02 /2022
ASIXc 1B M03 UF1 A5 - A5 + Pp3

Fer un programa per demanar el número de files i columnes, d'una matriu.
Comprovar que la matriu sigui quadra, és a dir
que tingui les mateixes fileres que columnes.
I que sigui un número senar de fileres i columnes.
Omplir la matriu amb 0's tret de la primera i última columna i la filera central, que s'han d'omplir amb 1's.
Mostrar la matriu resultant per pantalla. El resultat ha de dibuixar una H amb els 1's dins de la matriu de 0's
'''

matrix = 0
f0 = 0
c0 = 1

while f0 != c0:
    f0 = int(input("\n Nºde fileres, per favore: \n"))
    if f0 % 2 == 0:
        print("Les mides introduides han de ser senars!")
    else:
        c0 = int(input("\n Nº de columnes, per favore: \n"))
        if c0 != f0:
            print("Les mides introduides han de ser del mateix valor! Comença de 9")
        else:
            matrix = c0
    for fila in range(matrix):
        for columna in range(matrix):
            if columna == 0 or columna == matrix - 1 or fila == matrix // 2:
                print(1, end="")
            else:
                print(0, end="")
        print()
print("\nEnd of program")