"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Implementa un programa que determini el guany obtingut per una associació de vinicultors 
    donat el preu inicial d'un quilo de raïm en cèntims i el nombre de quilos venuts. 
    Per això el programa ha de seguir les regles següents:

    - Els raïms es classifiquen sota dos conceptes, el tipus (A o B), i la grandària 
    (grandària  1 o grandària 2)
    - En cada venda de raïm, aquestes són sempre d'un sol tipus i grandària
    - Si la venda és de raïms de tipus A, se li carreguen 20 cèntims al preu inicial quan és 
    de grandària 1. En canvi si és de mida 2, es carregaran 30 cèntims al preu inicial.
    - Si el raïm venut és de tipus B, es rebaixe el preu inicial en 30 cèntims quan el raïm 
    és de tamany 1, i en 50 cèntims quan és de mida 2.

    Com és costum, el preu inicial de l'quilo de raïm, el nombre de quilos venuts, el tipus i la 
    grandària del raïm venut seran entrats per teclat i el benefici o guany es mostrarà per pantalla.
"""

preu_inicial = float(input("Introdueix el preu inicial per kilos del raïm en cèntims:"))
kilos = int(input("Introdueix quants kilos has venut:"))
tipus = input("Introdueix el tipus de raïm (A/B):")

if tipus.upper() != "A" and tipus.upper() != "B":
    print("Tipus incorrecte")
else:
    tamany = input("Introdueix el tamany del raïm (1/2):")
    if tamany != "1" and tamany != "2":
        print("Tamany incorrecte")
    else:
        if tipus.upper() == "A":
            if tamany == "1":
                preu_inicial = preu_inicial + 20
            else:
                preu_inicial = preu_inicial + 30
        else:
            if tamany == "1":
                preu_inicial = preu_inicial - 20
            else:
                preu_inicial = preu_inicial - 30
        preu_final = preu_inicial * kilos
        print("El guany és %.2f euros." % (preu_final/100))
