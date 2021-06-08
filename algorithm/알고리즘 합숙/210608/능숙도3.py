def call(munja, idx):
    if idx == len(munja):
        for i in range(idx):
            print(munja[i], end='')
        print()
        for j in range(idx-1, -1, -1):
            print(munja[j], end='')
        return
    else:
        call(munja, idx+1)


# asadadas
string = input()
call(string, 0)