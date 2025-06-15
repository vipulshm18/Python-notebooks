def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations  = {
    "+" : add,
    "_" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    should_accumulate =  True
    num1 = float(input("Number 1: "))

    while should_accumulate:
        user_operation = input("What operation do you want to perform?: ")
        num2 = float(input("Number 2: "))
        answer = operations[user_operation](num1, num2)
        print(f"{num1} {user_operation} {num2} = {answer}")
        choice = input(f"Y to continue with {answer}, N to restart: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
