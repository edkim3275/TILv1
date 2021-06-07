n = int(input())
num_lst = list(map(int, input().split()))
max_num = -1000001
min_num = 987654321
for i in range(n):
    if max_num < num_lst[i]:
        max_num = num_lst[i]
    if min_num > num_lst[i]:
        min_num = num_lst[i]
print(min_num, max_num)
