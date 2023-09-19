entry = input().upper()
unique_symbols = ''
curr_symbol = ''
repetitions = ''

for i in range(len(entry)):
    if not entry[i].isdigit():
        curr_symbol += entry[i]
    else:
        for next_symbol in range(i, len(entry)):
            if not entry[next_symbol].isdigit():
                break
            repetitions += entry[next_symbol]
        unique_symbols += curr_symbol * int(repetitions)
        curr_symbol = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
