# 2번째부터 T까지의 숫자를 추출(인덱스로 사용)
for i in range(10):
    # test case에 대한 input()생성
    T = int(input())
    # 입력받은 정보를 list화
    numbers = list(map(int, input().split()))
    # 0,1번째는 00이니 2번째 숫자부터 시작
    for tc in range(2, T-2):
        # 결과 초기값 0
        ans = 0
        # 중간 과정을 담을 list
        part_lst = []
        # 두칸 전 숫자와의 차이가 양수라면
        if numbers[tc] - numbers[tc-2] > 0:
            # 그 차이만큼을 빈 리스트에 추가
            part_lst.append(numbers[tc] - numbers[tc-2])
            # 한칸 전 숫자와의 차이가 양수라면
            if numbers[tc] - numbers[tc-1] > 0:
                # 그 차이만큼을 빈 리스트에 추가
                part_lst.append(numbers[tc] - numbers[tc - 1])
                #  한칸 이후 숫자와의 차이가 양수라면
                if numbers[tc] - numbers[tc + 1] > 0:
                    # 그 차이만큼을 빈 리스트에 추가
                    part_lst.append(numbers[tc] - numbers[tc + 1])
                    #  두칸 이후 숫자와의 차이가 양수라면
                    if numbers[tc] - numbers[tc + 2] > 0:
                        # 그 차이만큼을 빈 리스트에 추가
                        part_lst.append(numbers[tc] - numbers[tc + 2])
        else:

        # 네 개의 차이값들이 들어가 있는 리스트에서 가장 작은 수를 결과값에 더해줍니다.
        ans += min(part_lst)

    print("#{} {}".format(i+1, ans))
