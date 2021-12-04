"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Escriure un programa que a partir del nombre de monedes que tenim dels següents tipus:
    2 €, 1 €, 50 cèntims, 20 cèntims i 10 cèntims, ens digui l'import corresponent en euros i cèntims.
"""

euro2 = int(input("Monedes de 2 euros:"))
euro1 = int(input("Monedes de 1 euro:"))
cent50 = int(input("Monedes de 50 cèntims:"))
cent20 = int(input("Monedes de 20 cèntims:"))
cent10 = int(input("Monedes de 10 cèntims:"))
# Calculem els euros: sumem les monedes de 2 euros i d'un euro
total_euros = euro2 * 2 + euro1
# Calculem els cèntims (monedes de 50c * 50 + monedes de 30c * 30 + monedes de 20c * 20 + monedes de 10c * 10
total_centims = cent50 * 50 + cent20 * 20 + cent10 * 10
#  Convertim els cèntims a euros (divisió sencera entre 100)
total_euros = total_euros + total_centims // 100
# I ens quedem amb els cèntims "sobrants" (mòdul de la divisó sencera entre 100)
total_centims = total_centims % 100
print("Import total: " , total_euros," euros i", total_centims, " cèntims.")
