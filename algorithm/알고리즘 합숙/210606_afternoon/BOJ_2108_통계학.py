import sys
n = int(sys.stdin.readline())
numbers = []

yang = [0]*4001
umm = [0]*4001

for _ in range(n):
    number = int(sys.stdin.readline())
    numbers.append(number)
    if number >= 0:
        yang[number] += 1
    elif number < 0:
        umm[number*-1] += 1

# print(yang)
# print(umm)

# 산술평균
print(int(round(sum(numbers)/n, 0)))

# 중앙값
numbers.sort()
print(numbers[n//2])
tmp_lst = []
# 최빈값
if max(yang) > max(umm):
    for i in range(len(yang)):
        if yang[i] == max(yang):
            tmp_lst.append(i)
    if len(tmp_lst) >= 2:
        print(tmp_lst[1])
    else:
        print(tmp_lst[0])

elif max(yang) < max(umm):
    for i in range(len(umm)):
        if umm[i] == max(umm):
            tmp_lst.append(i*-1)
    tmp_lst.sort()
    if len(tmp_lst) >= 2:
        print(tmp_lst[1])
    else:
        print(tmp_lst[0])

elif max(yang) == max(umm):
    for i in range(len(yang)):
        if yang[i] == max(yang):
            tmp_lst.append(i)
    for i in range(len(umm)):
        if umm[i] == max(umm):
            tmp_lst.append(i*-1)
    tmp_lst.sort()
    if len(tmp_lst) >= 2:
        print(tmp_lst[1])
    else:
        print(tmp_lst[0])

# 범위
print(max(numbers)-min(numbers))

