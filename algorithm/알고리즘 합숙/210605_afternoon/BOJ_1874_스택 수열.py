n = int(input())
stack = []
ans_lst = []
flag = 1
var = 1

for i in range(n):
    num = int(input())
    # 스택안에 해당하는 수가 없는 경우 => 추가
    if num not in stack:
        while var <= num:
            stack.append(var)
            ans_lst.append('+')
            var += 1
        stack.pop()
        ans_lst.append('-')
        continue
    # 스택안에 해당하는 수가 있지만 마지막에 없는경우 => 불가
    if num in stack:
        if num != stack[-1]:
            flag = 0
            break
        elif num == stack[-1]:
            stack.pop()
            ans_lst.append('-')
            continue

if flag:
    for i in range(len(ans_lst)):
        print(ans_lst[i])
else:
    print('NO')
