# 교체회수가 최소회수를 초과하면 더 갈 필요가 없다.
def go(now, change_cnt):
    global minimum_cnt
    if minimum_cnt < change_cnt:
        return
    # 현재위치가 종점이상이 되면 교체회수 갱신
    if now >= N-1:
        if minimum_cnt > change_cnt:
            minimum_cnt = change_cnt
        return
    # 아직 종점이 아니라면 현재 정류장의 배터리를 저장
    if now < N-1:
        battery = charge[now]
    else:
        return

    # 갈 수 있는 거리만큼 이동
    for i in range(battery, 0, -1):
        go(now+i, change_cnt+1)


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]  # N: 정류장의 수
    station = list(range(N))  # 정류장
    charge = info[1:]  # 정류장 별 배터리 용량
    minimum_cnt = 987654321

    # 현재위치, 교체횟수
    go(0, 0)

    print('#{} {}'.format(tc, minimum_cnt-1))
