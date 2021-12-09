"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Exercici 9
Escriu un programa que donat l'import d'una compra, apliqui a aquest import un descompte del 15% i el mostri a pantalla.
"""

importCompra =  float(input("Importa de la compra? "))

descompte = (importCompra * 15) / 100

print("El teu descompte es de " +str(descompte))