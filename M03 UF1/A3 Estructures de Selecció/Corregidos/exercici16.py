"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Implementa un programa que calculi l'import a pagar per un usuari a una empresa telefònica.
    La política de cobrament de la companyia telefònica és:
    - quan es realitza una trucada, l'import és en funció del temps de la trucada i 
    per trams de durada:
        - els primers cinc minuts costen 1 euro x minut
        - els següents tres minuts, 80 cèntims x minut
        - els següents dos minuts, 70 cèntims x minut
        - a partir del desè minut, 50 cèntims x minut

    - a l'import calculat per la durada de la trucada a més se'ls aplicarà un recàrrec de:
        - 3% quan és diumenge
        - Si és un altre dia, en torn de matí, 15%, i en torn de tarda, 10%.

    El programa demanarà per teclat la durada de la trucada en minuts sencers 
    (si l’usuari ha estat 3 minuts i mig, s’haurà d’entrar 4 minuts) 
    L'import a pagar per l'usuari es mostrarà a la pantalla.
"""
temps = int(input("Quan ha durat la trucada?:"))
es_diumenge = input("Ha sigut en diumenge? (S/N):")
if es_diumenge.upper() == "N":
    torn = input("Quin torn: Matí o Tarda? (M/T)?:")
if temps < 5:
    cost = temps * 100
else:
    if temps < 8:
        cost = (temps - 5) * 80 + 500
    else:
        if temps < 10:
            cost = (temps - 8) * 70 + 240 + 500
        else:
            cost = (temps - 10) * 50 + 140 + 240 + 500
if es_diumenge.upper() == "S":
    cost = cost + cost * 0.03
else:
    if torn.upper() == "M":
        cost = cost + cost * 0.15
    else:
        cost = cost + cost * 0.10

print("El cost de la trucada és: %.2f euros." % (cost / 100))
