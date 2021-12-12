"""Exercici 9
Realitza un programa que demani tres nombres per teclat i a continuació els mostri ordenats
de major a menor."""

n1 = int(input("n1 "))
n2 = int(input("n2 "))
n3 = int(input("n3 "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(n1,n2,n3)
    else:
        print(n1,n3,n2)
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(n2,n1,n3)
    else:
        print(n2,n3,n1)
if n3 >= n1 and n3 >= n2:  #en la ultima condicion, meto un mayorqueigual y listo. 
    if n1 > n2:
        print(n3,n1,n2)
    else:
        print(n3,n2,n1)