"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Un ciclista triga T segons a recórrer el trajecte de la ciutat “A” a la ciutat “B”.
    El ciclista va partir de la ciutat “A” a les HH hores, MM minuts i SS segons.

    Escriu un programa que calculi l'hora d'arribada a la ciutat B. Els segons en què el ciclista tarda a realitzar
    el trajecte i l'hora, minuts i segons de partida es demanaran per teclat.
"""

horaPartida = int(input("Hora de partida:"))
minPartida = int(input("Minuts de partida:"))
segPartida = int(input("Segons de partida:"))
segonsViatge = int(input("Temps que ha trigat el ciclista en segons:"))
# Converteixo l'hora de partida a segons
seginicial = horaPartida * 3600 + minPartida * 60 + segPartida; #lo pasa todo a segundos y lo junta con el resto de segundos
# Li sumo els segons que ha trigat el ciclista
segtotal = seginicial + segonsViatge; #suma mas segundos
# Converteixo els segons totals a hora, minuts i segons
horaarribada = segtotal // 3600;
minarribada = (segtotal % 3600) // 60;
segarribada = (segtotal % 3600) % 60;
# Mostro l'hora d'arribada
print("Hora d'arribada")
print(horaarribada, ":", minarribada, ":", segarribada)
