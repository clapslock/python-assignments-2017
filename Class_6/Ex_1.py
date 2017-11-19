
def removeSpacesAndSpecialChars(inputText):

    whitelist = set('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ')

    answer = ''.join(filter(whitelist.__contains__, inputText))
    answer = answer.lower()
    return answer

def caesar(inputText, constant):

    inputText = removeSpacesAndSpecialChars(inputText)
    encryptedInputText = ""

    for character in inputText:
        encryptedInputText += chr(ord(character) + constant)

    return encryptedInputText

def deCaesar (encryptedText, constant):
    decryptedInputText = ""

    for character in encryptedText:
        decryptedInputText += chr(ord(character) - constant)

    return decryptedInputText



test = "Hello* Worls ^% sup"
encryptedTest = caesar(test, 1)

print(caesar(test, 1))

print(deCaesar(encryptedTest, 1))




    #metoda replace. join
