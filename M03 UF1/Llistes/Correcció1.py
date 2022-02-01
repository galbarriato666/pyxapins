#Inicialitzar dades
gener = [1, 12, 4, -5, 7, 3, 2,
        9, -6, 7, 8, 2, 14, -7,
        5, 13, 12, 4, 6, -7, 1,
        12, 4, -2, 3, 5, 2, 7,
        -2, 8,-15]
febrer = [4, 8, -3, 20, 19, 3, 12,
          5, -7, 11, 3, 7, 1, -6,
          5, 13, 12, 24, 14, -7, 8,
          12, 5, -2, 0, 18, 8, 3,]
marc = [4, 8, -3, 20, 19, 3, 12,
        5, -7, 11, 3, 7, 1, -6,
        5, 13, 12, 4, 6, -7, 1,
        12, 4, -2, 3, 5, 2, 7,
        -4, 4,-10, 29]
calendari = [gener, febrer, marc]
tempMinimes = []
tempMaximes = []
tempMitjanes = [0,0,0]

#Calcular dades
mesActual = 0
for mes in calendari:
    tempMaximes.append(mes[0])
    tempMinimes.append(mes[0])
    tempMitjanes.append(0)
    mesOrdenat = sorted(mes,key=None,reverse=True)
    tempMaximes[mesActual] = mesOrdenat[-1]
    tempMinimes[mesActual] = mesOrdenat[0]
    tempAcumulada = 0
    for temp in mes:
        tempAcumulada = tempAcumulada + temp
    mesActual = mesActual + 1
    tempMitjanes[mesActual] = round(tempAcumulada / len(mes), 1)

#Calcular trimestre
tempMinimesTrimestre = sorted(tempMinimes,key=None,reverse=True)[0]
tempMaximesTrimestre = sorted(tempMaximes,key=None,reverse=True)[0]
tempMitjanaAcumulada = 0
for tempMitjana in tempMitjanes:
    tempMitjanaAcumulada = tempMitjanaAcumulada + tempMitjana
tempMitjanaTrimestre = tempMitjanaAcumulada / len(tempMitjanes)

#Mostrar dades
for temp in tempMaximes:
    print(f"Max del mes = {temp} ")
