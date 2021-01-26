# 최댓값과 등장 횟수 구하기
# 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력
numbers = [7, 10, 22, 7, 22, 22, 22, 23, 55, 55, 55, 55]
count = 0
result = numbers[0]
for number in numbers:
    if result < number:
        result = number

for number in numbers:
    if result == number:
        count += 1
print(result, count)

# 함수로 풀어보기
# def func(numbers):
#     output = []
#     count = 0
#     result = numbers[0]
#     for number in numbers:
#         if result < number:
#             result = number

#     for number in numbers:
#         if result == number:
#             count += 1
#     output.append(result)
#     output.append(count)
#     return output

# print(func(numbers))