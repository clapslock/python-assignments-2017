
def removeSpacesAndSpecialChars(inputText):

    whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    answer = ''.join(filter(whitelist.__contains__, inputText))
    answer = answer.lower()
    return answer

def zKluczem(unencryptedMsg, key):

    unencryptedMsg = list(removeSpacesAndSpecialChars(unencryptedMsg))
    key = list(removeSpacesAndSpecialChars(key))
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    alphabetDictionary = dict()
    invAlphabetDictionary = dict()
    encryptedMsg = ""

    # creates a dictionary where 'a' = 1, 'b' = 2, ... , 'z' = 26
    for i in range (0, len(alphabet)):
        alphabetDictionary[alphabet[i]] = i + 1

    for i in range(0, len(alphabet)):
        for letter in alphabet:
            invAlphabetDictionary[i+1] = letter

    intValuesKey = list()

    # converts chars in key to their int values (using alphabetDictionary)
    for character in key:
        intValuesKey.append(alphabetDictionary[character])

    for characterIndex in range(1, len(unencryptedMsg) + 1):

        character = alphabetDictionary[unencryptedMsg[characterIndex-1]]  #numeral value of
        encryptedCharacter = 0

        if characterIndex % 3 == 0:
            encryptedCharacter = (character + intValuesKey[2])
            encryptedMsg += invAlphabetDictionary[encryptedCharacter]
        elif characterIndex % 2 == 0:
            encryptedCharacter = (character + intValuesKey[1])
            encryptedMsg += invAlphabetDictionary[encryptedCharacter]
        else:
            encryptedCharacter = (character + intValuesKey[0])
            encryptedMsg += invAlphabetDictionary[encryptedCharacter]

    return encryptedMsg

def charCheck(a):
    return a % 26
test = zKluczem("aaa", "aaa")
print(test)


