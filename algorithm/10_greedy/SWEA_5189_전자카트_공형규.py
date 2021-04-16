# v: 내가있는현재구역
def dfs(v, total):
    global min_total

    if min_total < total:
        return

    if 0 not in visited:
        total += arr[v][0]
        if min_total > total:
            min_total = total
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, total + arr[v][i])
            visited[i] = 0


for tc in range(1, int(input()) + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    # visited = [0] * n
    min_total = 999999

    visited = [0] * n
    visited[0] = 1
    dfs(0, 0)

    print('#{} '.format(tc), end='')
    print(min_total)