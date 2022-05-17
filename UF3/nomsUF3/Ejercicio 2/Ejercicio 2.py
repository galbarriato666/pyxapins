'''
Emmanuel Manzanilla García
17/05/2022
ASIXb M03 UF2 A1 Disseny Descendent

Crea una copia del archivo "paraules.txt" añadiendo un número que indique
la cantidad de caractéres de cada una de las palabras del fichero.
El fichero resultado se denominará "paraulesQuantitat.txt"

El formato de cada linea debe ser: "cantidad + espacio + palabra"
ej.
7 Abporal
8 laborals
8 absorbat
9 absorbats
'''

inbound = "./paraules.txt"
outbound = "./paraulesQuantitat.txt"

def ReadWrite(input, output):
    """
    Lee un archivo y lo copia en otro añadiendo contenido
    :param input: Ruta de entrada del archivo
    :param output: Ruta de salida del archivo
    """
    wordlist = []
    try:
        with open(input, "rt") as file:
            for palabras in file:
                palabrasNoLinea =  palabras.strip("\n")
                wordlist.append(palabrasNoLinea)

            with open(output, "wt") as outboundFile:
                for i in range(len(wordlist)):
                    outboundFile.write(f'{len(wordlist[i])} {wordlist[i]} \n')
    except UnicodeError or OSError as ErrorCode:
        print(ErrorCode)

ReadWrite(inbound, outbound)
