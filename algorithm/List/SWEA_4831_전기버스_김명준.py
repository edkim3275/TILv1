T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    # 충전기 위치에 1이 들어가있는 리스트 생성
    ct = [0] * (N+1)
    for charge in charges:
        ct[charge] += 1
        # 초기화
        ans = 0
        bus = 0
    # while 반복문 내에서 끝낼 수 있다면 무한반복가능!
    while True:
        bus += K
        if bus >= N: break
        # 이동한 버스 위치에서 한칸씩내려오는 범위
        for i in range(bus, bus-K, -1):
            if ct[i]:
                ans += 1
                # 충전소가 있는 위치로 이동해야하기 때문에 이와같이 위치를 갱신
                bus = i
                break
        # 충전기를 찾지 못한경우
        else:
            ans = 0
            break
    print("#{} {}".format(tc, ans))

