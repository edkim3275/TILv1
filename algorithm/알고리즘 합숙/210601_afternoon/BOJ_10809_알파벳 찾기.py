word = input()
alphabet_lst = list(range(97, 123))
N = len(alphabet_lst)
cnt_lst = [-1]*N
for i in range(N):
    alpha = chr(alphabet_lst[i])
    if chr(alphabet_lst[i]) in word:
        cnt_lst[i] = word.index(alpha)

    print(cnt_lst[i], end=' ')
