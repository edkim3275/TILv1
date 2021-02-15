def max_search(A, B):
    max_value = 0
    for i in range(len(B)-len(A)+1):
        msv = 0
        for j in range(len(A)):
            msv += B[i+j] * A[j]
        if max_value < msv:
            max_value = msv
    return max_value

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    if N < M:
        ans = max_search(ai, bj)
    else:
        ans = max_search(bj, ai)

    print("#{} {}".format(tc, ans))
#################################################
# 함수를 사용하지 않은 풀이
if N < M:
max_value = 0
    for i in range(M - N + 1):
        msv = 0
        for j in range(N):
            msv += bj[i + j] * ai[j]
            if max_value < msv:
                max_value = msv
else:
    for i in range(N - M + 1):
        msv = 0
        for j in range(M):
            msv += bj[j] * ai[i + j]
            if max_value < msv:
                max_value = msv