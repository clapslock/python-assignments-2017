
def removeSpacesAndSpecialChars(inputText):

    whitelist = set('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ')

    answer = ''.join(filter(whitelist.__contains__, inputText))
    answer = answer.lower()
    return answer

def zKluczem(tekst, klucz):

    tekst = list(removeSpacesAndSpecialChars(tekst))
    klucz = list(removeSpacesAndSpecialChars(klucz))
    alphabet = list("abcdefghijklmnopqrstuvwxy")
    alpHabetDictionary = dict()
    encryptedMessage = ""

    for i in range (0, len(alphabet)) :
        alpHabetDictionary[alphabet[i]] = i + 1

    kluczIntValuesList = []

    for i in range(0, len(klucz)):
        singleElementValue = alpHabetDictionary[klucz[i]]
        kluczIntValuesList.append(singleElementValue)

    for characterIndex in range(1, len(tekst) + 1):

        character = ord(tekst[characterIndex - 1])  #numeral value of

        if characterIndex % 3 == 0:
            character = character + kluczIntValuesList[2]
            encryptedMessage += chr(character)
        elif characterIndex % 2 == 0:
            character = character + kluczIntValuesList[1]
            encryptedMessage += chr(character)
        else:
            character = character + kluczIntValuesList[0]
            encryptedMessage += chr(character)
    return encryptedMessage

test = zKluczem("Hello", "zzz")
print(test)


