"""
    Javier Amaya Boira / José Luis Álvarez Casas
    20/09/2021
    ASIXc
    Descripció:
    Realitza un programa que demani a l'usuari graus Fahrenheit i posteriorment els mostri com graus Celsius.

    La fórmula per a la conversió és:
    C = (F-32)*5/9

"""
fahrenheit = float(input("Entra la temperatura en ºF:"))
celcius = (fahrenheit - 32) * 5 / 9
print("La temperatura és", celcius, "ºC")
