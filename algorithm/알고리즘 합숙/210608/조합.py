# 5C3
N = 5
R = 3

arr = [1,2,3,4,5]

sel = [0] * R

def combination(idx, sidx):
    # if idx == N:
    #     return

    if sidx == R:
        print(sel)
        return

    if idx == N:
        return

    sel[sidx] = arr[idx]
    combination(idx+1, sidx+1)  # 첫번째로는 두개의 화살표가 동시에 오른쪽으로 가보고
    combination(idx+1, sidx)  # 두번째로는 arr 쪽 화살표만 혼자 가봄.

combination(0,0)











