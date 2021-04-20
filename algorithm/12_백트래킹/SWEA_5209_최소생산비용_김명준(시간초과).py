def search(idx):
    global minimum_value

    if idx == N:
        if minimum_value > sum(temp):
            minimum_value = sum(temp)
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                temp[idx] = cost[idx][i]
                search(idx+1)
                visited[i] = 0
        return


T = int(input())
for tc in range(1, T+1):
    # N: 제품 수
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    temp = [0] * N
    visited = [0] * N
    minimum_value = 987654321

    search(0)

    print('#{} {}'.format(tc, minimum_value))
