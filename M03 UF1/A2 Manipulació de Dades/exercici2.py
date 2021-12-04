"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Exercici 2
Donada la base i altura d'un rectangle, escriure el programa que calcula i mostra el seu perímetre i àrea.
"""
"""base = int(input("base? "))
altura = int(input("altura? "))
area = base * altura

print("Area: " +str(area))"""

#hay que ponerle int a los inputs, hay que especificar muy bien que tipos de inputs se espera
#asi puede area calcularse. Despues al final tambien hay que pulir strings porque no puede
#concaternar el texto de Area + area, que es un integer. Hay que ponerlo en cadena con str.)

#round para definir decimales

#ejercicios debajo de redondear y de float

altura = float(input("introduce altura "))
base = float(input("introduce la base "))

print("altura "+str(altura))
print("base "+str(base))
area = base * altura
print("Area: "+str(round(area,2)))
