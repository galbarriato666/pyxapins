'''
Emmanuel Manzanilla García
17/05/2022
ASIXb M03 UF2 A1 Disseny Descendent

Realizar un programa que a partir del archivo, "ocells.txt" cree otro
"ocells_2.txt". el contenido de cada fichero debe ser:

Foto 1

Foto 2
'''

inbound = "./ocells.txt"
outbound = "./ocells_2.txt"

def ReadWrite(input, output):
    """
    Lee un archivo y lo copia en otro añadiendo contenido
    :param input: Ruta de entrada del archivo
    :param output: Ruta de salida del archivo
    """
    comptador = 0
    try:
        with open(input, "rt") as file:
            with open(output, "wt") as outputFile:
                for linies in file:
                    for char in linies:
                        if char == "6":
                            comptador += 1
                        if comptador == 2:
                                outputFile.write("*")
                                comptador += 1
                        elif char == "3":
                            outputFile.write("-")
                        else:
                            outputFile.write(char)



    except UnicodeError or OSError as ErrorCode:
        print(ErrorCode)


CallReadWriteF(inbound, outbound)
