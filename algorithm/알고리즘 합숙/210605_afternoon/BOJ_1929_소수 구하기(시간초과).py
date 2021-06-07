import sys
m, n = map(int, sys.stdin.readline().split())
while m <= n:
    cnt = 0
    for i in range(1, m + 1):
        if m % i == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        print(m)
    m += 1
