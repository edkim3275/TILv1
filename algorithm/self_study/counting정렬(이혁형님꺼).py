# counting sort 구현

original_list = [0, 4, 1, 3, 1, 2, 4, 1]
sorted_list = [0]*(len(original_list))
count_list = [0]*(max(original_list)+1) # 최댓값이 4니까 리스트 길이 자체는 5여야함. 0포함하니까.
accumulated_list = []
accumulated_count = 0

for num in original_list: # 카운트 list에 집계해 보자
    count_list[num] += 1

for i in count_list:
    accumulated_count += i
    accumulated_list.append(accumulated_count)

print(count_list)
print(accumulated_list)

for j in range(len(original_list)-1, -1, -1): # 오리지날 리스트의 뒤부터 0번인덱스까지 뽑을건데
    x = original_list[j]  # 처음에 오리지널 리스트의 7번 인덱스 값인 x = 1
    sorted_list[(accumulated_list[x])-1] = x  # j의 처음이 1인데 1이 튀어나오면 그 '1' 은
    accumulated_list[x] -= 1  # 1이 나왔으니까 1 패밀리의 인덱스 하나 깎고

print(sorted_list)