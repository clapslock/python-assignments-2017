import time

def primeNumbers(maxValue):

    # Lista ktora bedzie zawierac wartosc True,
    # jeśli dany index jest liczbą pierwszą
    # oraz False jeśli nia nie jest
    primeNumbersList = [True] * (maxValue + 1)
    primeNumbersList[0] = primeNumbersList[1] = False
    j = 2

    while (j ** 2 <= maxValue):
        # odrzucamy elementy które po sprawdzeniu
        # na pewno nie są liczbami pierwszymi
        if (primeNumbersList[j] == True):

            for i in range(j * 2, maxValue + 1, j):

                primeNumbersList[i] = False
        j += 1

    # Przypisz wszystkie znalezione liczby pierwsze do nowej listy
    primes = []
    for k in range(2, maxValue + 1):
        if primeNumbersList[k]:
            primes.append(k)
    return primes

# Sprawdzenie czasu szukania liczb pierwszych w danym zakresie

for _ in range(0, 10):
    start = time.time()
    primes = primeNumbers(10000000)
    stop = time.time()
    print(stop - start)


