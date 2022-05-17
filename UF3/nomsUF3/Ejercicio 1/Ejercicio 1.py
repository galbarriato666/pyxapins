"""
EX1
"""
import os


def pathFromKeyboard():
    return input("RUTA: ")


def directoryExists(path):
    return os.path.exists(path)


def isDirectory(path):
    return os.path.isdir(path)


def outputDirExists():
    outputpath = os.path.join(".", "sortida")
    if not directoryExists(outputpath):
        os.mkdir(outputpath)
    return outputpath


def main():
    path = pathFromKeyboard()
    if not directoryExists(path):
        print(f"\nERROR: \"{path}\" no existeix!")
    elif not isDirectory(path):
        print(f"\nERROR: \"{path}\" no és un directori!")
    else:
        outputFilePath = os.path.join(outputDirExists(), "FitxersDelDirectori.txt")
        with open(outputFilePath, "w", encoding="utf-8") as out:
            filesInPath = os.listdir(path)
            for file in filesInPath:
                filepath = os.path.join(path, file)
                if os.path.isfile(filepath):
                    out.write(f"{os.path.abspath(filepath)}\n")


main()
