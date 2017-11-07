
def calculator ():
    while True:
        choosenOperation = input('Please choose an operation \n -"+" for addition\n -"-" for substraction\n '
                              '-"*" for multiplication \n -"/" for division\n -"^" for exponentation\n\n')
        while True:
            if choosenOperation == "+":
                rhsOperand = float(input("Enter the first operand: "))
                lhsOperand = float(input("Enter the second operand: "))
                result = float(rhsOperand) + float(lhsOperand)
                print (lhsOperand, choosenOperation, rhsOperand, "=", result)
                break
            elif choosenOperation == "-":
                rhsOperand = float(input("Enter the first operand: "))
                lhsOperand = float(input("Enter the second operand: "))
                result = float(rhsOperand) - float(lhsOperand)
                print(lhsOperand, choosenOperation, rhsOperand, "=", result)
                break
            elif choosenOperation == "/":
                lhsOperand = float(input("Enter the first operand: "))
                rhsOperand = float(input("Enter the second operand: "))
                while True:
                    if float(rhsOperand) != 0:
                        result = float(lhsOperand) / float(rhsOperand)
                        print(lhsOperand, choosenOperation, rhsOperand, "=", result)
                        break
                    else:
                        print("Division by 0!\nPlease enter different rhsOperand")
                        rhsOperand = float(input("Enter the second operand: "))
                        continue
                break
            elif choosenOperation == "*":
                rhsOperand = float(input("Enter the first operand: "))
                lhsOperand = float(input("Enter the second operand: "))
                result = float(rhsOperand) * float(lhsOperand)
                print(lhsOperand, choosenOperation, rhsOperand, "=", result)
                break
            elif choosenOperation == "^":
                rhsOperand = float(input("Enter the base operand: "))
                lhsOperand = float(input("Enter the power: "))
                result = rhsOperand ** lhsOperand
                print(rhsOperand, choosenOperation, lhsOperand, "=", result)
                break
            else:
                print("Operation not found. Please try again.")
                break

        anotherOne = input("Do another one? (y/n): ")
        if anotherOne == "y":
            print("\n\n\n")
            continue
        else:
            break


calculator()