def find_palindromes(words):
    palindrome = input()
    palindromes = [w for w in words if w == w[::-1]]
    found = palindromes.count(palindrome)
    print(f"{palindromes}")
    print(f"Found palindrome {found} times")


text = input().split()
find_palindromes(text)
