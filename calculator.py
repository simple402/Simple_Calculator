# Simple Calculator

def calculator():
    x = float(input("Give a number: "))

    o = input("Give me an operator: ")

    y = float(input("Give me another number: "))
    
    if o == "+":
        print("Result: ", float(x + y))
    elif o == "-":
        print("Result: ", float(x - y))
    elif o == "*":
        print("Result: ", float(x * y))
    elif o == "/":
        print("Result: ", float(x / y))
    elif o == "**" or o == "^":
        print("Result: ", float(x ** y))
    elif o == "%":
        print("Result: ", float(x % y))
    else:
        print("Unknown operator.")  
        
calculator()
