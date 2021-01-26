# # 평균을 내는 함수
# def _avg(scores):
#     try:
#         # 실행하다가 
#         return sum(scores) / len(scores)
#     # 특정한 오류 발생하면
#     except ZeroDivisionError:
#         return 0
class NoTestError(ZeroDivisionError):
    pass
def _avg(scores)
# # 위 함수를 활용해서 학생들의 각각의 평균을 구하는 함수
# def class_avg(students):
#     for scores in students.values():
#         print(_avg(scores))
