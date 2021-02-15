T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input()))
    cnt_lst = [0] * 10
    cnt = 0
    idx = 0
    # 숫자열에서 하나씩 뽑아봅니다
    for i in ai:
        # 해당 인덱스에 1을 더해줍니다
        cnt_lst[i] += 1
    # 개수를 센 리스트에서 가장 큰 수를 확인합니다.
    for n in cnt_lst:
        if n > cnt:
            cnt = n

    # 가장 많은 카드 숫자를 확인하기 위한 반복문
    ans = 0
    for i in range(10):
        if cnt_lst[i] == cnt:
            ans = i

    print("#{} {} {}".format(tc, ans, cnt))