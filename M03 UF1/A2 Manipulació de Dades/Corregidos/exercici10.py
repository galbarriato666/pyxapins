"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    En un institut la nota de l'assignatura de Programació es calcula de la següent manera:

     • 55% de la mitjana de tres qualificacions parcials.
     • 30% de la nota d’una prova final.
     • 15% de la nota d’un treball final.

    Implementa un programa que calculi la nota final a partir dels valors entrats per teclat corresponents a les
    qualificacions parcials i notes de la prova i treball finals.
"""

parcial1 = float(input("Entra la nota del parcial 1:"))
parcial2 = float(input("Entra la nota del parcial 2:"))
parcial3 = float(input("Entra la nota del parcial 3:"))
prova = float(input("Entra la nota de la prova final:"))
treball = float(input("Entra la nota del treball final:"))
nota = ((parcial1 + parcial2 + parcial3) / 3) * 0.55 + prova * 0.3 + treball * 0.15
print("nota final:", nota)

