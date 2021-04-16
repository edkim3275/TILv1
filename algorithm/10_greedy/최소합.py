# 우측, 하단
dr = [1, 0]
dc = [0, 1]
# def search(r, c):
#     global minimum
#     nr, nc = r, c
#     minimum += arr[nr][nc]
#     stack.append((nr, nc))
#
#     while stack:
#         row, col = stack.pop()
#
#         for k in range(2):
#             tmp_r = row + dr[k]
#             tmp_c = col + dc[k]
#
#             if tmp_r<0 or tmp_r>N or tmp_c<0 or tmp_c>N:
#                 continue
#
#             stack.append((tmp_r, tmp_c))


def recursive(r, c, cnt):
    # 목표점에 도달했다면 그때까지의 거리를 저장
    if r == N-1 and c == N-1:
        # cnt += arr[r][c]
        stack.append(cnt)
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr > N-1 or nc < 0 or nc > N-1:
            continue

        recursive(nr, nc, cnt+arr[nr][nc])

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # minimum = 0
    stack = []
    # 시작점, 거리정보 인자로 넣어주기
    recursive(0, 0, arr[0][0])
    print(stack)
