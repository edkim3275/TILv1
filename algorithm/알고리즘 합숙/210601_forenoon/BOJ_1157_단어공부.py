# print(ord('B'))
# print(chr(ord('Z')+32))
# if 'B'.isupper():
#     print('대문자')

string = input()
ans_lst = [0]*28
# 문자열 순회
for ea_str in string:
    # 대문자 => 개수 증가
    if ea_str.isupper():
        ans_lst[ord(ea_str)-65] += 1
    # 소문자 => 대문자로 변형 후 개수 증가
    else:
        ans_lst[ord(ea_str)-32-65] += 1

# 가장 많은 개수 확인
max_num = max(ans_lst)
# 중복 => ? 출력
if ans_lst.count(max_num) > 1:
    answer = '?'
# 아니라면 => 리스트 내의 가장 많은 개수의 인덱스 확인 후 대문자로 출력
else:
    answer = chr(ans_lst.index(max_num) + 65)
print(answer)
