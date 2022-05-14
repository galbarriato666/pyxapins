# Exercici 1
# Demanar la ruta d'un arxiu i un text que volem introduir en l'arxiu. //mismo input que output, solo modificar

# S’ha de canviar entre majúscules i minúscules, és a dir, si escric “Hola” ha de guardar a l’arxiu “hOLA”.

# S’ha d'utilitzar un mètode per a escriure en l'arxiu el text introduït

# i un altre per a llegir de l'arxiu

# i un altre per a mostrar el contingut de l’arxiu que tindrà les majúscules i minúscules intercanviades


def introDades():
    ruta = str(input('Introdueix ruta'))
    text = str(input('Intro text'))
    return ruta,text

#todo dentro de las funciones! Luego en el main se especifica el orden de ejecución de las funciones


def changeText(texti): #esta info ya la estoy asignando (llamando) desde main!
    changed = ""
    for letras in texti:
        if letras == letras.lower():
            letras = letras.upper()
        elif letras == letras.upper():
            letras = letras.lower()
        changed = changed + letras
    return changed

def writeFile(value1,value2):
    # rutasalida = value1.replace('.txt','.dat')

    with open(value1, 'wt', encoding='UTF-8') as outputfile:
        outputfile.write(value2) #si quisiera usar el .dat, utilizo la variable rutasalida en vez de value2.


def readFile(leer):
    with open(leer, 'rt', encoding='UTF-8') as reading:
        print(reading.readline())



def main(): #sin parametros, solo llama otras funciones

    rutexto = introDades()
    texto = changeText(rutexto[1]) #aqui es mas visible, recomendado
    # print(changeText(rutexto[1])) #visualizo
    writeFile(rutexto[0],texto) #le indico qué valores (variables ya definidas en el mismo main, quiero utilizar en esta función)
    readFile(rutexto[0])



main() #HAY QUE LLAMAR A MAIN BRO

#lo primero es verificar con if si los datos introducidos existan (exista ruta para que no duplique - depuración de errores)
