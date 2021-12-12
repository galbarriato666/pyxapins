"""Exercici 18
Escriu un programa que donat el nom i els dos cognoms introduïts per un usuari, mostri les
inicials corresponents en majúscules"""

nom = input("How's yar neim? ")
cog = input("How's yar cog? ")
cg2 = input("Hows your cg2 ")

alemanianazi = nom[0] + cog[0] + cg2[0]

alemanianazi = alemanianazi.upper()

print("Las iniciales son: " + alemanianazi)