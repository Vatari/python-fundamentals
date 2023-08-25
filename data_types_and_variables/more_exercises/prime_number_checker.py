def get_prime(number):
    c = 0
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            c = c + 1
            is_prime = False
    print(is_prime)


num = int(input())
get_prime(num)
