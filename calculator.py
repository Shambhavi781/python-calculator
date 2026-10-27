import math

op = input("Enter operator (+, -, *, /,sqrt,cbrt,square,cube,%,power): ")
a = float(input("Enter first number: "))

if op in ["+","-","*","/","%","power"]:
    b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
    
elif op == "-":
    print("Result:", a - b)
    
elif op == "*":
    print("Result:", a * b)
    
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
        
elif op == "%":
    print("Result:",a % b )
 
elif op == "power":
    print("Result:",a**b)
        
elif op == "sqrt":
    if a>=0:
        print("Result:",math.sqrt(a))
    else:
        print("Cannot find sqrt for -ve numbers")        

elif op == "cbrt":
    if a >= 0:
        print("Cube root:", a ** (1 / 3))
    else:
        print("Cube root:", -(abs(a) ** (1 / 3)))
    
elif op == "Square":
    print("Result:",a**2) 
    
elif op == "Cube":
    print("Result:",a**3)
    
                  