"""1. Programa de càlcul de temperatures emmagatzemades dins d’una llista de nombres sencers (sense decimals).
Proveu el resultat usant les definicions següents d’array, una per a cada execució diferent:
//Primer proveu si funciona usant aquesta llista"""

gener = [1, 12, 4, -5, 7, 3, 2,
        9, -6, 7, 8, 2, 14, -7,
        5, 13, 12, 4, 6, -7, 1,
        12, 4, -2, 3, 5, 2, 7,
        -2, 8, -15]

febrer = [1, 20, 6, 7, 2, -70,5, 4,
         32, 1, -10, 6, 5, 13, 12,
         4, 6, -7, 3, -16, 8, 9, 6,
         -19,4, 9, -6, 2]

marzo = [ 5, 4, 32, 1, -10, 6,
        9, -6, 7, 8, 2, 14, -7,
        3, -16, 8, 4, 6, -2, 23,
        14, 4, -2, 3, 5, 2, 7,
        -2, 8, -22]

max_temp_gen = 1
min_temp_gen = 0

max_temp_feb = 1
min_temp_feb = 0

max_temp_mar = 1
min_temp_mar = 0

"""Cal definir els 3 primers mesos de l’any, i calcular:
Per a cada mes: temperatura màxima, mínima i mitjana
Per al 1r trimestre de l’any: temperatura màxima, mínima i mitjana"""

for temp in gener:
        if temp > max_temp_gen:
                max_temp_gen = temp
        if temp < min_temp_gen:
                min_temp_gen = temp

for temp in febrer:
        if temp > max_temp_feb:
                max_temp_feb = temp
        if temp < min_temp_feb:
                min_temp_feb = temp

for temp in marzo:
        if temp > max_temp_mar:
                max_temp_mar = temp
        if temp < min_temp_mar:
                min_temp_mar = temp


print("Màxima gener és", max_temp_gen,"i mínima",min_temp_gen)
print("Màxima febrer és", max_temp_feb,"i mínima",min_temp_feb)
print("Màxima març és", max_temp_mar,"i mínima",min_temp_mar)

mitja_gen = 0
mitja_feb = 0
mitja_mar = 0

for temp in gener:
    mitja_gen = mitja_gen + temp
    mitja_gen = mitja_gen / len(gener)
print("La temp mitja del gener és", round(mitja_gen, 2))

for temp in febrer:
    mitja_feb = mitja_feb + temp
    mitja_feb = mitja_feb / len(febrer)
print("La temp mitja del febrer és", round(mitja_feb, 2))

for temp in marzo:
    mitja_mar = mitja_mar + temp
    mitja_mar = mitja_mar / len(marzo)
print("La temp mitja del març és", round(mitja_mar, 2))












