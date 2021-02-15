# 3  # 전체 테스트 케이스의 수
# 9  # 아래의 원소수
# 7 4 2 0 0 6 0 7 0  # 원소들
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    # 전체중 최고의 값
    ans = 0

    # 전체 모든박스를 해보기
    for i in range(N):
        # 중간중간 노란박스 얼마나 떨어지는 확인하기위한 변수
        cnt = 0
        # 나 다음부터 나보다 작은 값을 찾아 카운트
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1

        # 내가 생각한 최고의 값보다 그 값이 크다면? 바꾸자
        if  ans < cnt:
            ans = cnt

    print("#{} {}".format(tc, ans))

