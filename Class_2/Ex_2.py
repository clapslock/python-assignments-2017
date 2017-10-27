
#binary to decimal

def binaryToDecimal():
    while True:
        binaryNumberToConvert = int(input("Please enter binary number to convert: "))
        i = 0
        decimalResult = int(i)
        binaryNumber = int(binaryNumberToConvert)

        while (binaryNumber != 0):
            reminder = int(binaryNumber % 10)
            binaryNumber /= 10
            decimalResult = decimalResult + (reminder * (2**i))
            i += 1
        print(binaryNumberToConvert, "is", int(decimalResult), "in decimal")
        userContinueInput = input("Do you want to continue? (y/n)")

        if userContinueInput == "y":
            continue
        else:
            break

binaryToDecimal()