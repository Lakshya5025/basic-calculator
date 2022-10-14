print("Welcome to basic calculator.")
print("Which operation you want to perform:-")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
print("// for floor division or to get the quotient")
print("% for modular or to get the reminder of division")
print("** for 'n' rase to power 'm'")
operation=input("Enter which operation you want to perform = ")
num1=eval(input("Enter your first number = "))
num2=eval(input("Enter your second number = "))
if operation=="**":
    n1=eval(input("Enter the number = "))
    n2=eval(input("Enter the power = "))
    print(f"{n1} ** {n2} = {n1**n2}")
elif operation=="+":
    print(f"{num1} + {num2} = {num1+num2}")
elif operation=="-":
    print(f"{num1} - {num2} = {num1- num2}")
elif operation=="*":
    print(f"{num1} *{num2} = {num1*num2}")
elif operation=="/":
    print(f"{num1} / {num2} = {num1/num2}")
elif operation=="//":
    print(f"{num1} divide by {num2} quotient is {num1//num2}")
elif operation=="%":
    print(f"{num1} divide by {num2} reminder is {num1%num2}")
else:
    print("Please enter from the above operation")
print("Thank you for using this calculator")