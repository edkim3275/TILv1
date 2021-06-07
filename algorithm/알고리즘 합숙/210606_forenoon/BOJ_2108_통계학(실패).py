numbers = []
n = int(input())
cnt_lst = [0]*7999
sum_number = 0
max_num = -4001
min_num = 4001

for i in range(n):
    number = int(input())
    numbers.append(number)
    # 산술평균을 위한 합계
    sum_number += number

    # 최대, 최소
    if max_num < number:
        max_num = number
    if min_num > number:
        min_num = number
    # 숫자가 나온 횟수 저장
    cnt_lst[number] += 1

print(int(round(sum_number/n, 0)))

# 중앙값
m = n//2
numbers.sort()
print(numbers[m])

# 가장 큰 빈도수를 확인
mode = max(cnt_lst)
a = []
# 두개 이상인 경우 => 빈도수가 같은 것들중 두번째로 작은 수
if cnt_lst.count(mode) >= 2:
    for i in range(len(cnt_lst)-1, -1, -1):
        if cnt_lst[i] == mode:
            if i >= 4000:
                a.append(i-7999)
            else:
                a.append(i)
    a.sort()
    print(a[1])
else:
    if cnt_lst.index(mode) >= 4000:
        print(cnt_lst.index(mode)-7999)
    else:
        print(cnt_lst.index(mode))

print(max_num-min_num)
