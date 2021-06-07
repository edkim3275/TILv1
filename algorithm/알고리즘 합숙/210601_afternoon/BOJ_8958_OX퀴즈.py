T = int(input())
for tc in range(T):
    case = input()
    n = len(case)
    # 해당칸의 점수 확인을 위한 리스트
    lst = [0]*n
    # 변수 초기화
    result = 0
    i = 0

    while i < n:
        if i == 0:
            if case[i] == 'O':
                result += 1
                lst[i] = result
        else:
            if case[i] == 'O':
                lst[i] = lst[i-1]+1
        i += 1
    print(sum(lst))
