from collections import deque


def make_nv(x, y):
    if y == 0:
        return x+1
    elif y == 1:
        return x-1
    elif y == 2:
        return x*2
    elif y == 3:
        return x-10


def calculate(num, cnt):
    q = deque()
    q.append((num, cnt))
    # a = set()
    while q:
        nv, nc = q.popleft()
        # a.add(nv)
        # 범위 벗어난다면
        if nv < 0 or nv > 1000000:
            continue
        # 방문되어있다면
        if visited[nv] == 1:
            continue
        visited[nv] = 1
        # 같은 수가 나왔다면 nc를 출력
        if nv == M:
            print('#{} {}'.format(tc, nc))
            return

        for i in range(4):
            next_v = make_nv(nv, i)
            q.append((next_v, nc+1))


T = int(input())
for tc in range(1, T+1):
    # N: 주어진 수, M: 구하고자 하는 수
    # 1 <= N, M <= 1000000
    N, M = map(int, input().split())
    visited = [0]*1000001
    # 주어진 수, 연산회수를 인자로 넣어주기
    calculate(N, 0)
