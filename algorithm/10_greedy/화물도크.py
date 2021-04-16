def dock(start, end):
    global cnt
    next_end, next_start = start, end
    time_info.pop(time_info.index((start, end)))
    for i in range(len(time_info)):
        if time_info[i][0] >= end:
            if time_info[i][0] >= next_start:

    # dock(next_start, next_end)


T = int(input())
for tc in range(1, T+1):
    # N: 신청서
    N = int(input())
    time_info = []
    first_end = 24
    first_start = 0
    for i in range(N):
        s, e = map(int, input().split())
        time_info.append((s, e))

    # 처음 시작하는 화물작업 찾기
    for i in range(N):
        if first_end > time_info[i][1]:
            first_end = time_info[i][1]
            first_start = time_info[i][0]
    print(time_info)
    print(first_start, first_end)

    cnt = 0
    dock(first_start, first_end)
