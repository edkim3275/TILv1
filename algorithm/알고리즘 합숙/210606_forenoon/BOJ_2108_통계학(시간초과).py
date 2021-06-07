# # 산술평균
# def arithmetic_mean(arr):
#     m = len(arr)
#     print(int(sum(arr)/m))
#     return
#
#
# # 중앙값
# def median(arr):
#     m = len(arr)//2
#     arr.sort()
#     print(arr[m])
#     return
#
#
# # 최빈값(가장 많이 나타난 수)
# def mode(arr):
#     # 오름차순으로 정렬
#     arr.sort()
#     cnt_arr = []
#     now_max = 0
#     now_mode = 0
#     cnt = 0
#     m = len(arr)
#     for i in range(m):
#         cnt_arr.append(arr.count(arr[i]))
#         # 가장 큰 값에 해당하는 수를 저장
#         if now_max < arr.count(arr[i]):
#             now_max = arr.count(arr[i])
#             now_mode = arr[i]
#             cnt += 1
#         # 여러 개가 있을경우에는 두 번째로 작은 값을 저장
#         elif now_max == arr.count(arr[i]):
#             if now_mode == arr[i]:
#                 continue
#             elif now_mode < arr[i]:
#                 now_mode = arr[i]
#                 cnt += 1
#                 if cnt == 2:
#                     print(now_mode)
#     return
#
#
# # 범위
# def diff(arr):
#     print(max(arr)-min(arr))
#     return


numbers = []
n = int(input())
sum_number = 0
max_num = -4001
min_num = 4001
for i in range(n):
    number = int(input())
    numbers.append(number)
    sum_number += number
    if max_num < number:
        max_num = number
    if min_num > number:
        min_num = number

print(int(round(sum_number/n, 0)))

m = n//2
numbers.sort()
print(numbers[m])

cnt_arr = []
now_max = 0
now_mode = 0
cnt = 0
for i in range(n):
    cnt_arr.append(numbers.count(numbers[i]))
    # 가장 큰 값에 해당하는 수를 저장
    if now_max < numbers.count(numbers[i]):
        now_max = numbers.count(numbers[i])
        now_mode = numbers[i]
        cnt += 1
    # 여러 개가 있을경우에는 두 번째로 작은 값을 저장
    elif now_max == numbers.count(numbers[i]):
        if now_mode == numbers[i]:
            continue
        elif now_mode < numbers[i]:
            now_mode = numbers[i]
            cnt += 1
            if cnt == 2:
                # print(now_mode)
                break
print(now_mode)

print(max_num-min_num)

# arithmetic_mean(numbers)
# median(numbers)
# mode(numbers)
# diff(numbers)
