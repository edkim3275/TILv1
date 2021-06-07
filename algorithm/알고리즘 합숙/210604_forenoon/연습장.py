# n = int(input())
# word_lst = []
# for i in range(n):
#     word_lst.append(input())
import sys
n = int(sys.stdin.readline())
word_lst = [sys.stdin.readline().strip() for i in range(n)]
# 중복제거
word_lst = list(set(word_lst))

N = len(word_lst)
# 길이 순 정렬
for i in range(N-1):
    for j in range(i+1, N):
        if len(word_lst[i]) > len(word_lst[j]):
            word_lst[i], word_lst[j] = word_lst[j], word_lst[i]

cnt_lst = [0]*N
for i in range(N):
    cnt_lst[i] = len(word_lst[i])

# 사전 순 정렬
for i in range(N-1):
    # 개수가 같은경우
    if cnt_lst[i] == cnt_lst[i+1]:
        # 개수가 다를 때 까지
        while cnt_lst[i] == cnt_lst[i+1]:
            for k in range(cnt_lst[i]):
                # 단어 우선순위 비교
                if word_lst[i][k] > word_lst[i+1][k]:
                    word_lst[i], word_lst[i+1] = word_lst[i+1], word_lst[i]
                    break
            i += 1
            if cnt_lst[i] != cnt_lst[i+1]:
                break
            if i == N-1:
                break

print(word_lst)