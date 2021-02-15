for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    # 우선 box내의 최대,최소값를 구한다
    max_val = 0
    min_val = 101
    for bx in box:
        if max_val < bx:
            max_val = bx
        if min_val > bx:
            min_val = bx
    # 각 박스 개수에 대한 리스트 생성
    box_lst = [0]*101
    for i in box:
        box_lst[i] += 1
    # dump가 차감 될 때마다 개수 젤 많은 박스 -1, 제일적은 박스 -1,
    # 두번째로 많은 박스 +1, 두번째로 적은 박스 +1
    for j in range(dump):
        box_lst[max_val] -= 1
        box_lst[max_val-1] += 1
        box_lst[min_val] -= 1
        box_lst[min_val+1] += 1
        # 변한 박스에서 다시 최대 최소값를 구한다
        for bx in box:
            if max_val < bx:
                max_val = bx
            if min_val > bx:
                min_val = bx
    ans = max_val - min_val
    print("#{} {}".format(tc, ans))
