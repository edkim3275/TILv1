T = int(input())
for tc in range(T):
    # k: 층, n: 호
    k = int(input())
    n = int(input())

    # 0층 n호까지의 사람들
    zero_floor = list(range(n+1))

    # 해당 층에 호의 사람들 == 아래층 호까지의 사람들의 합
    related_floor = [0]*(n+1)
    for i in range(1, k+1):
        # 1층인 경우
        if i == 1:
            for j in range(n+1):
                for k in range(j+1):
                    related_floor[j] += zero_floor[k]
        else:
            next_floor = [0]*(n+1)
            for j in range(n+1):
                for k in range(j+1):
                    next_floor[j] += related_floor[k]
            for j in range(n+1):
                related_floor[j] = next_floor[j]

    print(related_floor[n])
