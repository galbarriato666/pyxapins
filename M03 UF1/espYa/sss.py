punctuationMarks = [",", ";", ":", "-", "?", "¿", "!", "¡", ".", "\"", "\'"]


def countPuntuactionMarks(text):
    count = 0
    for i in range(len(text)):
        if text[i] in punctuationMarks:
            count = count + 1
    return count


def positionPuntuactionMarks(text):
    positions = {}
    for i in range(len(text)):
        if text[i] in punctuationMarks:
            if text[i] in positions:
                savedPos = positions.get(text[i])
                newPos = str(savedPos) + ", " + str(i)
                positions[text[i]] = newPos
            else:
                positions[text[i]] = i
    return positions


def asciiConverter(text):
    convertedTextList = []
    for letter in text:
        convertedLetter = ord(letter)
        convertedTextList.append(convertedLetter)
    convertedText = " ".join(str(e) for e in convertedTextList)
    return convertedText


print(countPuntuactionMarks("Hola que tal! ¿Si?"))
print(positionPuntuactionMarks("¿Hola que tal! ¿Si??"))
print(asciiConverter("Hola que tal! ¿Si?"))