number_of_chars = int(input())
sum_of_ascii = 0

for char in range(number_of_chars):
    next_char = input()
    sum_of_ascii += ord(next_char)

print(f"The sum equals: {sum_of_ascii}")
