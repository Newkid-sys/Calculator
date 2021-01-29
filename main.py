
from art import logo

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

functions = {'+': addition, '-':subtraction, '*':multiplication, '/':division}



def calculator():
    print(logo)
    n1 = float(input("Pick a number: "))
    for symbol in functions:
        print(symbol)
    should_continue = True
    while should_continue:
        function_symbol = input("What operation do you want to use? ")
        calculation_function = functions[function_symbol]
        n2 = float(input("Enter another number: "))
        answer = calculation_function(n1, n2)
        print(f"{n1} {function_symbol} {n2} = {answer}")
        start_again = input(f"Type 'y' to continue with {answer}, or 'n' to start new calculation: ").lower()
        n1 = answer
        if start_again == 'y':
            n1 = answer
        else:
            should_continue = False
            calculator()

calculator()


