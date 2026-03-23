def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2


# Take input once
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Subtraction:", subtraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))