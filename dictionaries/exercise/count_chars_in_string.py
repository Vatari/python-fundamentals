text = input().split()
text = ''.join(text)
symbols = {}

for ch in text:
    if ch not in symbols:
        symbols[ch] = 0
    symbols[ch] += 1

for k, v in symbols.items():
    print(f"{k} -> {v}")

# COUNTER SOLUTION

# from collections import Counter
#
# word = input()
# result = Counter(word)
#
# for key, value in result.items():
#     if key != ' ':
#         print(f'{key} -> {value}')
