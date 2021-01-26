# 불쌍한 달팽이
# 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. 
# (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
# 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 snail()을 작성하시오.
# 함수의 인자는 다음과 같다.
# 1. 기둥의 높이(미터)
# 2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
# 3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)
def snail(height, day, night):
    k = height / (day-night)
    return int(k)
print(snail(100, 6, 1))

# def snail(height, day, night):  # 3개의 인자를 받는다.
#     count = 0  # 얼마나 시간을 가야하는지
#     dif = 0  # snail의 이동거리
#     while dif < height:  # snail 이동거리가 height를 넘으면 종료
#         count += 1  # 1시간을 간다
#         dif += day  # 낮시간동안 이동한 거리를 더해준다
#         if dif >= height:  # 이동한 거리가 height를 넘으면
#             break  # 반복문을 종료
#         else:  # 그 외의 시간
#             dif -= night  # 밤시간동안 이동거리가 줄어든다
#     return count  # dif가 height를 넘을때까지의 시간 count를 반환
# print(snail(100, 5, 2))