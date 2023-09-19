entry = input()
encrypted = []

for ch in entry:
    new_ch = chr(ord(ch) + 3)
    encrypted.append(new_ch)

print(''.join(encrypted))
