

T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    answer = 0
    p1_flag = False
    p2_flag = False
    R = 3
    sel = [0] * R
    for i in range(len(numbers)):
        if i % 2 == 0:
            player_1.append(numbers[i])
        elif i % 2:
            player_2.append(numbers[i])


    print(player_1)
    print(player_2)
