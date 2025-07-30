num1 = float(input("Enter first number: "))
opeartor = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if opeartor == '+':
    print("Result:", num1 + num2)
elif opeartor == '-':
    print("Result:", num1 - num2)
elif opeartor == '*':
    print("Result:", num1 * num2)
elif opeartor == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operator")