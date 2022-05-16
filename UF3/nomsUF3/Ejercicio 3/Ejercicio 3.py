'''
Miquel Regué Barrera
17/05/2022
ASIXc M03 UF2 A1 Disseny Descendent

Realizar un programa que a partir del archivo, "ocells.txt" cree otro
"ocells_2.txt". el contenido de cada fichero debe ser:

Foto 1

Foto 2
'''

ruta_entrada = "./ocells.txt"
ruta_salida = "./ocells_2.txt"

def LeeryEscribirUnArchivo(input, output):
    """
    Lee un archivo y lo copia en otro añadiendo contenido
    :param input: Ruta de entrada del archivo
    :param output: Ruta de salida del archivo
    """
    contador = 0
    try:
        with open(input, "rt") as archivo:
            with open(output, "wt") as archivo_escrito:
                for lineas in archivo:
                    for caracteres in lineas:
                        if caracteres == "6":
                            contador += 1
                        if contador == 2:
                                archivo_escrito.write("*")
                                contador += 1
                        elif caracteres == "3":
                            archivo_escrito.write("-")
                        else:
                            archivo_escrito.write(caracteres)



    except UnicodeError or OSError as mensaje:
        print(mensaje)


LeeryEscribirUnArchivo(ruta_entrada, ruta_salida)
