T = int(input())
for tc in range(T):
    r, s = input().split()
    n = len(s)
    for char in s:
        print(char*int(r), end='')
    print()