"""
    Javier Amaya Boira / José Luis Álvarez Casas
    27/09/2021
    ASIXc
    Descripció:
    Escriu un programa que demani a l'usuari per teclat dos nombres, 'nota' i 'edat', i un caràcter per 
    indicar el gènere. 
    Al programa caldrà implementar la següent lògica:
    - Si la nota és igual o major que 5 i l'edat és més gran o igual a 18 i el gènere és 'F', 
    llavors es mostrarà el missatge ‘Acceptada’
    - Si en canvi es compleix el mateix, però amb gènere igual a 'M', llavors es mostrarà 
    el missatge 'Possible'.
    - En qualsevol altre cas (és a dir, no es compleixen ni les condicions del primer punt 
    ni les del segon) s'ha de mostrar el missatge 'No Acceptada'.
"""

nota = int(input("Introdueix la nota:"))
edat = int(input("Introdueix l'edat:"))
sexe = input("Introdueix el sexe (F/M):")
if nota >= 5 and edat >= 18:
    if sexe.upper() == "F":
        print("Acceptada")
    else:
        if sexe.upper() == "M":
            print("Possible")
        else:
            print("No Acceptada")
else:
    print("No Acceptada")
