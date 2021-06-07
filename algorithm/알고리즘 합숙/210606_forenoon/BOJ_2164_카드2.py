import collections
n = int(input())
card = list(range(1, n+1))
q = collections.deque(card)
# print(q)
while q:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    if len(q) == 1:
        print(q[0])
        break
    pop_card = q.popleft()
    q.append(pop_card)
