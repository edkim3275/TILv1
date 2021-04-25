def search(v, dist):
    global ans
    # 거리가 길어질때마다 갱신
    if ans < dist:
        ans = dist
    # 방문했던 곳이라면 돌아가기
    if visited[v]:
        return
    else:
        visited[v] = 1
        for w in range(N+1):
            if adj_arr[v][w] == 1:
                if visited[w] != 1:
                    search(w, dist+1)
                    visited[w] = 0


T = int(input())
for tc in range(1, T+1):
    # N: 정점 수, M: 간선 수
    N, M = map(int, input().split())
    # 인접행렬 1~N까지
    adj_arr = [[0]*(N+1) for _ in range(N+1)]
    ans = 0
    # 인접행렬에 간선정보 표시
    for _ in range(M):
        x, y = map(int, input().split())
        adj_arr[x][y] = 1
        adj_arr[y][x] = 1
    # 1~N을 출발지점으로 가장 긴 거리 확인
    for i in range(1, N+1):
        visited = [0 for _ in range(N + 1)]
        search(i, 1)

    print('#{} {}'.format(tc, ans))
