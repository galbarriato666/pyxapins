"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Escriu el programa que calcula i mostra en pantalla
la suma, resta, divisió i multiplicació de dos nombres entrats per l'usuari.
"""
numero1 = int(input("numero 1? "))
numero2 = int(input("numero 2? "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacio = numero1 * numero2
divisio = numero1 / numero2
#divisioentera = numero1 // numero2
#divisioresto = numero1 % numero2

print("Suma = " +str(suma))
print("Resta = " +str(resta))
print("Multiplicació = " +str(multiplicacio))
print("Divisió = " +str(divisio))

#print("Divisio = " + str(divisio)