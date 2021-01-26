# 최댓값 구하기
# 주어진 리스트의 요소 중에서 최댓값을 출력
numbers = [7, 10, 22, 4, 3, 17]

result = 0
for number in numbers:
    if result < number:
        result = number
print(result)