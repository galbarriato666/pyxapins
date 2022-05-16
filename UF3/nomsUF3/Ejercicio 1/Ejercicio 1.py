'''
Miquel Regué Barrera
17/05/2022
ASIXc M03 UF2 A1 Disseny Descendent
Visualiza los nombres de ficheros, y nada más que ficheros, de un directorio.
La ruta al directorio (Absoluta o relativa) se solicitará por teclado.
Tiene que validar:
- Que la ruta existe.
- Que la ruta corresponde a un directorio.

Si alguna de estas condiciones es falsa, el programa acabará mostrando un error,
indicando que la condición ha fallado.

Los nombres de ficheros y su ruta se debe guardar en un fichero denominado
"FitxersDelDirectori.txt" en un directorio denominado "sortida".
Ejemplo de contenido:
/home/sjo/Escritorio/DADES/usuari/M03/f1.txt
/home/sjo/Escritorio/DADES/usuari/M03/f2.txt
/home/sjo/Escritorio/DADES/usuari/M03/README.txt

El directorio de "sortida" se debe crear si no existe
(Y no se debe intentar crear si existe).
'''

import os
import datetime

def pedirRuta():
    """
    Pide una ruta al usuario por teclado
    :return: Devuelve dicha ruta
    """
    ruta = str(input("Indique la ruta de archivos a validar: "))
    return ruta
def comprobarRuta(var_ruta):
    """
    Comprueba si una ruta dada existe
    :param var_ruta: Ruta de un directorio
    :return: True o False en función si existe o no.
    """
    if os.path.exists(var_ruta) == True:
        return True
    else:
        ERROR_01 = "El directorio no existe"
        print(ERROR_01)
        return False
def comprobarRutaEsDirectorio(var_ruta):
    """
    Comprueba si una ruta corresponde a un directorio o no.
    :param var_ruta: Ruta de un directorio
    :return: True o False en función si la ruta es un directorio o no.
    """
    if os.path.isdir(var_ruta) == True:
        return True
    else:
        ERROR_02 = "La ruta no se corresponde con ningún directorio"
        print(ERROR_02)
        return False
def WriteOutputFile(var_ruta):
    """
    Si no existe, crea una carpeta de salida, donde, si no existe, crea el archivo con el nombre
    de los documentos que contiene el directorio.
    :param var_ruta: Ruta de un directorio
    """
    cwd = os.getcwd()
    output = os.path.join(cwd, "sortida")
    archivo_ouput = os.path.join(output, "sortida.txt")
    list_dir = os.listdir(var_ruta)

    if comprobarRuta(output) == False:
        os.mkdir(output)
        if comprobarRuta(archivo_ouput) == False:

            with open(archivo_ouput, "wt", encoding='utf-8') as doc_exit:
                doc_exit.write(f'{datetime.datetime.now()}\n')
                for nombres_archivos in list_dir:
                    doc_exit.write(f'{nombres_archivos}\n')
        else:
            with open(archivo_ouput, "a", encoding='utf-8') as doc_exit:
                doc_exit.write(f'{datetime.datetime.now()}\n')
                for nombres_archivos in list_dir:
                    doc_exit.write(f'{nombres_archivos}\n')

    else:
        if comprobarRuta(archivo_ouput) == False:

            with open(archivo_ouput, "wt", encoding='utf-8') as doc_exit:
                doc_exit.write(f'{datetime.datetime.now()}\n')
                for nombres_archivos in list_dir:
                    doc_exit.write(f'{nombres_archivos}\n')
        else:
            with open(archivo_ouput, "a", encoding='utf-8') as doc_exit:
                doc_exit.write(f'{datetime.datetime.now()}\n')
                for nombres_archivos in list_dir:
                    doc_exit.write(f'{nombres_archivos}\n')
def main():
    """
    Activa todas las funciones, solicita la ruta al usuario y
    si no cumple los requisitos, no para de pedirla.
    """
    ruta = pedirRuta()
    while comprobarRuta(ruta) == False and comprobarRutaEsDirectorio(ruta) == False:
        ruta = pedirRuta()
        comprobarRuta(ruta)
        comprobarRutaEsDirectorio(ruta)
    WriteOutputFile(ruta)
    print("Archivo salida actualizado")

main()

