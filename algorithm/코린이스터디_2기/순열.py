arr = ['a', 'b', 'c']
# sel : 완성 된 순열
sel = [0]*len(arr)
# 방문확인을 위한 체크박스
check = [0]*len(arr)

def perm(idx):
    # base case
    if idx == len(arr):
        print(sel)
    # 재귀 case
    else:
        # arr의 값을 sel에 넣어주기 위해서?
        for i in range(len(arr)):
            if check[i] == 0:

                sel[idx] = arr[i]
                check[i] = 1
                perm(idx+1)
                check[i] = 0

# 첫번째 깊이, 맨 첫번째 행부터
perm(0)