# abs() 구현하기
# 절댓값은 숫자형 자료(int, float)가 들어오면 절댓값을 반환하고, 복소수형 자료(complex)가 들어오면 해당하는 자료의 크기를 반환합니다.
# 파이썬 내장 함수 abs()를 직접 구현한 my_abs()를 작성하시오.
def my_abs(number):
    if type(number) == int:
        if number >= 0:
            return number
        elif number < 0:
            return (number**2)**(1/2)
    elif type(number) == float:
        if number >= 0:
            return number
        elif number < 0:
            return (number**2)**(1/2)
    elif type(number) == complex:
        return (number.real**2 + number.imag**2) ** (1/2)


print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(abs(3+4j), abs(-0.0), abs(-5))