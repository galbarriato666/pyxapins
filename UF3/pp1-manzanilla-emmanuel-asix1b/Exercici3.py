'''
Emmanuel Manzanilla García
17/05/2022

ASIXb M03 Fonaments de Gestió de Fitxers

Exercici 3

'''

inbound = "ocells.txt"  #ruta+fitxer d'entrada
outbound = "ocells_2.txt" #ruta+fitxer de sortida

def ReadWrite(input, output): #recorre un arxiu i genera un altre. input és el que entra, output el que surt.

    comptador = 0
    try:
        with open(input, "rt") as file:
            with open(output, "wt") as outputFile:
                for linies in file:
                    for char in linies:
                        if char == "6":
                            comptador += 1
                        if comptador == 1:
                            outputFile.write("*")
                            comptador += 1
                        elif char == "4":
                            comptador += 1
                            outputFile.write("X")
                        else:
                            outputFile.write(char)

    except UnicodeError or OSError as ErrorCode:
        print(ErrorCode)


ReadWrite(inbound, outbound)



