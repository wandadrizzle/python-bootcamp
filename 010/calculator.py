import art, os

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
    "/": divide,

}

def operate(a, b, op):
    answer = 0

    function = operations[op]
    answer = function(a, b)
    # if op == "+":
    #     answer = add(a, b)
    # elif op == "-":
    #     answer =  a - b
    # elif op == "*":
    #     answer =  a * b
    # elif op == "/":
    #     answer = a / b
    # else:
    #     answer = "undefined"
    #     print("Wanda's calculator cannot recognise that operation.")
    
    return round(answer, 2)

def calculate_cont(a):
    op = input("Pick an operation: ")
    b = float(input("What's the next number? "))

    answer = operate(a, b, op)
    print(f"{a} {op} {b} = {answer}")

    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    if cont == "y":
        calculate_cont(answer)
    elif cont == 'n':
        os.system('cls')
        calculate()
    else:
        print("You have entered an invalid response, the Wanda's calculator app will be closed now.")
        exit()

def calculate():
    print(art.logo)
    a = float(input("What's the first number?: "))
    #print("+\n-\n*\n/")
    for k in operations:
        print(k)
    calculate_cont(a)
    

calculate()