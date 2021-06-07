n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in range(n-1):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for i in range(n):
    print(numbers[i])
