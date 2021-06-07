n = int(input())
i = 1

while i <= n:
    for j in range(n-i):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()
    i += 1
