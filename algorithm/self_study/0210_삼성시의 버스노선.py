T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0]*5001
    for i in range(N):
        case = list(map(int, input().split()))
        for j in range(case[0], case[1]+1):
            counts[j] += 1
    print("#{} ".format(tc), end="")
    P = int(input())
    for k in range(P):
        C = int(input())
        print(counts[C], end=" ")
    print()