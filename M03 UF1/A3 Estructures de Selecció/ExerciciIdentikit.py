"""
Emmanuel Manzanilla García
27/10/2021
ASIXc1b M03 UF1

Un grup d'investigadors ens ha demanat un programa per generar retrats robots.

L'usuari ha d'introduir el tipus de cabells, ulls, nas i boca i s'imprimeix per pantalla un dibuix de com és el sospitós.

Els cabells poden ser arrissats @@@@@, llisos VVVVV o pentinats XXXXX

Els ulls poden ser aclucats .-.-., rodons .o-o. o estrellats .*-*.

El nas pot ser aixafat ..0.., arromangat ..C.. o agilenc ..V..

La boca pot ser normal .===. , bigoti  .∼∼∼.  o dents-sortides  .www.

Input
arrissats
rodons
axafat
normal

Output
@@@@@
.o-o.
..0..
.===.
"""
"""Definir Dades ---> SON CONSTANTS, VAN EN MAJUSCULES PERQUE SON DADES FIXES 
    Mostrar Opcions
    Demanar Dades
    Comprovar dades
    Mostrar cara 
    o 
    Mostrar error"""

CABELL_ARRISSAT = "@@@@@"
CABELL_LLIS = "VVVVV"
CABELL_PENTINAT = "XXXXX"

ULLS_ACLUCATS = ".-.-."
ULLS_RODONS = ".o-o."
ULLS_ESTRELLATS = ".*-*."

NAS_AIXAFAT = "..0.."
NAS_ARROMANGAT = "..C.."
NAS_AGILENC = "..V.."

BOCA_NORMAL = "==="
BIGOTI = "∼∼∼"
DENTS_SORTIDES = ".www."

print("Bienvenido a Indentikit Gener8r, estas son tus opciones: ")
print("\n")
print("*******TIPUS DE CABELL********")
print("ARRISSAT")
print("LLIS")
print("PENTINAT")
print("\n")
cabello = print(input("Entonces, qué pelo tiene el sospechoso? "))
print("\n")
print("*******TIPUS D'ULLS'********")
print("\n")
print("ULLS ACLUCATS")
print("ULLS RODONS")
print("ULL ESTRELLATS")
print("\n")
ojos = print(input("Y qué tipo de ojos tiene el sospechoso? "))
print("\n")
print("*******TIPUS DE NAPIA'********")
print("NAS AIXAFAT")
print("NAS ARROMANGAT")
print("NAS AGILENC")
print("\n")
nas = print(input("Y qué tipo de nariz tiene el sospechoso? "))
print("\n")
print("*******TIPUS DE BOCA********")
print("BOCA NORMAL")
print("BIGOTI")
print("DENTS SORTIDES")
print("\n")
boca = print(input("Y qué pelo tiene el sospechoso? "))
print("\n")

if cabello == "arrissat":
elif cabello == "pentinat":
elif cabello == "llis":
elif ojos == "aclucats"
elif ojos == "rodons"
elif ojos == "estrellats"
elif nas == "aixafat"
elif nas == "arromangat"
elif nas == "agilenc"
elif boca == "normal"
elif boca == "bigoti"
elif boca == "dents sortides"
else:
    print("CABELLO NO EXISTENTE")
