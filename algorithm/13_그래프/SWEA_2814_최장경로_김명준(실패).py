def dfs(start):
    global cnt
    stack = []
    stack.append(start)
    while stack:
        v = stack.pop()
        # 방문했던 곳을 들리게 된다면 돌아가기
        # if visited[v] == 1:
        #     distance[start] = cnt
        #     return
        if visited[v] == 0:
            visited[v] = 1
            distance[v] = cnt
            cnt += 1
            # print(v)
            for w in range(N+1):
                if adj_arr[v][w] == 1:
                    if visited[w] == 0:
                        stack.append(w)


T = int(input())
for tc in range(1, T+1):
    # N: 정점 수, M: 간선 수
    N, M = map(int, input().split())
    adj_arr = [[0]*(N+1) for _ in range(N+1)]

    distance = [0]*(N+1)

    for _ in range(M):
        x, y = map(int, input().split())
        adj_arr[x][y] = 1
        adj_arr[y][x] = 1
    # for i in range(N+1):
    #     print(adj_arr[i])
    for i in range(1, N+1):
        visited = [0 for _ in range(N + 1)]
        cnt = 1
        dfs(i)

    print('#{} {}'.format(tc, max(distance)))
