n = int(input())

for i in range(1, n + 1):
    print(i * "*")

for i in range(n - 1, 0, -1):
    print(i * '*')

# for i in range(n):
#     for j in range(n - i):
#         print(end=' ')
#     for j in range(i + 1):
#         print('* ', end='')
#     print()