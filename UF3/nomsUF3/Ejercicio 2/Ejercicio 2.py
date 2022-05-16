'''
Miquel Regué Barrera
17/05/2022
ASIXc M03 UF2 A1 Disseny Descendent

Crea una copia del archivo "paraules.txt" añadiendo un número que indique
la cantidad de caractéres de cada una de las palabras del fichero.
El fichero resultado se denominará "paraulesQuantat.txt"

El formato de cada linea debe ser: "cantidad + espacio + palabra"
ej.
7 Abporal
8 laborals
8 absorbat
9 absorbats
'''

ruta_entrada = "./paraules.txt"
ruta_salida = "./paraparaulesQuantat.txt"

def LeeryEscribirUnArchivo(input, output):
    """
    Lee un archivo y lo copia en otro añadiendo contenido
    :param input: Ruta de entrada del archivo
    :param output: Ruta de salida del archivo
    """
    lista_palabras = []
    try:
        with open(input, "rt") as archivo:
            for palabras in archivo:
                palabras_sin_salto =  palabras.strip("\n")
                lista_palabras.append(palabras_sin_salto)

            with open(output, "wt") as archivo_escrito:
                for i in range(len(lista_palabras)):
                    archivo_escrito.write(f'{len(lista_palabras[i])} {lista_palabras[i]} \n')
    except UnicodeError or OSError as mensaje:
        print(mensaje)


LeeryEscribirUnArchivo(ruta_entrada, ruta_salida)