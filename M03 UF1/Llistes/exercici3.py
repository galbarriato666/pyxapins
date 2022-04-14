





"""
Por ejemplo, aquí está el programa que crea una tabla numérica
con dos filas y tres columnas,
y luego realiza algunas manipulaciones con ella:
"""
# llist a =[[1 ,2 ,3] ,[4 ,5 ,6] ,[7 ,8 ,9]]

matriz = []
for indice_fila in range(0, 5):
    fila = []
    for indice_col in range(0, 5):
        # Si estoy en alguna diagonal inicializo a 1
        if indice_fila == indice_col or indice_fila == 4 - indice_col:
            fila.append(1)
        # No estoy en diagonal, inicializo a 0
        else:
            fila.append(0)
    matriz.append(fila)
# Recorro para mostrar tabla
for fila in matriz:
    for elemento in fila:
        print(elemento, " ", end="")
    print()

