#Introducir 5 números i sumar els nombres parells

suma = 0;

for i in range (1,6): #se pone 6 para que cuente hasta 5, a recordar
    num = int(input("Dime un número o te rajo, majo ")) #me lo pide 5 veces, va debajo del for
    if num % 2 == 0:
        suma = suma + num #aqui lo estoy sumando al número introducido, y al declarla otra vez la reemplazo con "="
                            #debajo del if, si se cumple la condicion del if, ejecuta la suma
print("La suma de los números pares es ", suma)

