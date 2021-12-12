	
ElMesGran
Tots els programes resolen el mateix problema: troben el número major i l'imprimeixen. 

Exemple 1 
Com identificar el major dels dos números? 

"""

Source: Python Institute

"""

#lee dos números

numero1 = int (input("Ingresa el primer número:"))

numero2 = int (input("Ingresa el segundo número:"))



#elegir el número más grande

if numero1> numero2:

   nmasGrande = numero1

else:

   nmasGrande = numero2



#imprimir el resultado

print("El número más grande es:", nmasGrande)

Exemple 2
Python té una característica interessant, mira el codi a continuació 

"""

Com identificar el major dels dos números?

Source: Python Institute

"""

#lee dos números

numero1 = int (input("Ingresa el primer número:"))

numero2 = int (input("Ingresa el segundo número:"))



# elegir el número más grande

if numero1 > numero2: nmasGrande = numero1

else: nmasGrande = numero2



#imprimir el resultado

print("El número más grande es: ", nmasGrande)



Nota: si alguna de les branques de if-*elif-*else conté una sola instrucció, pots codificar-la de forma més completa (no és necessari que aparegui una línia amb sagnia després de la paraula clau), però només continua la línia després dels dos punts).



No obstant això, aquest estil pot ser enganyós, i no l'usarem en els nostres programes futurs, però definitivament val la pena saber si vols llegir i entendre els programes d'una altra persona. 

Exemple 3
Trobem el major de tres números. 

Suposem que el primer valor és el més gran. Després verifiquem aquesta hipòtesi amb els dos valors restants.

Observa el següent codi: 

"""

Com identificar el major del TRES números.

Source: Python Institute

"""

#lee tres números

numero1 = int (input("Ingresa el primer número:"))

numero2 = int (input("Ingresa el segundo número:"))

numero3 = int (input("Ingresa el tercer número:"))



#asumimos temporalmente que el primer número

#es el más grande

#lo verificaremos pronto

nmasGrande = numero1



#comprobamos si el segundo número es más grande que el mayor número actual

#y actualiza el número más grande si es necesario

if numero2 > nmasGrande:

   nmasGrande = numero2



#comprobamos si el tercer número es más grande que el mayor número actual

#y actualiza el número más grande si es necesario

if numero3 > nmasGrande:

   nmasGrande = numero3



#imprimir el resultado

print("El número más grande es:", nmasGrande)

Aquest mètode és significativament més simple que tractar de trobar el número més gran comparant tots els parells de números possibles (és a dir, el primer amb el segon, el segon amb el tercer i el tercer amb el primer). Intenta reconstruir el codi per tu mateix. 

Exemple 4 - funció max()
Trobar el número més gran,  fent servir la  funció incorporada de Python anomenada max(). 

# lee tres números

numero1 = int(input("Ingresa el primer número:"))

numero2 = int(input("Ingresa el segundo número:"))

numero3 = int(input("Ingresa el tercer número:"))



# verifica cuál de los números es el mayor

# y pásalo a la variable de mayor número



numeroMayor = max(numero1,numero2,numero3)



# imprimir el resultado

print("El número más grande es:", numeroMayor)