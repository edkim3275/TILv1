# input()은 기본적으로 문자열
tmp = input()
print(tmp, type(tmp))
# 정수를 입력 받는 경우
N = int(input())
# 4 5 6 을 받는다면?
# 어떻게 관리 할 것이냐에 따라서 달라집니다.

# 1 공백을 기준으로 우선 쪼개고 나서 정수형(int)으로 바꾸자
# a, b, c라는 변수에 저장
a, b, c =  map(int, input().split())

# 2 이런식으로 가장많이 작성을 합니다.
# input을 받아서 하나의 리스트로 처리
arr = list(map(int, input().split()))

# 예를들어 가,나,다 라는 입력이 주어졌을때
tmp = input().split()
print(tmp)
# 이것은 ['가,나,다']가 되는데
tmp = input().split(",")
print(tmp)
# 이것은 ['가', '나', '다']가 됩니다.
# 나를 기준으로 나누게 되면??
tmp = input().split("나")
print(tmp)
# ['가,', ',다']가 됩니다.

# 3 붙어서 오는것을 찢고싶은경우 list를 사용해 줍니다.
# 가나다라
tmp = list(input())
print(tmp)

# 아래와 같은 입력을 쪼개서 정수형으로 바꾸려면?
# 12341512
tmp = list(input())
print(tmp)
# 지금은 리스트내부에 있는 요소들이 문자형이 되버림
# 따라서 이런식으로 해줍니다.
tmp = list(map(int, input()))
print(tmp)

# ---- 여기가지는 1차원 입력받기 -------

