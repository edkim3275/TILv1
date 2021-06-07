T = int(input())
for tc in range(T):
    # n: 문서의 개수, m: 현재 문서의 위치
    n, m = map(int, input().split())
    priority_list = list(map(int, input().split()))
    queue = 1
    # 큐가 비어있을 때까지 진행
    while priority_list:
        # 가장 앞에있는 문서의 중요도 확인
        if priority_list[0] == max(priority_list):
            # 가장 큰 수라면, 찾고자 하는 수인지 확인
            if m == 0:
                print(queue)
                break
            # 큰 수는 맞지만, 찾고자 하는 수가 아니라면
            else:
                # 결과로 내보내기
                pop_num = priority_list.pop(0)
                queue += 1
                m -= 1
        # 큰 수가 아닌경우 뒤로 재배치
        else:
            # 큰 수가 아니지만 찾고자 하는 수였다면
            if m == 0:
                # 뒤로 재배치하면서 값 갱신
                pop_num = priority_list.pop(0)
                priority_list.append(pop_num)
                m = len(priority_list)-1
            else:
                # 큰 수도아니고, 찾고자 하는 수도 아니라면 뒤로 재배치
                pop_num = priority_list.pop(0)
                priority_list.append(pop_num)
                m -= 1
