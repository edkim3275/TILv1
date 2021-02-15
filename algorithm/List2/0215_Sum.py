for tc in range(10):
    # case 번호
    case_num = int(input())
    # 100*100 box
    box = []
    for _ in range(100):
        box.append(list(map(int, input().split())))
    # 최대값 초기화
    max_sum = 0
    # 행의 합중 최대값 구하기
    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += box[i][j]
        if max_sum < sum_col:
            max_sum = sum_col
    # 열의 합중 최대값 구하기
    for j in range(100):
        sum_row = 0
        for i in range(100):
            sum_row += box[i][j]
        if max_sum < sum_row:
            max_sum = sum_row
    # 오른쪽 아래로 내려가는 대각선의 합
    sum_diag_1 = 0
    for i in range(100):
        sum_diag_1 += box[i][i]
    if max_sum < sum_diag_1:
        max_sum = sum_diag_1
    # 왼쪽 아래로 내려가는 대각선의 합
    sum_diag_2 = 0
    for i in range(100):
        sum_diag_2 += box[i][99-i]
    if max_sum < sum_diag_2:
        max_sum = sum_diag_2
    print("#{} {}".format(case_num, max_sum))