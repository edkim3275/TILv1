def Prim():
    # 0~V번 까지
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[V] = 0
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1
        # 갱신할 수 있으면 갱신
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)


T = int(input())
for tc in range(1, T+1):
    # 최소신장트리 노드 n 간선 n-1
    # V: 마지막 노드번호, E: 간선의 개수
    V, E = map(int, input().split())
    adj = [[987654321]*(V+1) for _ in range(V+1)]
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w

    print('#{} {}'.format(tc, Prim()))