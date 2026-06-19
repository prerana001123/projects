import art
print(art.logo2)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# print(operations["*"](4,2))


def calculator():
    should_continue = True
    x = float(input("What is the first number?: "))
    while should_continue:

        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        z = float(input("What's the next number?: "))
        answer = operations[operations_symbol](x, z)
        print(f"{x} {operations_symbol} {z} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if choice == "y":
            x = answer

        else:
            should_continue = False
            print("\n" * 30)
            calculator()
calculator()