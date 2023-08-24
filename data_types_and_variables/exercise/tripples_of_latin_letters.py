num = int(input())

for first_symbol in range(num):
    for second_symbol in range(num):
        for third_symbol in range(num):
            print(f"{chr(97 + first_symbol)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")
