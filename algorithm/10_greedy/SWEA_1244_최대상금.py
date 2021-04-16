def perm(idx, count):
    global tmp
    if idx == N:
        if cnt == count:
            tmp2 = 0
            for i in range(N):
                tmp2 += sel[i] * (10**(N-1-i))
            if tmp < tmp2:
                tmp = tmp2
        # count += 1
        # print(sel, count)
        return

    if idx == N:
        return

    for i in range(N):
        if check[i] == 0:
            sel[idx] = board_lst[i]
            check[i] = 1
            perm(idx+1, count+1)
            count -= 1
            check[i] = 0


T = int(input())
for tc in range(1, T+1):
    # board: 숫자판 정보, cnt: 교환 횟수
    board, cnt = map(int, input().split())
    # 숫자판 정보를 담아놓은 리스트
    board_lst = list(map(int, str(board)))
    # print(board_lst)
    N = len(board_lst)

    sel = [0]*N
    check = [0]*N

    tmp = 0
    ans = []

    perm(0, 0)
    print('#{} {}'.format(tc, tmp))