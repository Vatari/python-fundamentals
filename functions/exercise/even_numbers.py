def get_evens(args):
    result = []
    for n in args:
        if int(n) % 2 == 0:
            result.append(int(n))
    return result


numbers = input().split()
print(get_evens(numbers))
