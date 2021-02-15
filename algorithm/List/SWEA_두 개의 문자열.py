T = int(input())
for tc in range(1, T + 1):
    # N : Ai의 개수
    # M : Bj의 개수
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    # 상황마다의 곱하고 더한 값
    mul_sum_case = 0
    # 최대값 변수
    max_val = 0

    if M > N:
        for i in range(M-N+1):

            for j in range(N):
                # Ai의 경우 그대로 인덱스 값이 j로 유지되지만
                # Bj의 경우에는 인덱스에 i를 더해줘야합니다.
                mul_sum_case += (Ai[j] * Bj[i+j])
            if mul_sum_case > max_val:
                max_val = mul_sum_case

    else:
        for i in range(N-M+1):

            for j in range(M):
                mul_sum_case += (Ai[i+j] * Bj[j])
            if mul_sum_case > max_val:
                max_val = mul_sum_case


    print("#{} {}".format(tc, max_val))