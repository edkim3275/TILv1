def combi_rep(idx, sidx):
    if sidx == m:
        print(*sel)
        return
    if idx == n:
        return
    sel[sidx] = arr[idx]
    combi_rep(idx, sidx+1)
    combi_rep(idx+1, sidx)


n, m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0]*m
combi_rep(0, 0)
