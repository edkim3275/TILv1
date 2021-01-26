# 5의 개수 구하기
# 주어진 리스트의 요소 중에서 5의 개수를 출력하시오
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5, 2, 2, 3, 7, 17, 5, 10]
# print(numbers.count(5))
finding_num = int(input('개수를 찾고자 하는 숫자를 입력하세요 : '))
count = 0
for number in numbers:
    if finding_num == number:
        count += 1
print(count)
