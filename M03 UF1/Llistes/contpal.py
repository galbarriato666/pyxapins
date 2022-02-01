'''Emmanuel Manzanilla García
01 / 02 /2022
ASIXc 1B M03 UF1 A5 - A5 + Pp3

Fer un programa per crear un vector de mida 15.
Omple'l pel teclat amb paraules. Mostra tot el seu contingut.
Copiar a un vector de mida 2, la paraula més llarga i la més curta.

Mostra aquest vector per pantalla.
Calcular també la llargada mitjana de les paraules introduïdes i mostrar-la per pantalla'''

vect1 = 5
vect2 = []
sum = 0

for i in range(vect1, 0, -1):
    vect2.append(str(input(f"{i}.Introduzca palabra: ")))

print(vect2)

lista_medidas = [vect2[0], vect2[0]]

for palabras in vect2:
    tamaño_palabras = len(palabras)
    sum += tamaño_palabras
    if tamaño_palabras > len(lista_medidas[0]):
        lista_medidas[0] = palabras
    elif tamaño_palabras < len(lista_medidas[1]):
        lista_medidas[1] = palabras

print("Paraula + llarga", {lista_medidas})
print("Paraula + curta", {lista_medidas})
print(f'Mitjana llargada paraules introduides {round(sum / len(vect2), 2)}')

print("\n Fin del juego")