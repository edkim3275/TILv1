def quick_sort(m1, l, r):
    if l < r:
        s = lomuto_partition(m1, l, r)
        quick_sort(m1, l, s-1)
        quick_sort(m1, s+1, r)


def lomuto_partition(m2, left, right):
    pivot = m2[right]
    i = left - 1
    for j in range(left, right):
        if m2[j] <= pivot:
            i += 1
            m2[i], m2[j] = m2[j], m2[i]
    m2[i+1], m2[right] = m2[right], m2[i+1]
    return i+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    # print(arr)
    print('#{} {}'.format(tc, arr[int(N/2)]))
