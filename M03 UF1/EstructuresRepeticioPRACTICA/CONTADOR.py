#Programa que demana 5 números i compta quants  són parells

culazo = 0 #a esto da igual el nombre que le pongamos, simplemente es una variable fija al principio

for i in range (1,6):
    num = int(input("Dime un número: "))
    if num % 2 == 0:
        culazo = culazo + 1
print("Has introducido", culazo," números pares")


