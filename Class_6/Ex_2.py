
def removeSpacesAndSpecialChars(inputText):

    whitelist = set('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ')

    answer = ''.join(filter(whitelist.__contains__, inputText))
    answer = answer.lower()
    return answer

def podstawieniowy(inputText, key):
    alphabet = list("abcdefghijklmnopqrstuvwxy")
    inputList = list(removeSpacesAndSpecialChars(inputText))
    keyList = list(key)
    keyDictionary = dict()
    encryptedMsg = ""

    for i in range (0, len(alphabet)) :
        keyDictionary[alphabet[i]] = keyList[i]

    for character in inputList:
        encryptedMsg += keyDictionary[character]

    return encryptedMsg

def dePodstawieniowy(encryptedInputText, key):
    encryptedInputText = list(encryptedInputText)
    key = list(key)
    alphabet = list("abcdefghijklmnopqrstuvwxy")
    invertedKeyDictionary = dict()
    decryptedMsg = ""

    for i in range(0, len(alphabet)): 
        invertedKeyDictionary[key[i]] = alphabet[i]

    for character in encryptedInputText:
        decryptedMsg += invertedKeyDictionary[character]

key = "bacdefghijklmnopqrstuvwxy"
message = "Hello" #return

encryptedMessage = podstawieniowy(message, key)

print(encryptedMessage)