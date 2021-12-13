"""2.
Programa que implementi la funcionalitat del mètode replace. (sense fer servir el mètode)

És a dir un programa que demani una cadena de caràcters, un caràcter a modificar i un altre caràcter
de substitució.
El programa haurá de mostrar com a resultat la cadena amb tots els caràcters a modificar canviats
pel caràcter de substitució"""


usuario = str(input(""))

a = input("")
b = input("")

stringlista = []


for i in usuario: #para i que es lo que haya en usuario, metemelo en
    stringlista.append(i) #esta lista (i)

for x in stringlista: #otro bucle, para x de lo que haya en stringlista[], aplica:
    if x == a: #si lo que hay ahi (x) es igual a == tal,
        x = b #cambiamelo por b
    cadena = " ".join(x) #aqui hace una variable que sea un espacio en blanco + la x cambiada
    print(cadena, end="")