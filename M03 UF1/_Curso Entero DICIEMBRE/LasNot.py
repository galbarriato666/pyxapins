
aprovats = []
suspesos = []

for alumne in range(1,12):
    print("Nota alumne "+str(alumne)+":")
    nota = input("") #preguntame 11 veces del 1 al 11 las notas. Guardalo en variable notas
    if int(nota) >= 5: #si la nota es menor o igual que 5, guardamelo en aprovats [nota,nota,nota,nota...]
        aprovats.append(nota)
    else: #sino guardamelo en suspesos  [nota,nota,nota,nota...]
        suspesos.append(nota)

print(f"APROVATS {aprovats} TOTAL = {len(aprovats)}") #len me da la cantidad de elementos dentro de
print(f"SUSPESOS {suspesos} TOTAL = {len(suspesos)}")