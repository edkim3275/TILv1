# 재귀 순열

arr = ['a', 'b', 'c']  # 재료가 될 arr, 여기서 찝어와서 sel 에 넣을것
sel = [0, 0, 0]  # 결국 내가 몇개를 '보여' 줄거냐의 issue
check = [0, 0, 0]  # 화살표가 멈출지 말지 체크해주는 리스트


def perm(idx):
    if idx == 3:  # 결국 depth 가 3까지 (index 로 치면 0 1 2 3개까지) 보겠다는 의미.
        print(sel)
        return

    else:
        for i in range(3):  # 각자의 depth 에서 화살표는 3개를 돌 기회를 가진다.
            if check[i] == 0:
                check[i] = 1
                sel[idx] = arr[i]
                perm(idx + 1)
                check[i] = 0

# 첫 번째 depth부터 시작
perm(0)

##################################################################
# 중복 순열

N = 3
arr = ['a', 'b', 'c']
sel = [0] * 3
# check = [0] * 3  사실이 경우 check 관련을 다 없애버리면 화살표가 멈추지 않아 중복이 자연스럽게 가능해진다.

def perm(depth):
    if depth == 3:
        print(sel)
        return

    else:
        for i in range(3):
            sel[depth] = arr[i]
            perm(depth + 1)

perm(0)

###################################################################
# 4P2 는 ??

N = 4
arr = ['a', 'b', 'c', 'd']
sel = [0] * 2
check = [0] * 4


def perm(depth):
    if depth == 2:
        print(sel)
        return

    else:
        for i in range(4):
            if check[i] == 0:
                sel[depth] = arr[i]
                check[i] = 1
                perm(depth + 1)
                check[i] = 0

perm(0)

##########################################################################
# 일반 조합 5C3 의 경우

N = 5  # 원래는 arr 의 len
R = 3  # 몇개 보여주고 싶냐의 차이

arr = ['a', 'b', 'c', 'd', 'e']  # 여기 떨어질 화살표가 idx
sel = [0] * R  # selection 의 idx(selection 쪽에 떨어지는 화살표 == sidx)


def combination(idx, sidx):  # 기본적으로 시작시 두개의 if 는 화살표가 리스트 밖으로 벗어나지 않기 위해서 해준다.
    if sidx == R:  # 이게 먼저 와야 하는 이유는? sel 이 지금 더 짧기 때문.
        print(sel)
        return
    if idx == N:  # 역시 이것도 범위를 벗어나 버리면 리턴해줘야 한다.
        return

    sel[sidx] = arr[idx]  # 재료 arr 의 화살표 위치의 문자를 sel 의 화살표 위치에 넣는다.
    combination(idx+1, sidx+1)  # 화살표가 각각 한칸씩 옆으로 이동함을 의미.
    combination(idx+1, sidx)  # 이경우라면 arr 쪽의 화살표만 한칸을 이동하게 됨.

combination(0, 0)