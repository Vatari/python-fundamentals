entry = input()
digits = [d for d in entry if d.isnumeric()]
text = [t for t in entry if t.isalpha()]
symbols = [s for s in entry if not s.isnumeric() and not s.isalpha()]

print(''.join(digits))
print(''.join(text))
print(''.join(symbols))
