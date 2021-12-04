"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Donada la base i altura d'un rectangle, escriure el programa que calcula i mostra el seu perímetre i àrea.
"""

base=float(input("Entra la base:"))
altura=float(input("Entra l'altura:"))
perímetre = 2 * base + 2 * altura
area = base * altura
print("El perímetre és", perímetre, "i l'àrea és", area)
