
def anyToDecimal():
    isInputDecimal = input("Is the number you're trying to convert in decimal numeral system? (y/n)\n")
    if isInputDecimal == "y":
        decimalToAny(int(decimal))

def decimalToAny(decimal):
    while True:

        base = int(input("Enter a desirable numeral system: (n-based)\n"))

        list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        answer = ""
        while decimal != 0 :
            answer  += list[int(decimal) % int(base)]
            decimal /= base

        answer = str(answer)
        print("Your result: ", answer[::-1])
        doAgain = input("Wanna do antoher? (y/n)\n")
        if doAgain == "y":
            continue
        else:
            break

decimalToAny()