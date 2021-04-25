def find_set(x):
    if P[x] != x:
        P[x] = find_set(P[x])
    return P[x]


def union(x, y):
    P[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    # N: 번호 개수, M: 신청서 개수
    N, M = map(int, input().split())
    # 신청서정보(간선)
    info = list(map(int, input().split()))
    # 1~N까지 자신을 대표로하는 리스트
    P = list(range(N+1))

    # 간선정보처럼 번호의 대표 바꾸기
    for i in range(M):
        union(info[2*i], info[2*i+1])

    # 몇개의 그룹이 만들어졌는지 확인
    cnt = 0
    for i in range(1, N+1):
        if P[i] == i:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
