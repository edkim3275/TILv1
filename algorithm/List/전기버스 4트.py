T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    t_no = list(map(int, input().split()))
    # 처음위치
    idx = 0
    # 이동한 최소 횟수
    ans = 0
    # 충전소 위치파악을 위한 리스트
    c_lst = []
    # 위치가 종점을 넘긴다면 반복문 종료
    while idx < N:
        # 충전소의 위치를 꺼내면서
        for i in t_no:
            # 현위치에서 이동할수있는 거리내에 충전소가 위치해있다면
            if i <= idx+K:
                # 충전소의 위치를 리스트에 담는다
                c_lst.append(i)
        # 이때 만약 리스트에 담겨진 것이 없다면 0을 출력하고 종료
        if len(c_lst) == 0:
            print("#{} 0".format(tc))
            break
        # 그 외에는
        else:
            # 현재 위치에 리스트에 담긴 마지막 위치값을 더해서 그곳으로 이동
            idx += c_lst[-1]
            # 이동회수에 1을 추가
            ans += 1
            # 만약 이동위치가 종점을 넘긴다면
            if idx >= N:
                print("#{} {}".format(tc, ans))