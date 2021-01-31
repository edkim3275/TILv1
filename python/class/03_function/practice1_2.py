students = [
    '이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희'
    ]

# def count(students):
#     return students.count('이영희')

# print(count(students))

def count(students):
    count = 0
    for student in students:
        if '이영희' == student:
            count += 1
    return count

print(count(students))