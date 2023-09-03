def find_evens(numbers):
    evens_index = [i for i, n in enumerate(numbers) if int(n) % 2 == 0]
    # for i, n in enumerate(numbers):
    #   if int(n) % 2 == 0:
    #       evens_index.append(i)

    return evens_index


text = input().split(', ')
print(find_evens(text))
