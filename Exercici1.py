
for i in range(medida, 0, -1):
    lista.append(str(input(f"{i}.Introduzca palabra: ")))

print(lista)

#Con la intención de no definir 0 como valor, definimos la posición de la lista,
#Como la lista esta vacia antes de este punto, defino las variables aquí, en vez de arriba del todo.
max_palabra = len(lista[0])
min_palabra = len(lista[0])

for palabras in lista:
    tamaño_palabras = len(palabras)
    suma += tamaño_palabras

    if tamaño_palabras > max_palabra:
        max_palabra = len(palabras)
    elif tamaño_palabras < min_palabra:
        min_palabra = len(palabras)

print(f'Palabra más larga mide {max_palabra} y más corta {min_palabra}')
print(f'Media del tamaño de las palabras {round(suma/len(lista),2)}')
