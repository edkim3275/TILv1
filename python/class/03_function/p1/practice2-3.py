# 간단한 소수 판별2
# 조건, 반복문을 응용하여 numbers 리스트의 요소들이 소수인지 아닌지 판단하는 코드를 작성하시오
# 출력예시
# 26은(는) 소수가 아닙니다. 2은(는) 26의 인수입니다.
# 39은(는) 소수가 아닙니다. 3은(는) 39의 인수입니다.
# 53은(는) 소수입니다.
# 57은(는) 소수가 아닙니다. 3은(는) 57의 인수입니다.
# 79은(는) 소수입니다.
# 85은(는) 소수가 아닙니다. 5은(는) 85의 인수입니다.
# numbers = [26, 39, 51, 53, 57, 79, 85]
# number = int(input('수를 입력하세요 : '))
# def check_pr_num(numbers):
#     count_a = 0
#     for number in numbers:
#         for i in range(1,10):
#             if number % i == 0:
#                 count_a += 1
#         if count_a == 2:
#             print(f'{number}은(는) 소수입니다.')

#     count_b = 0
#     for number in numbers:
#         for i in range(1,10):
#             if number % i == 0:
#                 count_b += 1
#                 if count_b > 2:
#                     print(f'{number}은(는) 소수가 아닙니다. {i}은(는) {number}의 인수입니다.')
                    
# check_pr_num(numbers)
numbers = [26, 39, 51, 53, 57, 79, 85]

for number in numbers:
    for i in range(2, number):
        if (number % i) == 0:
            print(f'{number}은(는) 소수가 아닙니다. {i}은(는) {number}의 인수입니다.')
            break
    else:
        print(f'{number}은(는) 소수입니다.')
    