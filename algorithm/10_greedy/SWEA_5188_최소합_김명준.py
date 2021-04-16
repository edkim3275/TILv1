# 우측, 하단
dr = [1, 0]
dc = [0, 1]


def recursive(r, c, cnt):
    global minimum
    # 목표점에 도달했다면 최소거리를 갱신
    if r == N-1 and c == N-1:
        if minimum > cnt:
            minimum = cnt
        return
    # 2방향 탐색
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위를 벗어나면 다른 방향탐색
        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue
        # 해당 깊이에서의 거리가 갱신되어있는 거리보다 크다면 돌아가기
        if cnt > minimum:
            return

        recursive(nr, nc, cnt+arr[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minimum = 9999

    # 시작점, 거리정보 인자로 넣어주기
    recursive(0, 0, arr[0][0])

    print('#{} {}'.format(tc, minimum))
