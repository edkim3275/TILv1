for i in range(10):
    T = int(input())
    numbers = list(map(int, input().split()))
    ans = 0
    for tc in range(2, T-2):
        a = 0
        if numbers[tc] - numbers[tc-2] > 0:
            a = numbers[tc-2]
            if numbers[tc] - numbers[tc-1] > 0:
                part_lst.append(numbers[tc] - numbers[tc - 1])
                if numbers[tc] - numbers[tc + 1] > 0:
                    part_lst.append(numbers[tc] - numbers[tc + 1])
                    if numbers[tc] - numbers[tc + 2] > 0:
                        part_lst.append(numbers[tc] - numbers[tc + 2])
        if part_lst != []:
            ans += min(part_lst)

    print("#{} {}".format(i+1, ans))