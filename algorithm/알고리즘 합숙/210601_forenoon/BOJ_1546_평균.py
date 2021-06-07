def new_grade(num):
    global M
    return num/M*100


# n: 과목의 개수
n = int(input())
grades = list(map(int, input().split()))
M = max(grades)
for i in range(n):
    grades[i] = new_grade(grades[i])

ans = sum(grades) / n
print(ans)
