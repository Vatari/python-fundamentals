def find_even_len_words(words):
    words = [w for w in words if len(w) % 2 == 0]
    return '\n'.join(words)


text = input().split()
print(find_even_len_words(text))
