
# Wczytujemy listę liczb i przepisujemy ją 
# usuwając liczby pierwsze powtarzające się 
# nieparzystą liczbę razy

def removePrimesFilter(userList):

    primes = primeNumbers(max(userList)) #list with all prime numbers
    numberOfOccurences = 0
    finalUserList = []

    for primeNumber in primes:
        if userList.count(primeNumber) % 2 != 0:
            userList = [x for x in userList if x != primeNumber]


    return userList


def primeNumbers(maxValue):


    primeNumbersList = [True] * (maxValue + 1)
    primeNumbersList[0] = primeNumbersList[1] = False
    j = 2

    while (j ** 2 <= maxValue):
        if (primeNumbersList[j] == True):

            for i in range(j * 2, maxValue + 1, j):

                primeNumbersList[i] = False
        j += 1
    primes = []
    for k in range(2, maxValue + 1):
        if primeNumbersList[k]:
            primes.append(k)
    return primes

testlist = [1, 2,  3, 13,  3, 4, 4, 5, 6, 7, 11, 11, 13, 13,  3] # return 1, 4, 4, 6, 11, 11,
fiteredTestList = removePrimesFilter(testlist)
print(fiteredTestList)