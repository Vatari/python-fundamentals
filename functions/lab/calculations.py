
def calculate(operation, num1: int, num2: int):
    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 // num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


operation = input()
num1 = int(input())
num2 = int(input())
print(calculate(operation, num1, num2))
