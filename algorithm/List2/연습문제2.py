# arr = list(map(int, input().split()))
arr = [0, 1, -3, 0, 0, 1, 3, 0, 1, 1]
n = len(arr)
cnt = 0
for i in range(1<<n):
    sum = 0
    for j in range(n):
        if i & (1<<j):
            sum += arr[j]
    if sum == 0:
        cnt += 1
print(cnt)