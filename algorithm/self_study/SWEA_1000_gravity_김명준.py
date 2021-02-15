T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    max_h = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1
        if max_h < cnt:
            max_h = cnt
    print("#{} {}".format(tc, max_h))