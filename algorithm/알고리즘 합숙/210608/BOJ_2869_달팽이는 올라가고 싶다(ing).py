a, b, v = map(int, input().split())
# 하루 올라가는 높이
height = a - b
if v % height == 0:
    ans = v // height - b
else:
    ans = v // height + 1
print(ans)
