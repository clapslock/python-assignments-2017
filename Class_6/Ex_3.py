
def removeSpacesAndSpecialChars(inputText):

    whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    answer = ''.join(filter(whitelist.__contains__, inputText))
    answer = answer.lower()
    return answer

def withKey(unencryptedMsg, key):

    unencryptedMsg = list(removeSpacesAndSpecialChars(unencryptedMsg))
    key = list(removeSpacesAndSpecialChars(key))
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    alphabetDictionary = dict()
    invAlphabetDictionary = dict()
    intValuesKey = list()
    encryptedMsg = ""

    # creates a dictionary where 'a' = 1, 'b' = 2, ... , 'z' = 26
    for i in range (0, len(alphabet)):
        alphabetDictionary[alphabet[i]] = i + 1

    for i in range(0, len(alphabet)):

        invAlphabetDictionary[i+1] = alphabet[i]

    # converts chars in key to their int values (using alphabetDictionary)
    for character in key:
        intValuesKey.append(alphabetDictionary[character])

    i = 1
    j = 0
    for character in unencryptedMsg:
        singleKeyValue = intValuesKey[j % 3]
        charIntVal = alphabetDictionary[character] + singleKeyValue

        if charIntVal > 26:
            charIntVal = charIntVal % 26
            if charIntVal == 0:
                charIntVal += 1

        #print(invAlphabetDictionary[charIntVal], charIntVal)

        encryptedMsg += invAlphabetDictionary[charIntVal]

        i += 1
        j += 1

    return encryptedMsg
key = "zyf"
test = withKey("It's alive!", key)
print(test)

def decryptWithKey(encryptedMsg, key):

    encryptedMsg = list(removeSpacesAndSpecialChars(encryptedMsg))
    key = list(removeSpacesAndSpecialChars(key))
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    alphabetDictionary = dict()
    invAlphabetDictionary = dict()
    intValuesKey = list()
    unencryptedMssg = ""

    # creates a dictionary where 'a' = 1, 'b' = 2, ... , 'z' = 26
    for i in range (0, len(alphabet)):
        alphabetDictionary[alphabet[i]] = i + 1

    for i in range(0, len(alphabet)):

        invAlphabetDictionary[i+1] = alphabet[i]

    # converts chars in key to their int values (using alphabetDictionary)
    for character in key:
        intValuesKey.append(alphabetDictionary[character])

    i = 1
    j = 0
    for character in encryptedMsg:
        singleKeyValue = intValuesKey[j % 3]
        charIntVal = alphabetDictionary[character] - singleKeyValue

        if charIntVal < 1:
            charIntVal = 26 + charIntVal
            if charIntVal == 0:
                charIntVal = 1

        #print(invAlphabetDictionary[charIntVal], charIntVal)

        unencryptedMssg += invAlphabetDictionary[charIntVal]

        i += 1
        j += 1

    return unencryptedMssg

print(decryptWithKey(test, key))