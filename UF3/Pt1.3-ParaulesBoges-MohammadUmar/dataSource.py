"""
Umar Mohammad Riaz & Emmanuel Manzanilla
04/05/2022
ASIXc 1B

Gets the data from different sources
"""
import os
from errorsHandler import log, personalizedException


def isUTF8(data):   # Checks the encoding
    try:
        with open(data, "r+", encoding="UTF-8", errors="strict") as txt: #l'atribut strict fa de error handler
            content = txt.read()
    except UnicodeDecodeError:
        filename = os.path.split(data)[-1]
        log(f"Encoding Error at file {filename}")
        return False
    else:
        return True

def getDataFromKeyboard():  # Esta funcion recoge el texto por teclado.
    dades = input()
    return dades

def getFilesFromFolder(inputFolder):    # Crea una lista con los archivos del directorio
    try:
        textDir = []
        if os.path.isdir(inputFolder) and os.path.exists(inputFolder):
            directory = os.listdir(inputFolder)
            for file in directory:
                filepath = os.path.join(inputFolder, file)
                if file.endswith(".txt") and isUTF8(filepath) == True:
                    textDir.append(filepath)
        else:
            log(f"\"{inputFolder}\" does not exist or it's not an input directory")
        return textDir
    except Exception as e:
        log(personalizedException(e))


def getDataFromFile(file):   # Gets Data from files
    text = []
    try:
        with open(file, "r+", encoding="UTF-8", errors="strict") as inp:
            content = inp.readlines()
            text.append(content)
    except Exception as i:
        log(personalizedException(i))
    return text





def writeOutput(result, files):     # Writes the output dir/file
    try:
        if not os.path.exists("./sortida"):
            os.mkdir("sortida")
        for filenum in range(len(files)):
            filename = os.path.split(files[filenum])[-1]
            filename = filename.replace(".txt", "Boges.txt")
            outputFile = os.path.join(".", "sortida", filename)
            with open(outputFile, "a", encoding="UTF-8", errors="strict") as out:
                for line in result[filenum]:
                    out.write(line + "\n")
    except Exception as e:
        log(personalizedException(e))