jongmal = ['0666', '1666', '2666', '3666', '4666',
           '5666', '6660', '6661', '6662', '6663',
           '6664', '6665', '6666', '6667', '6668',
           '6669', '7666', '8666', '9666'
           ]

n = int(input())
Q = n // 19
res = n % 19
# print(Q, res)
if Q == 0:
    if res == 0:
        print('666')
    else:
        print(jongmal[res-1])
else:
    print(str(Q*10)+jongmal[res-1])
