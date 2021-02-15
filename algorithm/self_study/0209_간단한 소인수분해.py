T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = [2, 3, 5, 7, 11]
    print("#{}".format(tc), end=" ")
    for i in num_lst:
        cnt = 0
        while N % i == 0:
            cnt += 1
            N = N // i
        print(cnt, end=" ")
    print()
#####################################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_lst = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    for i in range(len(num_lst)):
        while N % num_lst[i] == 0:
            cnt[i] += 1
            N //= num_lst[i]
    print("#{} {}".format(tc, ' '.join(map(str, cnt))))