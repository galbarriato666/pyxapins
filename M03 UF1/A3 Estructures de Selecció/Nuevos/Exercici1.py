"""Exercici 1
Escriu un programa que demani per teclat dos nombres i mostri un missatge que digui si el
primer és més gran que el segon o bé que no ho és."""

n1 = int(input("n1 "))
n2 = int(input("n2 "))

if n1 > n2:
    print(n1,"és més gran que",n2)
else:
    print("nope", n1, "it isn't lol")
    