# def permutation(idx):
#     if idx == 3:
#         print(sel)
#     else:
#         for i in range(n):
#             if check[i] == 0:
#                 sel[idx] = arr[i]
#                 check[i] = 1
#                 permutation(idx+1)
#                 check[i] = 0
#
#
# arr = ['유린기', '볶음밥', '짬뽕']
# n = len(arr)
# sel = [0]*3
# check = [0]*n
# permutation(0)

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