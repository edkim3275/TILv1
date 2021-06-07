n = int(input())
start_num = max(0, n - 9*len(str(n)))

for i in range(start_num, n):
    if i + sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)
