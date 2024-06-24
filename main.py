from calculator.add import add
from calculator.subtract import subtract
from calculator.multiply import multiply
from calculator.divide import divide
from calculator.multiply_with_self import multiply_with_self


def main():
    print("Calculator App  ")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError as e:
        print(e)
        main()

    r = 1
    f = 2
    c = 3
    d = 4
    w = 5

    print("CHOOSE AN OPERATION: 1")
    print("1. Add 2")
    print("2. Subtract 3")
    print("3. Multiply 4")
    print("4. Divide 5")
    print("5. Multiply with self 6")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        print(f"The result of addition is: {add(a, b)}")
    elif choice == '2':
        print(f"The result of subtraction is: {subtract(a, b)}")
    elif choice == '3':
        print(f"The result of multiplication is: {multiply(a, b)}")
    elif choice == '4':
        try:
            print(f"The result of division is: {divide(a, b)}")
        except ValueError as e:
            print(e)
    elif choice == '5':
        print(f"multiplication with self is: {multiply_with_self(a)}")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
