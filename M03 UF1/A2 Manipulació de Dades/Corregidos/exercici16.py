"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Dos vehicles A i B viatgen a velocitats vA i vB respectivament, amb vB> vA. El vehicle B va a una distància D
    darrere del vehicle A.

    Es demana implementar un programa que demani les velocitats dels vehicles, expressades en km / h, i la distància
    entre ells (en km) Amb aquestes dades el programa ha de calcular i mostrar el temps en minuts en què el vehicle B
    arribarà a l’alçada del vehicle A.
"""

velocitatA = float(input("Entra la velocitat del cotxe A (km/h):"))
velocitatB = float(input("Entra la velocitat del cotxe B (km/h):"))
distancia = float(input("Entra la distància entre els dos cotxes (km):"))
temps = distancia / (velocitatB - velocitatA)
temps = temps * 60
print("El cotxe B arribarà a l'alçada del cotxe A en", temps, "minuts.")
