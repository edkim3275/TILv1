A = [0, 4, 1, 3, 1, 2, 4, 1]
# 최대값 구하기 ###
max_value = -1
for i in A:
    if max_value < i:
        max_value = i
# 최대값의 개수만큼 box를 생성, 갱신
C = [0]*(max_value+1) ###
for i in A:
    C[i] += 1
# box 누적합
for i in range(1, len(C)):
    C[i] += C[i-1]
# temp list 갱신
B = [0]*(len(A))
for i in range(len(A)-1, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]
print(B)