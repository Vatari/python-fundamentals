chars = []

s1 = input()
s2 = input()
entry = input()

for ch in entry:
    if ord(ch) > ord(s1) and ord(ch) < ord(s2):
        chars.append(ord(ch))

print(sum(chars))
