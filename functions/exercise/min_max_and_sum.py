def solve(args):
    args = [int(n) for n in args]
    return f"The minimum number is {min(args)}\nThe maximum number is {max(args)}\nThe sum number is: {sum(args)}"


numbers = input().split()
print(solve(numbers))
