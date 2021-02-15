def bubble_desc(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] <  arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
lst = [1, 1, 1, 2, 3, 4, 6, 8, 51, 46, 89, 779, 12, 64]
bubble_desc(lst)
print(lst)