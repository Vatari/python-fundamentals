def palindrome_check(element):
    if element == element[::-1]:
        return True
    else:
        return False


numbers = input().split(', ')
for el in numbers:
    print(palindrome_check(el))
