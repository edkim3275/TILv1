def my_max(a, b):
    if a > b:
        return a
    else:
        return b

# 전체적인 for문을 만들때는 i는 자제합시다.
for tc in range(1, 11):
    N = int(input())
    # input()으로 변수로 활용 안할 수도 있기는 합니다.
    building = list(map(int, input().split()))
    # 변수 초기화는 test case 안에서!!!
    ans = 0

    for idx in range(2, N-2):
        # 왼쪽 2집, 오른쪽 2집중 큰값 그리고 그중에서 다시 큰값을 구해보면 4집중 가장 큰 집이 나옵니다.
        # my_max 전달인자로 2개를 가지니 왼쪽 두집, 오른쪽두집 뽑힌 집들을 이용해야 함
        # my_max를 가변인자를 받는 함수로 지정해서 그냥 max 함수처럼 작동하게 해도 됩니다.(국현님 idea)
        max_h = my_max(my_max(building[idx-2], building[idx-1]) , my_max(building[idx+1], building[idx+2]))
        # 4집중 가장 큰 집보다 idx 빌딩이 크다면
        if building[idx] > max_h:
            # 그 차이를 더해줍니다.
            ans += building[idx] - max_h
    print("#{} {}".format(tc, ans))