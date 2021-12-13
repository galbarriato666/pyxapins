

for x in range(1,11):
    for y in range(1,11):
        if x == y or x+y == 11: #se pone el 2do valor del range
            print(" ",end="")
        else:
            print("0",end="")
    print("")