def binary_search(arr, l, r):
    global n, m
    left = l
    right = r
    H_lst = []
    while left < right:
        mid = (left + right) // 2
        tree_length = 0
        for i in range(n):
            if arr[i] - mid > 0:
                tree_length += (arr[i]-mid)
        # 목표길이를 넘겼다면 => 길이 늘려서 최적 길이 찾기
        if tree_length >= m:
            H_lst.append(mid)
            left = mid + 1
        # 만약 넘지 못했다면 => 길이를 늘려야 한다
        if tree_length < m:
            right = mid

    return max(H_lst)


# n: 나무의 수, m: 목표길이
n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
print(binary_search(trees, 0, max(trees)+1))
