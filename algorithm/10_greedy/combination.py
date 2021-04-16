R = 3
arr = [3,2,8,8,8]
sel = [0] * R
N = len(arr)


# idx: 전체 컨트롤하는 인덱스, sidx: 셀인덱스
def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)  # 뽑고가기
    combination(idx+1, sidx)  # 안뽑고가기

combination(0, 0)