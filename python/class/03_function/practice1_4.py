# 최댓값 구하기
# 주어진 리스트의 요소 중에서 최솟값을 출력
numbers = [7, 10, 22, 4, 3, 17]

# 1. 일반 for문을 이용한 풀이
# result = numbers[0]
# for number in numbers:
#     if result > number:
#         result = number
# print(result)

# 2. 함수를 이용한 풀이
def num_min(numbers):
    result = numbers[0]
    for number in numbers:
        if result > number:
            result = number
    return result

print(num_min(numbers))