T = int(input())
for tc in range(1, T+1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    # wi: 화물 무게정보, ti: 트럭 적재용량 정보
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    # 화물 무거운 순서대로
    a = sorted(wi)
    a.reverse()
    # 적재용량 큰 순서대로
    b = sorted(ti)
    b. reverse()
    # print(a, b)
    ans = 0
    # 화물과 적재용량 매칭시켜가면서
    for i in range(len(a)):
        for j in range(len(b)):
            # 적재용량 이하라면 이동시키고
            if a[i] <= b[j]:
                ans += a[i]
                # 해당 트럭은 0표시
                b[j] = 0
                break

    print('#{} {}'.format(tc, ans))
