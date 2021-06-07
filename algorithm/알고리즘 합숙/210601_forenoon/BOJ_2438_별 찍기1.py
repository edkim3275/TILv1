n = int(input())
i = 1

while i <= n:
    # 한 줄씩 출력하면서
    for j in range(i):
        print('*', end='')
    # 마지막 줄바꿈은 없도록
    if i == n:
        break
    print()
    # 별 개수 증가
    i += 1
