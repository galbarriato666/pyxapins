maxLinea = int(input("Tria la mida de la piràmide: "))
espai=maxLinea


for linea in range(1, maxLinea, 2):
    print(" "*espai,"#"*linea)
    espai = espai -1

