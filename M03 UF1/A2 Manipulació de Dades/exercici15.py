"""

Exercici 15
Escriu el programa que demani a l'usuari el valor de dues variables A i B, intercanviï els seus valors i finalment els mostri.

"""
variableA = input("Variable A ")
variableB = input("Variable B ")
print(variableA,variableB)
temp = variableB
variableB = variableA
variableA = temp
print(variableA,variableB)

#en la linea 12 asignamos a la variable a = temp. Pero esto no funciona al revés, es decir, en esa linea no asignamos ningun valor nuevo a temp

