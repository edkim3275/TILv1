arr = [55, 7, 78, 12, 42]

def BubbleSort(a):  # 정렬할 List
    for i in range(len(a)-1, 0, -1):  # 범위의 끝 위치
        for j in range(0, i):
            # 두 수를 비교해서 만약 전 수가 크다면
            if a[j] > a[j+1]:
                # 서로의 위치를 바꿔라
                a[j], a[j+1] = a[j+1], a[j]

BubbleSort(arr)
print(arr)