n = int(input())
Q = n // 5
ans = -1

while Q >= 0:
    tmp_n = n - (Q * 5)
    # 3으로 또한 나누어지는 경우
    if tmp_n % 3 == 0:
        res = tmp_n // 3
        ans = Q + res
        break
    else:
        Q -= 1

print(ans)
