"""
Exercici 8
Un venedor percep cada mes un sou base més un 10% de l'import de cada venda realitzada al mes en concepte de comissió de vendes.

Realitza un programa que a partir d'un import de sou base i l'import de tres vendes, calculi i escriu en pantalla:

l'import percebut en concepte de comissió de vendes
l'import total percebut pel venedor (el salari)

Nota: els imports de salari base i de les tres vendes seran entrats per teclat.
"""
salariBase = float(input("Salari Base?"))
venda1 = float(input("Primera Venda? "))
venda2 = float(input("Segona Venda? "))
venda3 = float(input("Tercera Venda? "))

comissio = float((venda1+venda2+venda3) *0.1) #els parentesis son necessaris pq primer ha de fer les sumes per poder despres la multi

salariFinal = salariBase + comissio

print("\tBase %.2f \n\tComisión %.2f \n\tSalari %.2f" %(salariBase,comissio,salariFinal))


# \t es tabular para printar
# barra invertida + n \n es un salto de linea, lo usaremos para printar por linea los valores
#Se añade un porcentaje al final del parentesis para especificar los valores

#las variables si las repito con copia y pega, cogerá el ultimo valor secuencialmente
