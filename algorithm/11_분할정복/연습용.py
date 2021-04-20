def binary_search(key):
    global cnt
    ls, rs = 0, 0
    left = 0
    right = N-1

    while left <= right:
        m = (left + right)//2
        # m에 찾는 원소가 있으면 방향 따지지 않고 +1
        if ls == 0 and rs == 0 and A[m] == key:
            cnt += 1
            return 1, 1

        if ls > 0 and rs > 0:
            if A[m] == key:
                break

        # m에 위치한 원소가 찾는 원소보다 크다면 왼쪽 구간 탐색
        if A[m] > key:
            ls += 1
            right = m-1
        # m에 위치한 원소가 찾는 원소보다 작다면 오른쪽 구간 탐색
        elif A[m] < key:
            rs += 1
            left = m+1

    return ls, rs


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
        if B[i] in A:
            a, b = binary_search(B[i])
            if a > 0 and b > 0:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
