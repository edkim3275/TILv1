def babyjin(idx, sidx, player, N):
    global p1_flag, p2_flag, sel
    if sidx == R:
        sel.sort()

        # triplet
        if sel[0] == sel[1] == sel[2]:
            if player == 1:
                p1_flag = True
            if player == 2:
                p2_flag = True

        # run
        if sel[1] == sel[0]+1 and sel[2] == sel[1]+1:
            if player == 1:
                p1_flag = True
            if player == 2:
                p2_flag = True

        return

    if idx == N:
        return

    if player == 1:
        sel[sidx] = player_1[idx]
    elif player == 2:
        sel[sidx] = player_2[idx]

    babyjin(idx + 1, sidx + 1, player, N)  # 뽑고가기
    babyjin(idx + 1, sidx, player, N)  # 안뽑고가기


T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    answer = 0
    p1_flag = False
    p2_flag = False
    R = 3
    sel = [0] * R
    for i in range(len(numbers)):
        if i % 2 == 0:
            player_1.append(numbers[i])
            # 3개 이상이 되면 확인시작
            if len(player_1) >= 3:
                N1 = len(player_1)
                babyjin(0, 0, 1, N1)
                if p1_flag:
                    answer = 1
                    break
        elif i % 2:
            player_2.append(numbers[i])
            if len(player_2) >= 3:
                N2 = len(player_2)
                babyjin(0, 0, 2, N2)
                if p2_flag:
                    answer = 2
                    break

    print('#{} {}'.format(tc, answer))
