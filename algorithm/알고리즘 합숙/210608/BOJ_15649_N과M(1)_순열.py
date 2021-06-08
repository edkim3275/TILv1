def permutation(idx):
    if idx == m:
        print(sel)
    else:
        for i in range(n):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                permutation(idx+1)
                check[i] = 0


n, m = map(int, input().split())
# 1부터 n까지의 자연수 중에서 길이가 m인 수열 뽑기
arr = list(range(1, n+1))
sel = [0]*m
check = [0]*n
permutation(0)
