arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]
n = len(arr)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(5):
       for j in range(5):
              temp = 0
              for k in range(4):
                     nr = i + dr[k]
                     nc = j + dc[k]

                     if nr<0 or nr>=n or nc<0 or nc>=n: continue
                     if arr[i][j] - arr[nr][nc] < 0:
                            temp += -(arr[i][j] - arr[nr][nc])
                     else:
                            temp += arr[i][j] - arr[nr][nc]
              print(temp, end=" ")

