# 3  # 전체 테스트 케이스의 수
# 9  # 아래의 원소수
# 7 4 2 0 0 6 0 7 0  # 원소들
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

test_case = int(input())
print(test_case)
for i in range(test_case):
    cnt_numbers = list(map(int, input()))
    numbers = list(map(int, input().split()))
    print(cnt_numbers)
    print(numbers)