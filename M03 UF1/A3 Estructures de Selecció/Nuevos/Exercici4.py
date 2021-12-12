"""Exercici 4
Escriu un programa que demani dos nombres per teclat i mostri la seva divisió. El programa
ha de comprovar si el segon nombre és igual a zero. Si ho és en lloc de realitzar i mostrar el
resultat de la divisió ha de mostrar un missatge d'error per pantalla indicant que la divisió no
es pot realitzar, ja que el segon nombre és zero."""

n1 = float(input("n1 "))
n2 = float(input("n2 "))

if n2 == 0:
    print("no és pot executar")
else:
    print(n1 / n2)

