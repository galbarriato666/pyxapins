punctuationMarks = [",", ";", ":", "-", "'", "?", "¿", "!", "¡", ".", "\"", "\'"]


def countPuntuactionMarks(text):
    count = 0
    for i in range(len(text)):
        if text[i] in punctuationMarks:
            count = count + 1
    return count


print(countPuntuactionMarks("Hola que tal!... ¿Si?"))