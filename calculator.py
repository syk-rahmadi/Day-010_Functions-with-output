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
    return n1 / n2

def calculator(n1, n2, pick_operation):
    #This function calls the operations and does the calculations
    if pick_operation == "+":
        answer = add(n1, n2)
    elif pick_operation == "-":
        answer = subtract(n1, n2)
    elif pick_operation == "*":
        answer = multiply(n1, n2)
    elif pick_operation == "/":
        if n2 == 0:
            return "Error: Division by zero"
        answer = divide(n1, n2)
    return answer

should_continue = True
while should_continue:
    n1 = int(input("What is the first number? "))
    n2 = int(input("What is the second number? "))
    pick_operation = input("Pick an operation: +, -, *, or / ")
    answer = calculator(n1,n2, pick_operation)
    print(f"{n1} {pick_operation} {n2} = {answer}")

    if input(f"Do you want to continue calculating with {answer}? Type 'y' to continue calculating, or type 'n' to start a new calculation: ") == 'y':
        n1 = answer
    else:
        continue_calculation = False
        calculator()



