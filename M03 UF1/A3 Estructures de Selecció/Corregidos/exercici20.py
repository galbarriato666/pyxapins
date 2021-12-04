"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Una companyia de transport ens encarrega escriure un programa que permeti calcular 
    l'import a cobrar a un client per enviar un paquet. L'import variarà en funció de la 
    zona del món on es trobi el destinatari i del pes del paquet. Notar que no es podrà 
    enviar paquets de pes superior als 5 quilos.

    Les zones en què divideix el món aquesta companyia, amb els seus corresponents costos 
    d'enviament, són les següents:

    - Amèrica de Nord: 24 euros el quilo
    - Amèrica Central: 20 euros el quilo
    - Amèrica de Sud: 21 euros el quilo
    - Europa: 10 euros el quilo
    - Àsia: 18 euros el quilo

En cas que el paquet superi els 5 quilos, es mostrarà un missatge d'error.
"""
pes = int(input("¿Qué peso tiene el paquete (en kilos)?:"))
if pes > 0 and pes <= 5:
    print("1.- América del Nord")
    print("2.- América Central")
    print("3.- América del Sud")
    print("4.- Europa")
    print("5.- Asia")
    zona = int(input("A que zona es fa el repart (1-5):"))
    if zona == 1:
        print("Cost:", pes * 24, "euros.")
    elif zona == 2:
        print("Cost:", pes * 20, "euros.")
    elif zona == 3:
        print("Cost:", pes * 21, "euros.")
    elif zona == 4:
        print("Cost:", pes * 10, "euros.")
    elif zona == 5:
        print("Cost:", pes * 18, "euros.")
    else:
        print("Zona incorrecte.")
else:
    print("Pes incorrecte (no podem transportar paquets de més de 5Kg).")
