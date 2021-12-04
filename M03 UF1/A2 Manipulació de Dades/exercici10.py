"""
Exercici 10
En un institut la nota de l'assignatura de Programació es calcula de la següent manera:

     • 55% de la mitjana de tres qualificacions parcials.
     • 30% de la nota d’una prova final.
     • 15% de la nota d’un treball final.

Implementa un programa que calculi la nota final a partir dels valors entrats per teclat corresponents a les qualificacions parcials i notes de la prova i treball finals.
"""
Qualificacio_Parcial_1 = float(input("Qualificació Parcial 1? "))
Qualificacio_Parcial_2 = float(input("Qualificació Parcial 2? "))
Qualificacio_Parcial_3 = float(input("Qualificació Parcial 3? "))
Prova_Final = float(input("Nota de prova final? "))
Treball_Final = float(input("Nota Treball Final? "))

MitjanaParcials = (Qualificacio_Parcial_1 + Qualificacio_Parcial_2 + Qualificacio_Parcial_3) / 3

CalculParcials = (MitjanaParcials * 55) / 100
CalculProvaFinal = (Prova_Final * 30) / 100
CalculTreballFinal = (Treball_Final * 15) / 100

CalculDefinitiu = CalculParcials + CalculProvaFinal + CalculTreballFinal

print("La teva nota final de Programació es = " + str(round(CalculDefinitiu,2)))