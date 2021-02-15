arr = [[1,2,3,4],
       [5,6,7,8],
       [10,11,12,13]
       ]
N = 3
M = 4
# len(arr)
# len(arr[0])
# 행 우선순회 방식
for i in range(N):
    for j in range(M):
        print(arr[i][j])
# 행 우선순회를 역으로 돌아보자
for i in range(N):
    for j in range(M-1,-1,-1):
        print(arr[i][j])
# 열 우선순회 방식
for j in range(M):
    for i in range(N):
        print(arr[j][i])
