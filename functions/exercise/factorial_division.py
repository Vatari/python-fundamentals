def calc_factorial(n1, n2):
    for factorial in range(1, n1):
        n1 *= factorial
    for factorial in range(1, n2):
        n2 *= factorial
    res = n1 / n2
    return f"{res:.2f}"


num1 = int(input())
num2 = int(input())
print(calc_factorial(num1, num2))
