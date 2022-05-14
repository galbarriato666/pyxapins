Esto escribe archivos


def writeFile(value1, value2):
    # rutasalida = value1.replace('.txt','.dat')

    with open(value1, 'wt', encoding='UTF-8') as outputfile:
        outputfile.write(value2)  # si quisiera usar el .dat, utilizo la variable rutasalida en vez de value2.

Esto hace lo mismo pero añade a lo q ya está escrito "append"

with open("log/error.log", "a") as log:

