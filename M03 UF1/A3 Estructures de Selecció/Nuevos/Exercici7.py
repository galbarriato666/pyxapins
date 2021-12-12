"""Exercici 7_/home/sjo/home/sjo/home/sjo/home/sjo
Crea un programa que donats dos nombres entrats per teclat, la base i l'exponent, calculi la
potència i la mostri a la pantalla. El programa ha de controlar el següent:
* L'exponent és positiu, només cal calcular la potència amb l'operador corresponent de
Python
* L'exponent és 0, el resultat és 1, sigui quina sigui la base.
* L'exponent és negatiu, el resultat s'obté calculant primer la potència P amb l'exponent
passat a nombre positiu i calculant després 1 / P.
Nota: En Àlgebra i en Combinatòria, generalment el valor de 0
0 és considerat com 1,
mentre que en anàlisi matemàtica l'expressió és de vegades deixada indefinida. En el nostre
cas considerarem que val 1."""

n1 = int(input("n1 "))
n2 = int(input("n2 "))

if n2 > 0:
    print(n1 ** n2)
elif n2 == 0:
    print(1)
elif n2 < 0:
    print( 1 / (n1 ** (n2 * -1)))