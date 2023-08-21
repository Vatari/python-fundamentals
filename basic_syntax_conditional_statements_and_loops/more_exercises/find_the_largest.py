num = int(input())

digits = list(str(num))
digits.sort(reverse=True)
largest = int(''.join(digits))
print(largest)
