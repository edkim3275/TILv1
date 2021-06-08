# ssadadaaasadaaas
string = input()
n = int(input())
ans_lst = []
for i in range(0, len(string)-n-1, n):
    tmp_dict = {}
    for j in range(i, i+n):
        # 해당 구간에서 가장많은 알파벳 저장
        tmp_dict[string[j]] = 0
    for j in range(i, i+n):
        tmp_dict[string[j]] += 1
    cnt = 0
    for k in tmp_dict.values():
        if cnt < k:
            cnt = k
    for l in tmp_dict:
        if tmp_dict[l] == cnt:
            ans_lst.append(l)

# print(ans_lst)
temp = {}
for i in range(len(ans_lst)):
    temp[ans_lst[i]] = 0

for i in range(len(ans_lst)):
    temp[ans_lst[i]] += 1

max_num = 0
# print(temp)
for i in temp:
    if temp[i] > max_num:
        max_num = temp[i]
for j in temp:
    if temp[j] == max_num:
        print(j)
        break

# print(tmp_dict)
# print(len(tmp_dict))
# print(max(tmp_dict))
# print(tmp_dict.values())