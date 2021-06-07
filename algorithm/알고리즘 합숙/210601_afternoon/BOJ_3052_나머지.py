tmp_lst = []
for i in range(10):
    tmp_lst.append(int(input())%42)
ans_lst = list(set(tmp_lst))
answer = len(ans_lst)
print(answer)