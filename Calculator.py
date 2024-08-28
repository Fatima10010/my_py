# a simple Calculation
def plus(a,b):
    return a+b

def mines(a,b):
    return a-b

def multi(a,b):
    return a*b

def division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "not possible to be divided!"

def poww(a,b):
    return a**b

while True:
    print("if you want to exit,Enter out!")
    try:
        a = int(input("Number one is="))
        b = int(input("Number two is="))
    except ValueError :
        print("Enter numbers! Try again")
        a = int(input("Number one is="))
        b = int(input("Number two is="))
    print(50*"*")
    x = input("ENTER opration: ")
    if x == "out":
        print("off")
        break
    elif x == "+":
        print("%s + %s = %s"%(a,b,plus(a,b)))
        print(50*"*")
    elif x == "-":
        print("%s - %s = %s"%(a,b,mines(a,b)))
        print(50*"*")
    elif x == "*":
        print("%s * %s = %s"%(a,b,multi(a,b)))
        print(50*"*")
    elif x == "/":
        print("%s / %s = %s"%(a,b,division(a,b)))
        print(50*"*")
    elif x == "**":
        print("%s ** %s = %s"%(a,b,poww(a,b)))
        print(50*"*")
    else:
        print("Unvalid!")
        print(50*"*")
