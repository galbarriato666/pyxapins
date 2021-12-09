"""
Emmanuel Manzanilla García
05/10/2021
ASIXc1b M03 UF1

Realitza un programa que demani a l'usuari graus Fahrenheit i posteriorment els mostri com graus Celsius.

La fórmula per a la conversió és:

C = (F-32)*5/9
"""
fahrenheit = float(input("Fahrenheit?"))
centigrads = (fahrenheit-32)*5/9
print(str(fahrenheit) +" FHR8 son "+str(centigrads) + " centigrads")
#manera pepino de hacerlo:
""" print("%2f"""