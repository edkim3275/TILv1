# word_priority = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
#                  'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#                  'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
#                  'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
#                  'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#                  'z': 26}


n = int(input())
word_lst = []
for i in range(n):
    word_lst.append(input())
# 중복제거
word_lst = list(set(word_lst))

N = len(word_lst)
# 길이 순 정렬
for i in range(N-1):
    for j in range(i+1, N):
        if len(word_lst[i]) > len(word_lst[j]):
            word_lst[i], word_lst[j] = word_lst[j], word_lst[i]

# 개수 리스트
cnt_lst = [0]*N
for i in range(N):
    cnt_lst[i] = len(word_lst[i])
# print(cnt_lst)
# print(word_lst)

# 사전 순 정렬
for i in range(N-1):
    # 개수가 같은경우
    if cnt_lst[i] == cnt_lst[i+1]:
        # 개수가 다를 때 까지
        while cnt_lst[i] == cnt_lst[i+1]:
            print(word_lst)
            for k in range(cnt_lst[i]):
                # 단어 우선순위 비교
                if word_lst[i][k] > word_lst[i+1][k]:
                    word_lst[i], word_lst[i+1] = word_lst[i+1], word_lst[i]
                    break
            i += 1
            if i == N-1:
                break

print(word_lst)
