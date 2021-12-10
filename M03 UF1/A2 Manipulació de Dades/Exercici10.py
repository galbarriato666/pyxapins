"""Exercici 10
En un institut la nota de l'assignatura de Programació es calcula de la següent manera:
• 55% de la mitjana de tres qualificacions parcials.
• 30% de la nota d’una prova final.
• 15% de la nota d’un treball final.
Implementa un programa que calculi la nota final a partir dels valors entrats per teclat
corresponents a les qualificacions parcials i notes de la prova i treball finals."""

Parci1 = float(input("Nota 1? "))
Parci2 = float(input("Nota 2? "))
Parci3 = float(input("Nota 3? "))
provfi = float(input("Provfi? "))
trebfi = float(input("Trebfi? "))

o = ((Parci1 + Parci2 + Parci3) /3) * .55
f = provfi * .3
s = trebfi * .15

i = o+f+s

print(round(i,2))
