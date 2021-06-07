n = int(input())
words = []
for _ in range(n):
    word = input()
    word_cnt = len(word)
    words.append((word, word_cnt))

words = list(set(words))
# 단어의 길이, 단어순서대로 정렬
words.sort(key=lambda word: (word[1], word[0]))
for word in words:
    print(word[0])


# 풀이 2
# n = int(input())
# word_list = []
# sorted_word_list = []
# for _ in range(n):
#     word_list.append(input())
#
# set_word_list = set(word_list)
# for word in set_word_list:
#     sorted_word_list.append((len(word), word))
#
# sorted_word_list.sort()
#
# for word_len, word in sorted_word_list:
#     print(word)
