T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    max_v = 0
    min_v = 10**6+1
    for i in range(N-M+1):
        msc = 0
        for j in range(i, i+M):
            msc += ai[j]
        if max_v < msc:
            max_v = msc
        if min_v > msc:
            min_v = msc
    ans = max_v - min_v

    print("{} {}".format(tc, ans))

##################################################################
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    msc = 0
    for i in range(M):
        msc += ai[i]
    max_v = msc
    min_v = msc
    for i in range(M, N):
        msc = msc + ai[i] - ai[i-M]
        if max_v < msc:
            max_v = msc
        if min_v > msc:
            min_v = msc
    ans = max_v - min_v
    print("{} {}".format(tc, ans))