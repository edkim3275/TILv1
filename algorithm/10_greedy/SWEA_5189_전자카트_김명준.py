def perm(idx):
    global min_consumption
    if idx == N:
        tmp2 = 0
        # 처음 시작이 1이 아닌경우 돌아가기
        if sel[0] != 1:
            return
        # 다시 사무실도 돌아와야하니 1을더해준다 [1, 2, 3, 1]
        tmp_sel = sel + [1]
        # area경로를 이동하면서 에너지 소비량 더해주기
        for i in range(len(tmp_sel)-1):
            tmp2 += area[tmp_sel[i]-1][tmp_sel[i+1]-1]
        # 최소 에너지 갱신
        if min_consumption > tmp2:
            min_consumption = tmp2
        return

    for i in range(N):
        if visit[i] == 0:
            sel[idx] = route[i]
            visit[i] = 1
            perm(idx+1)
            visit[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    # 이동경로 확인을 위한 변수
    route = list(range(1, N+1))
    # 가능한 경로확인을 위한 sel
    sel = [0] * N
    visit = [0] * N

    min_consumption = 9999

    perm(0)
    print('#{} {}'.format(tc, min_consumption))
