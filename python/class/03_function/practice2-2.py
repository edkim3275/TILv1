# 간단한 소수 판별
# 입력으로 1개의 정수 number가 주어진다. 정수 number가 소수인지 아닌지 판별하여 출력하시오
number = int(input('2에서 1000사이의 수를 입력하세요 : '))
if number in range(2,1001):
    count = 0
    for i in range(1,number+1):
        if number % i == 0:
            count += 1
    if count == 2:
        print('Y')
    else:
        print('N')
else:
    print('2에서 1000사이의 수를 입력하세요')

# for i in range(2, number):  # 2에서 num-1까지의 수에서
#     if (number % i) == 0:  # 약수가 있다면
#         print('N')  # 소수가 아니다
#         break
#     else:
#         print('Y')
