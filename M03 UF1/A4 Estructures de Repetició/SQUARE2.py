


mida = int(input("mida? "))
for fila in range(mida):
    for columna in range(mida):
        if fila == 0 or fila == mida-1 or columna == 0 or columna == mida-1:
            print("o  ", end="")
        else:
            print("   ", end="")
    print()
