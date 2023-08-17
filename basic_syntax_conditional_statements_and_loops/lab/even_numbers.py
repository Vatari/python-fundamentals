num = int(input())
for i in range(num):
    next_num = int(input())

    if next_num % 2 != 0:
        print(f"{next_num} is odd!")
        break
else:
    print("All numbers are even.")
    