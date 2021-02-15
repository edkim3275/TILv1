def counting_sort(arr):
    # 최대값 구하기
    max_v = 0
    for i in arr:
        if max_v < i:
            max_v = i
    # counts 배열 생성
    counts = [0] * (max_v+1)
    for i in arr:
        counts[i] += 1
    # 누적합
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]
    # 임시 list 생성
    temp = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        counts[arr[i]] -= 1
        temp[counts[arr[i]]] = arr[i]
    return temp

lst = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(lst))
