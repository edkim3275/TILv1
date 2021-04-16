M = 5
A = [1,2,3,4,5]
for i in range(0, M-3+1):
    for j in range(i+1, M-2+1):
        for k in range(j+1, M-1+1):
            # print(A[i], A[j], A[k])
            print(i, j, k)
