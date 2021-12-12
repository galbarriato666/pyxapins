"""Exercici 8_
Escriu un programa que demani a l'usuari per teclat dos nombres, 'nota' i 'edat', i un caràcter
per indicar el gènere. Al programa caldrà implementar la següent lògica:
- Si la nota és igual o major que 5 i l'edat és més gran o igual a 18 i el gènere és 'F',
llavors es mostrarà el missatge ‘Acceptada’
- Si en canvi es compleix el mateix, però amb gènere igual a 'M', llavors es mostrarà el
missatge 'Possible'.
- En qualsevol altre cas (és a dir, no es compleixen ni les condicions del primer punt ni
les del segon) s'ha de mostrar el missatge 'No Acceptada'."""

nota = int(input("nota "))
edat = int(input("edat "))
gen = str(input("gen "))

if nota >= 5:
    if edat >= 18:
        if gen == "F":
            print("Acceptada")
        elif gen == "M":
            print("Possible")
else:
    print("No acceptada")
