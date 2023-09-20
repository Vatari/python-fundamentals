entry = input()
final_text = ''
last_char = ''

for curr_ch in entry:
    if curr_ch != last_char:
        final_text += curr_ch
        last_char = curr_ch

print(final_text)

# print(''.join(set(input())))