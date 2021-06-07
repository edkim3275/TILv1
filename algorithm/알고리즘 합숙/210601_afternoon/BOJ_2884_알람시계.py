H, M = map(int, input().split())
total_time = H*60 + M
new_H = (total_time-45) // 60
if new_H == -1:
    new_H = 23
new_M = (total_time-45) % 60
print(new_H, new_M)
