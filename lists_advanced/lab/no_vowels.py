def no_vowels(txt):
    vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
    txt = [ch for ch in txt if ch not in vowels]
    return ''.join(txt)


text = input()
print(no_vowels(text))
