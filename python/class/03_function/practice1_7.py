# 'a'가 싫어
# 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력

word = input()
output_word = ''
for i in word:
    if i != 'a':
        output_word += i
print(output_word)
