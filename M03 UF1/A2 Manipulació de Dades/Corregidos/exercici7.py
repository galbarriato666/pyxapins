"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Implementa un programa que llegeixi del teclat una quantitat de minuts i després mostri en pantalla a quantes hores
    i minuts correspon aquesta quantitat.

    Per exemple: 1350 minuts són 22 hores i 30 minuts.
"""

minuts = int(input("Entra la quantitat de minuts:"))
res_hores = minuts // 60
res_min = minuts % 60
print(res_hores, "hores i", res_min, "minuts.")
