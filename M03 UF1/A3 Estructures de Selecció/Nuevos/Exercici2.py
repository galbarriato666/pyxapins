"""Exercici 2
Crea un programa que llegeixi un nombre per pantalla i mostri en pantalla un missatge que
digui si és positiu, negatiu o igual a zero."""

n1 = float(input("n1 "))

if n1 > 0:
    print("positivo")
elif n1 < 0:
    print("negativo")
else:
    print("és zero")
    
