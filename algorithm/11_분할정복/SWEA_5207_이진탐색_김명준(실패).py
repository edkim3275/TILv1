def binary_search(n, lst, l, r, lf, rf):
    global cnt
    if l >= r:
        return
    else:
        m = (l+r)//2
        if lst[m] == n:
            if lf == 0 and rf == 0:
                cnt += 1
                return
            if lf > 0 and rf > 0:
                if lf-rf == 0 or lf-rf == 1 or lf-rf == -1:
                    cnt += 1
                    return
        # if lst[m] == n:
        #     cnt += 1
        #     return

        if lst[m] > n:
            binary_search(n, lst, l, m-1, lf+1, rf)

        elif lst[m] < n:
            binary_search(n, lst, m+1, r, lf, rf+1)


T = int(input())
for tc in range(1, T+1):
    # N: A에 속한 정수의 개수, M: B에 속한 정수의 개수
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    # print(A)
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(M):
        # B[i]: 찾으려는 수, A: A에서 수 찾기, left, right
        binary_search(B[i], A, 0, N-1, 0, 0)

    print('#{} {}'.format(tc, cnt))
