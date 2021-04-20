def go(start, battery, cnt):
    if start >= N-1:
        # print(cnt)
        return
    else:
        for i in range(battery, 0, -1):
            if battery >= N:
                continue
            else:
                go(start+i, charge[battery], cnt+1)
                cnt -= 1


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    # N: 정류장의 수
    N = info[0]
    station = list(range(N))
    charge = info[1:]
    # 현재위치, 갈수있는 거리, 교체횟수
    go(0, charge[0], 0)

    print(station)
    print(charge)
