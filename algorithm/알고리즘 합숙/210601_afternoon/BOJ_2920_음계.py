num = list(map(int, input().split()))
ans = 'mixed'
if num == list(range(1, 9)):
    ans = 'ascending'
elif num == list(range(8, 0, -1)):
    ans = 'descending'
print(ans)
