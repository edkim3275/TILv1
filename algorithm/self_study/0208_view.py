for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-1):
        min_v = 256
        view_lst = []
        if building[i] - building[i-2] > 0:
            view_lst.append(building[i] - building[i-2])
            if building[i] - building[i-1] > 0:
                view_lst.append(building[i] - building[i-1])
                if building[i] - building[i+1] > 0:
                    view_lst.append(building[i] - building[i+1])
                    if building[i] - building[i+2] > 0:
                        view_lst.append(building[i] - building[i+2])
                        for j in view_lst:
                            if min_v > j:
                                min_v = j
                        ans += min_v
                    else:
                        view_lst = []
                else:
                    view_lst = []
            else:
                view_lst = []
        else:
            view_lst = []

        # if view_lst != []:
        #     ans += min_v
    print("#{} {}".format(tc, ans))