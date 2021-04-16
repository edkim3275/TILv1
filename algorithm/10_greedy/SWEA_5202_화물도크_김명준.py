# 가장 빨리 끝나는 화물작업 찾기
# 끝나는 시간에 가장 근접하게 시작하는 작업이 다음작업
T = int(input())
for tc in range(1, T+1):
    # N: 신청서
    N = int(input())
    time_info = []
    cnt = 0
    end = 0

    for i in range(N):
        s, e = map(int, input().split())
        time_info.append((s, e))

    # 끝나는 시간 기준으로 정렬
    time_info.sort(key=lambda x : x[1])
    # print(time_info)

    for i in range(N):
        if time_info[i][0] >= end:
            cnt += 1
            end = time_info[i][1]

    print('#{} {}'.format(tc, cnt))
