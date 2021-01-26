# 단어 뒤집기
# 입력으로 짧은 영단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력
# 단어를 사용자로 부터 받는다.
# 새로 출력할 ''를 형성해서 거기에
# 단어의 역순으로 넣어준다

word = input()
k = len(word)
output_word = ''
for i in range(k-1, -1, -1):
    output_word += word[i]
print(output_word)