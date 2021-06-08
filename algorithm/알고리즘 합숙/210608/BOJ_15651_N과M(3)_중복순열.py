def permu_rep(idx):
    global cnt
    if idx == m:
        print(*sel)
    else:
        for i in range(n):
            sel[idx] = arr[i]
            permu_rep(idx+1)


n, m = map(int, input().split())
# 1부터 n까지의 자연수 중에서 길이가 m인 수열 뽑기
arr = list(range(1, n+1))
sel = [0]*m
permu_rep(0)
