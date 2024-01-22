from art import logo
def add(n1, n2):
    #This function adds two numbers
    return n1 + n2

def subtract(n1, n2):
    #This function subtracts two numbers
    return n1 - n2

def multiply(n1, n2):
    #This function multiplies two numbers
    return n1 * n2

def divide(n1, n2):
    #This function divides two numbers
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2

def calculator():
    #This function calls the operations and does the calculations
    print(logo)
    n1 = float(input("What is the first number? "))

    should_continue = True
    while should_continue:
        pick_operation = input("Pick an operation: +, -, *, or / ")
        n2 = float(input("What is the second number? "))

        if pick_operation == "+":
            answer = add(n1, n2)
        elif pick_operation == "-":
            answer = subtract(n1, n2)
        elif pick_operation == "*":
            answer = multiply(n1, n2)
        elif pick_operation == "/":
            answer = divide(n1, n2)

        print(f"{n1} {pick_operation} {n2} = {answer}")

        if input(f"Do you want to continue calculating with {answer}? Type 'y' to continue calculating, or type 'n' to start a new calculation: ") == 'y':
            n1 = answer
        else:
            should_continue = False

calculator()
