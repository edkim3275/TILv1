def binary_search(key, left, right, ls_cnt, rs_cnt):
    global cnt
    m = (left + right) // 2
    if left > right:
        return
    # 구간을 살펴본 횟수 차이가 2이상이 난다면 돌아가기
    if ls_cnt - rs_cnt >= 2 or rs_cnt - ls_cnt >= 2:
        return
    # key와 같은 원소를 찾았다면
    if A[m] == key:
        # 차이가 0,-1,1중 하나라면 +1
        if ls_cnt - rs_cnt == 0 or ls_cnt - rs_cnt == 1 or rs_cnt - ls_cnt == 1:
            print(ls_cnt, rs_cnt, i)
            cnt += 1
            return
    else:
        # key값이 더 작다면 왼쪽구간을 봐야한다
        if A[m] > key:
            binary_search(key, left, m-1, ls_cnt+1, rs_cnt)
        # key값이 더 크다면 오른쪽구간을 봐야한다
        elif A[m] < key:
            binary_search(key, m+1, right, ls_cnt, rs_cnt+1)


T = int(input())
for tc in range(1, T+1):
    # N: A에 속한 정수의 개수, M: B에 속한 정수의 개수
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    cnt = 0
    for i in B:
        if i in A:
            if A[(N-1)//2] == i:
                cnt += 1
                continue
            else:
                # print(i, type(i))
                binary_search(i, 0, N-1, 0, 0)
    print('#{} {}'.format(tc, cnt))
