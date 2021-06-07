# 윤년 : 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
def check_leap_year(num):
    if num % 4 == 0 and num % 100 != 0:
        return 1
    elif num % 400 == 0:
        return 1
    else:
        return 0


n = int(input())
print(check_leap_year(n))
