# 더블더블
# 자연수 number를 입력 받아. 1부터 주어진 자연수 number까지 홀수는 2, 짝수는 3을 곱한
# 값들을 출력하시오
# 제약사항 : 주어질 숫자는 30을 넘지 않는다.
# 입력예시 : 5
# 출력예시 : 10
# 입력을 받는다.
# 1~30이 아니면? 다시 입력하라
# 1~30이면? 홀*2 짝*3

# number = int(input('1~30사이의 수를 입력하세요 : '))
# while number in range(1, 31):
#     if number % 2:
#         print(number*2)
#         break
#     else:
#         print(number*3)
#         break
# number = input()

# def double_double(number):
#     if number not in range(1, 31):
#         odd_sum = 0
#         even_sum = 0
#         for i in range(1, number+1):
#             if i % 2 != 0:
#                 odd_sum += i*2
#             else:
#                 even_sum += i*3
#         all_sum = odd_sum + even_sum
#         return all_sum
#     else:
#         number = int(input('30 이하의 자연수를 입력하세요: '))
#         return double_double(number)

# print(double_double(number))

number = int(input())
total = 0
if 0 < number <= 30:
    for i in range (1, number + 1):
        if i % 2:  # i가 짝수일때 false 홀수일때 true
            total += 2 * i
        else:
            total += 3 * i
    print(total)
else:
    print('30을 넘지 않는 숫자를 쓰십시오.')