for tc in range(1, 11):
    N = int(input())
    box = list(map(int, input().split()))
    count = [0] * (len(box)+1)
    max_h = 0
    min_h = 101
    for i in range(len(box)):
        count[box[i]] += 1
        if max_h < box[i]:
            max_h = box[i]
        if min_h > box[i]:
            min_h = box[i]

    while N > 0 and max_h - 1 > min_h:
        count[max_h] -= 1
        count[max_h-1] += 1
        count[min_h] -= 1
        count[min_h+1] += 1

        if count[max_h] == 0:
            max_h -= 1
        if count[min_h] == 0:
            min_h += 1
        N -= 1

    print("#{} {}".format(tc, max_h-min_h))
