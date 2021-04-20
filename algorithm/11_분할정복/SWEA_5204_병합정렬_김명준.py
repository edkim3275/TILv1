def merge_sort(m):
    global cnt
    # base case: 분할해서 개수가 1개면 m을 반환
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = [0] * mid
    right = [0] * (len(m) - mid)

    for x in range(mid):
        left[x] = m[x]
    for x in range(len(m) - mid):
        right[x] = m[x + mid]

    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)


def merge(left, right):
    idx_L, idx_R, idx = 0, 0, 0
    result = [0] * (len(left) + len(right))
    while idx_L < len(left) or idx_R < len(right):
        if idx_L < len(left) and idx_R < len(right):
            if left[idx_L] <= right[idx_R]:
                result[idx] = left[idx_L]
                idx += 1
                idx_L += 1
            else:
                result[idx] = right[idx_R]
                idx += 1
                idx_R += 1
        elif idx_L < len(left):
            result[idx] = left[idx_L]
            idx += 1
            idx_L += 1
        elif idx_R < len(right):
            result[idx] = right[idx_R]
            idx += 1
            idx_R += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print('#{} {} {}'.format(tc, merge_sort(arr)[N//2], cnt))
