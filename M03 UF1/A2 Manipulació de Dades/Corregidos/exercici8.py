"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Un venedor percep cada mes un sou base més un 10% de l'import de cada venda realitzada al mes en concepte de
    comissió de vendes.

    Realitza un programa que a partir d'un import de sou base i l'import de tres vendes, calculi i escriu en pantalla:

    - l'import percebut en concepte de comissió de vendes
    - l'import total percebut pel venedor (el salari)

    Nota: els imports de salari base i de les tres vendes seran entrats per teclat.
"""

sou_base = float(input("Entra el sou base:"))
venda1 = float(input("Entra preu de la venda 1:"))
venda2 = float(input("Entra preu de la venda 2:"))
venda3 = float(input("Entra preu de la venda 3:"))
comissio = venda1 * 0.1 + venda2 * 0.1 + venda3 * 0.1
print("Comissió per vendes:", comissio)
print("sou total:", sou_base + comissio)
