"""Exercici 14
Implementa un programa que determini el guany obtingut per una associació de vinicultors
donat el preu inicial d'un quilo de raïm en cèntims i el nombre de quilos venuts. Per això el
programa ha de seguir les regles següents:
- Els raïms es classifiquen sota dos conceptes, el tipus (A o B), i la grandària
(grandària 1 o grandària 2)
- En cada venda de raïm, aquestes són sempre d'un sol tipus i grandària
- Si la venda és de raïms de tipus A, se li carreguen 20 cèntims al preu inicial
quan és de grandària 1. En canvi si és de mida 2, es carregaran 30 cèntims
al preu inicial.
- Si el raïm venut és de tipus B, es rebaixe el preu inicial en 30 cèntims quan el
raïm és de mida 1, i en 50 cèntims quan és de mida 2.
Com és costum, el preu inicial del quilo de raïm, la quantitat de quilos venuts,
el tipus i la grandària del raïm venut seran entrats per teclat i el benefici o guany
es mostrarà per pantalla."""

preuini = float(input("Preu inicial? "))
tipus = input("Tipus de raïm? ")
 

if tipus.lower() != "a" and tipus.lower != "b":
    print("Opció incorrecta")
else:
    grn = int(input("Grandària raïm? "))

    if grn != 1 and grn != 2:
        print("Grn incorrecte!")
    else:
        qtykg = float(input("Quantitat kg venut? "))

        if tipus.lower() == "b" and grn == 1:
            preuini = preuini - 30
        elif tipus.lower() == "b" and grn == 2:
            preuini = preuini - 50
        elif tipus.lower() == "a" and grn == 1:
            preuini = preuini + 20
        elif tipus.lower() == "a" and grn == 2:
            preuini = preuini + 30
print("El benefici és", (preuini * qtykg) // 100, "euros") 