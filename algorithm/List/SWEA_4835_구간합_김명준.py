T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    ai = list(map(int, input().split()))
    # 각각의 구간합을 추가해줄 리스트를 생성
    num_lst = [0] * (N-M+1)
    # 인덱스 하나하나를 꺼내서
    for i in range(N-M+1):
        # M구간 만큼 더한 구간합을 리스트에 추가
        for j in range(M):
            num_lst[i] += ai[i+j]
    # 최대 최소값의 초기값
    max_val = 0
    min_val = 10000*M+1
    # 리스트에서의 최대 최소값을 구한 후
    for num in num_lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    # 차이를 구해줍니다.
    ans = max_val - min_val

    print("#{} {}".format(tc, ans))