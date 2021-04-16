N = 5
R = 3

arr = [1,2,3,4,5]

sel = [0] * R


# idx: 전체 컨트롤하는 인덱스, sidx: 셀인덱스
def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i+1, sidx+1)

combination(0, 0)