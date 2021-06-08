def combi_rep(idx, sidx):
    global cnt
    if sidx == n:
        print(order)
        cnt += 1
        return
    if idx == len(menu):
        return
    order[sidx] = menu[idx]
    combi_rep(idx, sidx+1) # 중복으로 뽑기
    combi_rep(idx+1, sidx) # 그냥 지나가기


menu = [1, 2, 3, 4, 5]
cnt = 0
# 사람수
n = int(input())
# 가능한 주문
order = [0]*n
combi_rep(0, 0)
print(cnt)