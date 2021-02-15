def max_val(arr):
    max_v = 0
    for m in arr:
        if max_v < m:
            max_v = m
    return max_v

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, list(input())))

    a = max_val(ai)
    box = [0] * (a+1) # box생성
    for i in ai:
        box[i] += 1

    max_in_box = max_val(box) # 가장많은 카드의 개수

    idx = 0
    for j in range(len(box)):
        if max_in_box == box[j]:
            idx = j

    print("#{} {} {}".format(tc, idx, max_in_box ))
##########################################################
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = input()
    count = [0]*10
    max_count = -1
    max_num = -1
    for i in card:
        count[int(i)] += 1
    for i in range(len(count)):
        if max_count <= count[i]:
            max_num = i
            max_count = count[i]
    print("#{} {} {}".format(tc, max_num, max_count))
##########################################################
def min_search():
    min_value = 987654321
    min_idx = -1
    for i in range(len(box)):
        if box[i] < min_value:
            min_value = box[i]
            min_idx = i
    return min_idx

def max_search():
    max_value = 0
    max_idx = -1
    for i in range(len(box)):
        if box[i] > max_value:
            max_value = box[i]
            max_idx = i
    return max_idx

for tc in range(10):
    N = int(input())
    box = list(map(int, input().split()))

    for i in range(N):
        box[max_search()] -= 1
        box[min_search()] += 1

    print("#{} {}".format(tc, box[max_search()]-box[min_search()]))
####################################################
def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
for tc in range(10):
    N = int(input())
    box = list(map(int, input().split()))
    bubble(box)
    for i in range(N):
        box[0] += 1
        box[-1] -= 1
        bubble(box)
    print("#{} {}".format(tc, box[-1]-box[0]))
####################################################