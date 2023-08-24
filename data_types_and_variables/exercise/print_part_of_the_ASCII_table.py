start_index = int(input())
final_index = int(input())
all_symbols = ''

for char in range(start_index, final_index + 1):
    all_symbols += chr(char) + " "
print(all_symbols)
