"""Descarregar els fitxers pictures.zip i deixar-los al directori  "pictures" del "working directory" de la nostra aplicació.

Llegir tots els fitxers  *.in

i crear el fitxer de sortida,

amb el mateix nom acabat en "Closed" *Closed.out amb el mateix contingut.

# Però caldrà, haver canviat prèviament, els ulls del drac que al fitxer d'entrada estan oberts 0   0 , i al de sortida hauran d'estar tancats - -"""

#HAY QUE USAR LAS FUNCIONES DEL SISTEMA IMPORT OS PARA RENOMBRAR Y USAR RUTAS

#usar join para juntar las barras y los directorios no peten IMPORTANTE DE EXAMEN
""" print(os.path.join(".","pictures")) """
import os

dir = os.listdir(pictures/)

def proceder():
    with open('*.in', mode ='rt', encoding ='utf-8') as read:
        with open('*.in', "wt") as write:











f = open(nombre, mode ='rt', encoding ='utf-8')
# f.close()
print(f.read())



