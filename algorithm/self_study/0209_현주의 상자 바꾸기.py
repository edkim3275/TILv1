T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    counts = [0] * (N+1)
    for i in range(1, Q+1):
        a, b = map(int, input().split())
        counts[a:b+1] = [i] * (b-a+1)
    print("#{}".format(tc), end=" ")
    for i in range(1, N+1):
        print(counts[i], end=" ")
    print()