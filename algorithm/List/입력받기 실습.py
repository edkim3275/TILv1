# 3
# 9
# 7 4 2 0 0 6 0 7 0
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

# test case의 번호를 입력
T = int(input())

# 이처럼 외부 txt파일에서 입력을 받아도 좋습니다.
# sys.stdin = open("input.txt","r")

for tc in range(1, T+1):
    # 전체원소의 개수를 N
    N = int(input())
    box = list(map(int, input().split()))
    print(N)
    print(box)

    # ans = 1
    # print("#{} {}".formamt(tc, ans))
