# 주어진 고유번호
id_numbers = map(int, input().split())
tmp = 0

# 하나씩 뽑으면서 제곱 수 더하기
for num in id_numbers:
    tmp += num**2
# 나온수에서 10을 나눈 나머지
j_num = tmp % 10

print(j_num)
