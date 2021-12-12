"""Exercici 16
Implementa un programa que calculi l'import a pagar per un usuari a una empresa
telefònica.
La política de cobrament de la companyia telefònica és:
- quan es realitza una trucada, l'import és en funció del temps de la trucada i per trams
de durada:
- els primers cinc minuts costen 1 euro x minut
- els següents tres minuts, 80 cèntims x minut
- els següents dos minuts, 70 cèntims x minut
- a partir del desè minut, 50 cèntims x minut
- a l'import calculat per la durada de la trucada a més se'ls aplicarà un recàrrec de
3% quan és diumenge
- Si és un altre dia, en torn de matí, 15%, i en torn de tarda, 10%.
El programa demanarà per teclat la durada de la trucada en minuts sencers (si l’usuari ha
estat 3 minuts i mig, s’haurà d’entrar 4 minuts) L'import a pagar per l'usuari es mostrarà a la
pantalla."""

mindur = int(input("min dur? "))
dia = input("Qué día de la semana? ")
torn = input("Torn (M/T)? ")

cents = 1 * 100

if mindur > 0 and mindur <= 5:
    durada = mindur * cents
    print("El importe a pagar es", durada)
elif mindur > 5 and mindur <= 8:
    durada = mindur * 80
    print("El importe a pagar es", durada)
elif mindur > 8 and mindur <= 10:
    durada = mindur * 70
    print("El importe a pagar es", durada)
elif mindur > 10:
    durada = mindur * 50 
    print("El importe a pagar es", durada)
if dia.lower() == "diumenge":
    durada = durada + (durada * 0.03 )
    print("El importe a pagar es", durada)
elif dia.lower() != "diumenge":
    if torn.lower() == "m":
        durada = durada + (durada * 0.15)
        print("El importe a pagar es", durada)
    elif torn.lower() == "t":
        durada = durada + (durada * 0.10)
        print("El importe a pagar es", durada)
else:
    print()