#getting user inputs
num1 = float(input("Enter the first number: "))#float() converts the string to a number
num2 = float(input("Enter the second number: "))
operator = input("Enter an operation (+, -, *, /): ")

# Performing the operation
if operator == '+':
    result = num1 + num2  
elif operator == '-':
    result = num1 - num2    
elif operator == '*':
    result = num1 * num2  
elif operator == '/':
    if num2 == 0:
        print("Error!")
    else:
        result = num1 / num2
else:
    print("Invalid operator! Please enter +, -, *, or /.")
print(f"{num1} {operator} {num2} = {result}")
3
