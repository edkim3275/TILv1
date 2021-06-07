# 2. 생성될 수 있는 체스판과 비교
def check_board(i, j):
    global min_cnt
    new_board = []
    for k in range(i, i+8):
        col = ''
        for l in range(j, j+8):
            col += board[k][l]
        new_board.append(col)

    # 3. 최소 변경 회수를 갱신
    change_cnt = 0
    for r in range(8):
        for c in range(8):
            if new_board[r][c] != white_start_board[r][c]:
                change_cnt += 1
    if min_cnt > change_cnt:
        min_cnt = change_cnt

    change_cnt = 0
    for r in range(8):
        for c in range(8):
            if new_board[r][c] != black_start_board[r][c]:
                change_cnt += 1
    if min_cnt > change_cnt:
        min_cnt = change_cnt


N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 1. 흰 시작 체스판, 검 시작 체스판 거름망을 만들어서
white_start_board = [0 for _ in range(8)]
for w in range(8):
    if w%2 == 0:
        white_start_board[w] = 'WBWBWBWB'
    else:
        white_start_board[w] = 'BWBWBWBW'

black_start_board = [0 for _ in range(8)]
for b in range(8):
    if b%2 == 0:
        black_start_board[b] = 'BWBWBWBW'
    else:
        black_start_board[b] = 'WBWBWBWB'

min_cnt = 987654321
# 8*8 만들 수 있는 시작점만 확인
for i in range(N-7):
    for j in range(M-7):
        check_board(i, j)

print(min_cnt)
