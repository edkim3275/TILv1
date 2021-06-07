a, b = map(int, input().split())
new_a = str(a)[3::-1]
new_b = str(b)[3::-1]
# print(new_a, type(new_a))
if new_a > new_b:
    ans = new_a
else:
    ans = new_b
print(ans)
