while True:
    num = input()
    if num == '0':
        break
    reverse_num = ''
    answer = 'no'
    for i in range(len(num)-1, -1, -1):
        reverse_num += num[i]
    if num == reverse_num:
        answer = 'yes'
    print(answer)
