def get_range(ch1, ch2):
    result = [chr(char) for char in range(ord(ch1) + 1, ord(ch2))] # comprehension solution

    # for char in range(ord(ch1) + 1, ord(ch2)):
    #    result.append(chr(char))
    return f"{' '.join(result)}"


char1 = input()
char2 = input()
print(get_range(char1, char2))
