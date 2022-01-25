largest_number = -99999999
counter = 0

#Primera condición: while true: arrancamos directo, pido variable/numero: si es -1 aborta, sino sumale 1 al contador. Despues
#sigue con otro if que sustituirá a la variable largest number: Si el number introducido es > largest number -- entonces pon

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

#Segunda condición: Para que en el momento en el que se introduzca -1 y se rompa el ciclo, el contador debe ser al menos uno. Si lo es,
#ya entonces puede ser printado el largest number. Sino, print else:

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")