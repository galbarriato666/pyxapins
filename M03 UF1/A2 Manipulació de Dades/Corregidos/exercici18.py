"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Escriu un programa que donat el nom i els dos cognoms introduïts per un usuari, mostri les inicials corresponents
    en majúscules.
"""

nom = input("Entra el teu nom:")
cognom1 = input("Entra el teu primer cognom:")
cognom2 = input("Entra el teu segon cognom:")

inicial = nom[0]
inicial = inicial + cognom1[0]
inicial = inicial + cognom2[0]
# pasem les inicials a majúscules
inicial = inicial.upper()
print("Les inicials són:",inicial)
