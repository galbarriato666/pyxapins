"""3. Programa que pinta per pantalla una matriu de 8x8 (fileres x columnes) amb zeros a cada posició, a excepció dels
diagonals"""

"""cruz x

blanc = "1 "
negre = "0 "

num = int(input("Mida del quadrat? "))

for horizontal in range(num):
    for vertical in range(num):
        if horizontal == vertical or (horizontal + vertical == num-1):
            print(blanc, end="")

        else:
            print(negre, end="")
    print()"""

#cruz +

uno = "1 "
dos = "0 "

import math
num = int(input("Mida del quadrat? "))

for hor in range(num):
    for ver in range(num):
        if hor == round((num / 2), 0) or ver == round((num / 2), 0):
            print(uno, end="")

        else:
            print(dos, end="")
    print() #la putada es que solo queda centrado con los input impares xD

















