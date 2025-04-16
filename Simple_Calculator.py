# functions for operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return None


def power(a, b):
    return a ** b


def remainder(a, b):
    return a % b


def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:

            num1 = input("Enter first number: ")

            if num1.endswith('$'):
                return 0
            if num1.endswith('#'):
                return -1
            try:
                num1 = float(num1)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        while True:

            num2 = input("Enter second number: ")

            if num2.endswith('$'):
                return 0
            if num2.endswith('#'):
                return -1
            try:
                num2 = float(num2)
                break
            except ValueError:
                print("Not a valid number, please enter again")
                continue

        result = None
        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)

        if result is not None:
            print(f"{num1} {choice} {num2} = {result}")
        else:
            print(f"{num1} {choice} {num2} = None")

        return 0
    else:
        print("Unrecognized operation")
        return 0


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")


    choice = input("Enter choice(+,-,*,/,^,%,#,$): ").strip()

    if not choice:
        continue

    result = select_op(choice)
    if result == -1:
        print("Done. Terminating")
        break