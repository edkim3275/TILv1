def exam_grade(num):
    if 90 <= num <= 100:
        return 'A'
    elif 80 <= num <= 89:
        return 'B'
    elif 70 <= num <= 79:
        return 'C'
    elif 60 <= num <= 69:
        return 'D'
    else:
        return 'F'


n = int(input())
answer = exam_grade(n)
print(answer)
