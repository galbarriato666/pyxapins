nota = float(input("Dime tu nota:"))

if nota >=1 and nota < 5:

    print("Suspenso")

elif nota >= 5 and nota <6:

    print("Suficiente")

elif nota <= 6 and nota <7:

    print("Bien")

elif  nota <= 8 and nota <9:

    print("Notable")

elif nota <=9 and nota <= 10: #Aqui es importante delimitarlo con AND puesto que sino con que se cumpla una de los condiciones, le podriamos clavar un catorce y dar sobresaliente

    print("Sobresaliente")

else:

    print("Nota incorrecta")

print("Programa terminado")
