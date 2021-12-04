#Introduir 5 numeros i dir si s'ha introduït algun numero parell

indicador = False         #Cuando es FALSE,
for i in range (1,6):
    num = int(input("Introdueix un numero "))
    if num % 2 == 0:
        indicador = True               #Cuando es TRUE (metido dentro del if) salimos del for
if indicador:
    print("Has introducido un nº par ")
else:
    print("Has introducido un nº impar ")


