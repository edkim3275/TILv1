N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
for i in range(M):
    if M_lst[i] in N_lst:
        print(1)
    else:
        print(0)
