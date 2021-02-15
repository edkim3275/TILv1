# box 내부에 0이 있는지 확인하는 함수
# 0이있다면 계속 반복해야 하므로 True를 반환
def search_zero(brr):
    for i in brr:
        for j in i:
            if j == 0:
                return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print("#{}".format(tc))
    # N*N box
    box = [[0]*N for _ in range(N)]
    # 처음 시작점 1
    num = 1
    # 겉 테두리를 다 돌고 내부로 들어가기 위해 필요한 변수
    idx = 0
    # box내부에 0이 없을때까지 반복
    while search_zero(box):
        # 오른쪽방향
        for j in range(idx, N-idx):
            box[idx][j] = num
            num += 1
        # N이 홀수라면 오른쪽방향에서 끝나기 때문에 확인을 위한 조건
        if num > N**2:
            break
        # 아래쪽방향
        for i in range(idx+1, N-idx):
            box[i][N-(idx+1)] = num
            num += 1
        # 왼쪽방향
        for j in range(N-(idx+2),idx-1,-1):
            box[N-(idx+1)][j] = num
            num += 1
        # N이 짝수라면 왼쪽방향에서 끝나기 때문에 확인을 위한 조건
        if num > N**2:
            break
        # 위쪽방향
        for i in range(N-(idx+2),idx,-1):
            box[i][idx] = num
            num += 1

        idx += 1

    for num_lst in box:
        print(*num_lst)
