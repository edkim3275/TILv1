a, b = map(int, input().split())
# 최대공약수
a_lst = []
b_lst = []
for i in range(a, 0, -1):
    # 나머지가 0이라면 약수
    if a % i == 0:
        a_lst.append(i)
for j in range(1, b+1):
    if b % j == 0:
        b_lst.append(j)
# print(a_lst)
for num in a_lst:
    if num in b_lst:
        print(num)
        maximum_common_divisor = num
        break

# 최소공배수
if maximum_common_divisor == 1:
    print(a*b)
else:
    tmp_a = a // maximum_common_divisor
    tmp_b = b // maximum_common_divisor
    print(maximum_common_divisor*tmp_a*tmp_b)
