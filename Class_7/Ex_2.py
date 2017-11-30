
# problem cięcia pręta:

INT_MIN = -32767

def cutRod(priceList, rodLength):
    val = [0 for x in range(rodLength + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, rodLength + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, priceList[j] + val[i - j - 1])
        val[i] = max_val

    return val[rodLength]

arr = [1, 5, 8, 9, 10, 16, 17, 20, 24, 26]
size = 5
print("Maximum Obtainable Value is " + str(cutRod(arr, 4)))

