# ant() 직접 구현하기
# any()는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
# 파이썬 내장 함수 any()을 직접 구현한 my_any() 함수를 작성하시오.
# my_any([1, 2, 5, '6']) #=> True
# my_any([[], 2, 5, '6']) #=> True
# my_any([0]) #=> False
def my_any(lsts):
    for lst in lsts:
        if bool(lst) == True:
            return True
    else:
        return False
    
print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any[0])