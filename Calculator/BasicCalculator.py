while True:
    print("1-Sum")
    print("2-Subtract")
    print("3-Multiplication")
    print("4-Division")
    print("0-Exit")
    op = int(input("Enter the option: "))

    match op:
        case 1:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            print(number1, " + ", number2, " = ", number1 + number2)
        case 2:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            print(number1, " - ", number2, " = ", number1 - number2)
        case 3:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            print(number1, " X ", number2, " = ", number1 * number2)
        case 4:
            number1 = int(input("Enter the first number: "))
            number2 = int(input("Enter the second number: "))
            if number2 == 0:
                print("Not include 0 (zero)")
                number1 = int(input("Enter the first number: "))
                number2 = int(input("Enter the second number: "))
                print(number1," / ",number2," = ",number1 / number2)
            else:
                print(number1," / ",number2," = ",number1 / number2)
        case _:
            print("Option not exist")