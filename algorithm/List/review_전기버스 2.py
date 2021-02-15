T = int(input())
for tc in range(1, T+1):
    # K : 이동할 수 있는 거리
    # N : 마지막 종점의 위치
    # M : 충전소의 개수
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    ans = 0

    charge = [0] + charge + [N]
    # 이렇게 표현할 수도 있습니다.
    # charge.insert(0,0)
    # cahrge.append(N)

    last = 0

    # 충전소에 출발점과 도착지를 넣어놓았으므로
    # 입력받은 충전소의 개수보다 2개를 더 추가해주었으니 +2를 해줍니다
    for i in range(1, M+2):
        # 충전소 간의 간격이 내가 현재 최대이동할수있는 거리를 넘는다면 가지 못한다
        if charge[i] - charge[i-1] > K:
            ans = 0
            break
        # 갈 수 있으면 아무작업 x
        # 갈 수 없다면 내 바로직전 충전소로 위치를 옮기고 횟수 1회 증가
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1

    print("#{} {}".format(tc, ans))
###################################
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    ans = 0
    charge = [0] + charge + [N]
    last = 0
    for i in range(1, M+2):
         if charge[i] - charge[i-1] > K:
             ans = 0
             break

        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1
    print("#{} {}".format(tc, ans))