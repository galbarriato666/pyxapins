"""Mostrar per pantalla cap i cua si la llista de N valors introduïts
per l'usuari són cap i cua (llegits en ordre invers és la mateixa llista).

Input

4

10 5 5 10


Output

cap i cua"""
capicua = []
capicuarev = []

num = int(input("Introdueix sequencia nºs: "))

for i in range(num):
    capicua.append(input("Introdueix nº "))

capicuarev = capicua.reverse()

print(capicuarev)
