import sys
k, n = map(int, sys.stdin.readline().split())
lanseon = []
for i in range(k):
    lanseon.append(int(sys.stdin.readline()))
lanseon.sort()
# print(lanseon)
lanseon_avg = int(sum(lanseon)/n)

while True:
    cnt = 0
    for i in range(k):
        cnt += lanseon[i]//lanseon_avg

    if n == cnt:
        print(lanseon_avg)
        break

    lanseon_avg -= 1
