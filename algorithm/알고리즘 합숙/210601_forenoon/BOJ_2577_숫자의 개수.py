#  세 개의 자연수 곱하기
result = 1
for i in range(3):
    result *= int(input())

tmp_lst = list(str(result))
#  곱한 값을 저장
tmp = list(set(str(result)))
#  개수를 세기위한 리스트
cnt_lst = [0]*10
#  곱한 값에서 중복제거
for num in tmp:
    cnt_lst[int(num)] = tmp_lst.count(str(num))
#  각각의 숫자가 몇개들어있는지 확인
for num_cnt in cnt_lst:
    print(num_cnt)
