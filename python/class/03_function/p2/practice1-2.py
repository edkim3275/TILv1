# all() 직접 구현하기
# all()은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
# 파이썬 내장 함수 all()을 직접 구현한 my_all()을 작성하시오.
# my_all([]) #=> True
# my_all([1, 2, 5, '6']) #=> True
# my_all([[], 2, 5, '6']) #=> False
def my_all(lsts):
    for lst in lsts:
        if bool(lst) == True:
            pass
        else:
            return False
    return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))
print(my_all([0]))