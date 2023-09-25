import re


def check_func(words):
    words_list = []
    for word in words:
        if word.group(2) == word.group(3)[::-1]:
            words_list.append(word.group(2) + " <=> " + word.group(3))
    return words_list


def print_func(words, words_list):
    if words:
        print(f'{len(words)} word pairs found!')
    else:
        print('No word pairs found!')

    if words_list:
        print(f'The mirror words are:')
        print(*words_list, sep=', ')
    else:
        print('No mirror words!')


text = input()

pattern = r'(#|@)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'
mirror_words = list(re.finditer(pattern, text))

words_result = check_func(mirror_words)
print_func(mirror_words, words_result)
