# n: 카드의 개수, m: 타깃넘버
n, m = map(int, input().split())
cards = list(map(int, input().split()))
# print(cards)
delete_lst = []
for i in range(n):
    print(i)
    if cards[i] > m:
        delete_lst.append(cards[i])

for j in range(len(delete_lst)):
    cards.remove((delete_lst[j]))
# print(cards)