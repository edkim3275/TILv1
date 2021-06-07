n = int(input())
for i in range(6, -1, -1):
    if n // (10**i) >= 1:
        start = i
        break
start_num = ((n // (10 ** start)) - 1) * (10 ** start)

while start_num <= n:
    tmp = start_num
    constructor = start_num
    for j in range(start, -1, -1):
        constructor += (tmp // (10**j))
        tmp = tmp - ((tmp // (10**j)) * (10**j))
    if constructor == n:
        print(start_num)
        break
    start_num += 1

if start_num > n:
    print(0)
