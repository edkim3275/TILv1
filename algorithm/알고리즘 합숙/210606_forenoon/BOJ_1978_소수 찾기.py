def prime(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if sieve[i] == True:
            # i의 배수들은 모두 제외시키기
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]


n = int(input())
numbers = list(map(int, input().split()))
# 소수의 개수를 세기위한 변수
cnt = 0
prime_numbers = prime(1000)
# print(prime_numbers)
for number in numbers:
    if number in prime_numbers:
        cnt += 1

print(cnt)
