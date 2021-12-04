"""
Emmanuel Manzanilla García
07/11/2021
ASIXc1b M03 UF1

Ejercicio 1
Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiente con mostrar True o False):

Si los dos números son iguales
Si los dos números son diferentes
Si el primero es mayor que el segundo
Si el segundo es mayor o igual que el primero
"""

a = int(input("Introduzca nº 1 "))
b = int(input("Introduzca nº 2 "))

#Son iguales
print('Son iguales?')
print(a==b)                            #Aqui simplemente con hacer un print con el operador relacional igual a, ya me
#compara ambos valores y me muestra en pantalla (por eso es print) si es TRUE or FALSE. Sin condicional, este es más a pelo (manual)

#Si los dos número son diferentes
print('Son diferentes?')
print(a!=b)

#Si el primero es mayor que el segundo
print('El primero es mayor que el segundo')
print(a>b)

#Si el segundo es mayor o igual que el primero
print('El segundo es mayor o igual que el primero')
print(a<=b)
