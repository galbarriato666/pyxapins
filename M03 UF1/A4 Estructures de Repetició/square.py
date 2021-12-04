"""

Emmanuel Manzanilla García
30/11/2021
ASIXc1b M03 UF1

Exercici 19

Square
Mostrar per pantalla un quadrat de mida N (la triarà l'usuari)

Cal "printar"  #  a les vores. És a dir, dalt, baix dreta i esquerra

Cal fer servir estructures de repetició, per fer servir la mínima quantitat possible de sentències print

input

5

output

#####

#   #

#   #

#   #

#####



BLANC = "   "
NEGRE = "███"

for i in range(1, 9):
    for j in range(1, 9):
        if (j + i) % 2 == 0:
            print(NEGRE, end="")
        else:
            print(BLANC, end="")
    print()"""




mida = int(input("Tria la mida de la piràmide: "))

for fila in range(mida,0,-1):
    for columna in range(mida,0,-1):
        if fila == 0 or fila == mida-1 or columna == 0 or columna == mida-1:
            print("# "*columna " ", end="")
        else:
            print("   ", end="")
    print()
