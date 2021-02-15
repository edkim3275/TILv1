T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    max_value = 0
    min_value = 10**7
    for a in ai:
        if a > max_value:
            max_value = a
        if a < min_value:
            min_value = a
    ans = max_value - min_value

    print("#{} {}".format(tc, ans))