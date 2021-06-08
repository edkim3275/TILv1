def combination(idx, sidx):
    if sidx == m:
        print(*sel)
        return
    if idx == n:
        return
    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


n, m = map(int, input().split())
arr = list(range(1, n+1))
sel = [0]*m
combination(0, 0)
