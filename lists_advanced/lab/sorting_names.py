def sort_names(names):
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    return sorted_names


text = input().split(', ')
print(sort_names(text))
