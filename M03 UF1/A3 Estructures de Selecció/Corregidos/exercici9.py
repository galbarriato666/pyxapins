"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani tres nombres per teclat i a continuació els mostri 
    ordenats de major a menor.
"""
num1 = int(input("Entra el primer nombre:"))
num2 = int(input("Entra el segon nombre:"))
num3 = int(input("Entra el tercer nombre:"))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
if num3 >= num1 and num3 >= num2:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
