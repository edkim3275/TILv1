def make_set(x):
    p[x] = x


# 효율이 고려된 find_set
def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    # 최소신장트리 노드 n 간선 n-1
    # V: 마지막 노드번호, E: 간선의 개수
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # arr = [[0]*(V+1) for _ in range(V+1)]

    # 크루스칼하기 위해서 간선을 가중치 순으로 오름차순 정렬
    edges = sorted(edges, key=lambda x: x[2])

    p = [0] * (V+1)
    # p = list(range(V+1))

    for i in range(V+1):
        make_set(i)

    ans = 0
    cnt = 0  # 간선선택회수
    idx = 0  # 간선의 인덱스

    while cnt < V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            cnt += 1
            ans += edges[idx][2]
        idx += 1

    print('#{} {}'.format(tc, ans))
