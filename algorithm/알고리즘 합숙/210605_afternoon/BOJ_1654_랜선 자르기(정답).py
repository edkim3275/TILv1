import sys


def solution(k, n, arr):
    high = arr[0]
    low = 0
    result = 0
    while low <= high:
        mid = (high + low) // 2
        cnt = 0
        if mid == 0:
            return 1

        for val in arr:
            cnt += val//mid
            # 필요랜선의 개수이면서, 최대길이인 경우
            if cnt >= n and mid > result:
                result = mid
                break
        # 필요랜선보다 작게 만들어진 경우
        if cnt < n:
            high = mid - 1
        # 필요랜선보다 많이 만들어진 경우
        else:
            low = mid + 1

    return result


# k: 랜선의 개수, n: 필요랜선의 개수
k, n = map(int, sys.stdin.readline().split())
lanseon = []
for i in range(k):
    lanseon.append(int(sys.stdin.readline()))
lanseon.sort(reverse=True)
print(solution(k, n, lanseon))
