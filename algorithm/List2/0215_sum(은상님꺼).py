n = 100
for _ in range(10):
    tc = int(input())
    input_arr = []
    for i in range(n):
        input_arr.append(list(map(int, input().split())))

    maximum = 0
    for j in range(100):
        maximum += input_arr[0][j]  # 첫행의 합
    # 각 행의 합
    for i in range(1, 100):
        sum_temp = 0  # 두번째 행부터의 합
        for j in range(100):
            sum_temp += input_arr[i][j]
        if maximum < sum_temp:
            maximum = sum_temp
    # 각 열의 합
    for j in range(100):
        sum_temp = 0
        for i in range(100):
            sum_temp += input_arr[i][j]
        if maximum < sum_temp:
            maximum = sum_temp
    # 대각선의 합1
    sum_temp = 0
    for i in range(100):
        sum_temp += input_arr[i][j]
    if maximum < sum_temp:
        maximum = sum_temp

    # 대각선의 합2
    sum_temp = 0
    for i in range(100):
        sum_temp += input_arr[i][n - j]
    if maximum < sum_temp:
        maximum = sum_temp

    print('#{} {}'.format(tc, maximum))