for i in range(10):
    T = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    for tc in range(2, T-2):
        part_lst = []
        if numbers[tc] - numbers[tc-2] > 0:
            part_lst.append(numbers[tc] - numbers[tc - 2])
            if numbers[tc] - numbers[tc-1] > 0:
                part_lst.append(numbers[tc] - numbers[tc - 1])
                if numbers[tc] - numbers[tc + 1] > 0:
                    part_lst.append(numbers[tc] - numbers[tc + 1])
                    if numbers[tc] - numbers[tc + 2] > 0:
                        part_lst.append(numbers[tc] - numbers[tc + 2])
                    else:
                        part_lst = []
                else:
                    part_lst = []
            else:
                part_lst = []
        else:
            part_lst = []

        if part_lst != []:
            ans += min(part_lst)

    print("#{} {}".format(i+1, ans))