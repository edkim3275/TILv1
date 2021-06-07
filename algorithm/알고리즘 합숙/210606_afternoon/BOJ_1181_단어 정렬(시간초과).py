# n개의 단어가 들어오면
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
import collections, sys
n = int(sys.stdin.readline())
words = collections.deque()
for i in range(n):
    word = sys.stdin.readline()
    if word in words:
        continue
    words.append(word)
m = len(words)

for i in range(m-1):
    for j in range(i+1, m):
        # 단어의 개수가 더 많은경우
        if len(words[i]) > len(words[j]):
            words[i], words[j] = words[j], words[i]
        # 단어의 개수가 같은경우
        elif len(words[i]) == len(words[j]):
            # 앞에서부터 비교하면서 사전 순으로 배치
            for k in range(len(words[i])):
                # 이후에 나오는 단어가 있다면 변경해야함
                if words[i][k] > words[j][k]:
                    words[i], words[j] = words[j], words[i]
                    break

for i in range(m):
    print(words[i], end='')
