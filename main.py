def plus(a,b):
    return  print(a + b)

def minus(a,b):
    return  print(a - b)

def umoghit(a,b):
    return print(a * b)

def delit(a,b):
    return  print(a / b)


a = int(input("Enter your 1 number:\n"))
b = int(input("Enter your 2 number:\n"))
c = input("Enter your operation:\n")

if c == "+":
    plus(a,b)

if c == "-":
    minus(a,b)

if c == "*":
    umoghit(a,b)

if c == "/":
    delit(a, b)
