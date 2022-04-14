"""
Emmanuel Manzanilla García
1r ASIXcB - A5 + Pp3 - Exercici1
01/02/2022

"""
qty = 10
llista = []
suma = 0

for word in range(qty, 0, -1):
    llista.append(str(input(f"{word} paraula!: ")))

print(llista)

mides = [llista[0], llista[0]]

for paraules in (llista):
    tamanyP = len(paraules)
    suma += tamanyP
    if tamanyP > len(mides[0]):
        mides[0] = paraules
    elif tamanyP < len(mides[1]):
        mides[1] = paraules



print(f'Palabra más larga mide {max_palabra} y más corta {min_palabra}')
print(f'Media del tamaño de las palabras {round(suma/len(lista),2)}')

print("Paraula + llarga {mides}"f)
print("Paraula + curta", {mides})
print(f'Mitjana llargada paraules introduides {round(sum / len(llista), 2)}')
