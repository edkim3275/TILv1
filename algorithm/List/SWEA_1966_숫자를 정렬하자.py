def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

T = int(input())
for test_case in range(1, T+1):
    # N : 숫자의 개수
    N = int(input())
    # numbers : 숫자열
    numbers = list(map(int, input().split()))
    bubble_sort(numbers)
    print("#{}".format(test_case), end=" ")
    for number in numbers:
        print("{}".format(number), end=" ")
    print()