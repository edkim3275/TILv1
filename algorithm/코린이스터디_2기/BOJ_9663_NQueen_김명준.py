'''
1개 둔다음 가동범위를 1로 변경, 남은 0의 개수가 N-1보다 작다? N_Queen불가능
남은 0의 개수가 N-1보다 클 때, 0인 곳에서 다시 n_queen
반복하면서 만약 체스의 개수가 N개가 되면? 총 횟수 1회증가 되면서 초기화
'''

# 좌대위부터 시계방향으로 팔방향
dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

def n_queen(r, c):
    nr = r
    nc = c
    ck_box[nr][nc] = 1

    for k in range(8):
        tmp_r = nr + dr[k]
        tmp_c = nc + dc[k]
        if tmp_r<0 or tmp_r>=N or tmp_c<0 or tmp_c>=N:
            continue
        if chess[tmp_r][tmp_c] != 0:
            continue

        while True:
            nr += dr[k]
            nc += dc[k]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                while nr != tmp_r:
                    nr -= dr[k]
                    nc -= dc[k]
                break
            ck_box[nr][nc] = 1
    print(ck_box)

N = int(input())
chess = [[0]*N for _ in range(N)]
ck_box = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if chess[i][j] == 0:
            n_queen(i, j)


