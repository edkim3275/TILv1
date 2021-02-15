T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print("#{}".format(tc))
    box = [[0]*N for _ in range(N)]
    num = 1
    for i in range(0, N):
        for j in range(N):
            box[i][j] = num
            num += 1
        break
    for j in range(N-1,-1,-1):
        for i in range(1, N):
            box[i][j] = num
            num += 1
        break
    for i in range(N-1,-1,-1):
        for j in range(N-2,-1,-1):
            box[i][j] = num
            num += 1
        break
    for j in range(N):
        for i in range(N-2,0,-1):
            box[i][j] = num
            num += 1
        break

    for i in range(1, N-1):
        for j in range(1, N-1):
            box[i][j] = num
            num += 1
        break
    for j in range(N-2, N-1):
        for i in range(2, 3):
            arr[i][j] = cnt
            cnt += 1
        break