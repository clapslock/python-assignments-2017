
# problem cięcia pręta:
# sprzedajmey pręty od 1m do 10m
# Napisz program który obliczy
# najbardziej optymalne cięcie pręta 
# przy określonym cenniku (największy zysk)

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces

INT_MIN = -32767

def cutRod(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]


# Driver program to test above functions
arr = [1, 5, 8, 10, 12, 17, 17, 20, 24, 30]
size = 5
print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

# This code is contributed by Bhavya Jain