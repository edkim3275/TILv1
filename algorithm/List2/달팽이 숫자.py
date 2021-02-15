arr = [[0] * 4 for _ in range(4)]
cnt = 1
for i in range(4):
    for j in range(4):
        arr[i][j] = cnt
        cnt += 1
    break
for j in range(4 - 1, -1, -1):
    for i in range(1, 4):
        arr[i][j] = cnt
        cnt += 1
    break
for i in range(4 - 1, -1, -1):
    for j in range(3 - 1, -1, -1):
        arr[i][j] = cnt
        cnt += 1
    break
for j in range(4):
    for i in range(3 - 1, 0, -1):
        arr[i][j] = cnt
        cnt += 1
    break
for i in range(1, 3):
    for j in range(1, 3):
        arr[i][j] = cnt
        cnt += 1
    break
for j in range(2, 3):
    for i in range(2, 3):
        arr[i][j] = cnt
        cnt += 1
    break
for i in range(3-1,-1,-1):
    for j in range(2-1,0,-1):
        arr[i][j] = cnt
    break
for i in arr:
    print(*i)
for j in range(5-1)