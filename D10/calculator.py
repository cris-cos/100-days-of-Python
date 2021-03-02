#The rudimentary calculator

def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def times(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_keys = {
    "+": plus,
    "-": minus,
    "*": times,
    "/": divide,
    }

def calculator_f():
    n1 = float(input("What's the first number? "))
    for symbol in calculator_keys:
        print(symbol)
    should_continue = True
    
    while should_continue:    
        operation = input("Pick an operation to perform: ")
        n2 = float(input("What's the second number? "))
        calculator = calculator_keys[operation]
        answer = calculator(n1, n2)
        print(f"{n1} {operation} {n2} = {answer}")
        if input("Type 'y' to continue calculating from this answer or 'n' to restart the calculator: \n") == "y":
            n1 = answer
        else:
            should_continue = False
            calculator_f()

calculator_f()
    