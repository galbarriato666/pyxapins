titulo = "Cuánto te gusta el queso?"
print(titulo, "\n", "-" * len(titulo), "\n")

puntuacion = 0 

opcion = input("""Pregunta 1: Qué haces cuando ves una tabla de quesos? 
A: Salgo corriendo
B: Pruebo uno de los quesos, incluso varios
C: Me los zampo que tiliflipas 
""").upper()


if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 15
elif opcion == "C": 
    puntuacion = puntuacion + 30


opcion = input("""
Pregunta 2: ¿Cómo te gusta la hamburguezita? 
A: Sin queso
B: Con queso  
C: Con el pan hecho de queso, la carne hecha de queso y un puto montonazo de queso
""").upper()


if opcion == "A":
    puntuacion = puntuacion + 0
elif opcion == "B":
    puntuacion = puntuacion + 15
elif opcion == "C": 
    puntuacion = puntuacion + 30
else:
    print("A, mover el culo")


if puntuacion > 30: #Solo aplicara a mayor que 30 la siguiente accion
    print("BEWARE: A cheesefucker at sight")
elif puntuacion >= 15: #Cuando usamos un elif, ya no tendra en cuenta la condicion anterior. Acotamos. Solo
    #lo que sea mayor o igual que 15 pero no mayor que 30
    print("You may like some cheez")
else: #Todo lo demas AKA cualquier cosa por debajo de 15
    print("Damn you fucking hate cheese")


print(puntuacion)