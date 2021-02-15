T = int(input())
for tc in range(1, T+1):
    # N: 칠할 영역의 개수
    N = int(input())
    # 10*10 box
    # box = [[0] * 10] * 10
    box = [[0]*10 for i in range(10)]
    # 색칠하기
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                # 조건을 어떻게 주어야 할까..
                if box[j][k] == 0:
                    box[j][k] += color
                if box[j][k] == 1 and color == 2:
                    box[j][k] += color
                if box[j][k] == 2 and color == 1:
                    box[j][k] += color
    # 보라색(3)이 된 칸 수 세기
    count = 0
    for i in range(10):
        for j in range(10):
            if box[i][j] == 3:
                count += 1
    print("#{} {}".format(tc, count))