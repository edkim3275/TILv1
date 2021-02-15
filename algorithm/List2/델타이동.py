arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
r = 1
c = 1

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상하좌우
drc = [[-1,0], [1,0], [0,-1], [0,1]]

for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]

    print(arr[nr][nc])
