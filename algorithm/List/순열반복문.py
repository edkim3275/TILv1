N = 3
card = [4, 5, 6]

# 반복문을 이용해서 작성

# run?
# triplet?
# 만들어 지면 출력이 되야하기때문에 False로 초기값을 정해 놓음
run = False
tri = False

for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])

                    # run을 검사(연속적인 수)
                    if card[i] + 1 == card[j] and card[i] + 2 == card[k]:
                        run = True

                    # tri 검사
                    if card[i] == card[j] and card[i] == card[k]:
                        tri = True

                    if run:
                        print("런")

                    if tri:
                        print("트리플")
