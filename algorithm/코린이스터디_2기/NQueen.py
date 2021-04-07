N = int(input())

answer = 0
visited = [[0]*N for _ in range(N)]

def queens_road(r,c): # 어떤 (r,c) 에서 시작하면 아래, 왼쪽대각선, 오른쪽 대각선을 방문체크 해야함
    # 아래를 방문체크
    for x in range(r, N):
        visited[x][c] = 1

    # 왼쪽 대각선을 방문체크
    column_left = c
    for y in range(r, N):
        if column_left < 0 or column_left >= N:
            break
        else:
            visited[y][column_left] = 1
            column_left -= 1

    # 오른쪽 대각선을 방문체크
    column_right = c
    for z in range(r, N):
        if column_right < 0 or column_right >= N:
            break
        else:
            visited[z][column_right] = 1
            column_right += 1


def queens_road_erase(r,c):
    for x in range(r, N):
        visited[x][c] = 0

    column_left = c
    for y in range(r, N):
        if column_left < 0 or column_left >= N:
            break
        else:
            visited[y][column_left] = 0
            column_left -= 1

    column_right = c
    for z in range(r, N):
        if column_right < 0 or column_right >= N:
            break
        else:
            visited[z][column_right] = 0
            column_right += 1

def deploy_queens(depth):  # 여기 depth 는 r c 에서의 r 과 같다고 생각
    global answer

    if depth == N: # 이경우는 무사히 퀸들이 배치가 끝나서 최대 뎁스까지 내려간 경우
        answer += 1
        return

    else:  # 최대 뎁스까지 도달하지 못한 경우라면?
        for c in range(N): # 각 뎁스는 N회 만큼 화살표 돌릴 기회를 가질 것.
            if visited[depth][c] == 0:
                queens_road(depth,c)  # 아래, 대각선들 다 방문체크 하고
                deploy_queens(depth+1)
                queens_road_erase(depth, c)


deploy_queens(0)  # 맨 위부터 시작해야함

print(answer)

