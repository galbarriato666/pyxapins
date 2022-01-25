"""

Demanar el nom de 3 Players
Demanar el resultat de la partida de cada player [1..10]
mostrar els players en ordre alfabetic
Mostrar els players en ordre de punctuació amb la seva puntuació al costat



"""
MAXP = 3

players = []
scores = []

for jugador in range(MAXP):
    players.append(input("Nom? ")) #append para añadir a la lista vacia, todos los inputs que haga en los bucles MAXP

for punts in range(MAXP):
    scores.append(int(input("Scores? ")))

print("El resultat es ")
for jugador, puntuacio in zip(players,scores):
    print(jugador + " " + str(puntuacio))





