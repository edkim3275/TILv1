# Function Practice

1. ### [연습] 함수를 정의하고 값을 반환해봅시다.

   > 리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환하는 함수를 만들어주세요.

   ```python
   my_list_max([10, 3], [5, 9])
   ```

   ---

   ```
   예시 출력)
   [5, 9]
   ```

   ```python
   # sum 없이 푸는 풀이
   def my_list_max(a, b):
       # 먼저 각 요소의 합을 정의해준다
       add_a = 0
       add_b = 0
       for i in a:
           add_a += i
       for j in b:
           add_b += j
       # 각 요소의 합을 비교
       result = []
       if add_a > add_b:
           result = a
       elif add_a < add_b:
           result = b
       return result
   ```

   ```python
   # sum으로 풀이
   def my_list_max(a,b):
       sum_a = sum(a)
       sum_b = sum(b)
       result = []
       if sum_a > sum_b:
           result = a
       else:
   		result = b
       return result
   ```

2. 다음중 오류가 나는 코드는 무엇인가

   ```python
   def func(*args, prof, cnt=5):
       print(prof, args, cnt)
   func('익주', '명준', prof='남호', 7)
   # SyntaxError: positional argument follows keyword argument
   # 키워드인자를 사용할 경우 그 뒤에 위치인자가 올 수 없다.
   ```

   ```python
   def func(*args, prof, cnt=5):
       print(prof, args, cnt)
   func('익주', '명준', prof='남호')
   # 남호 ('익주', '명준') 5
   ```

   ```python
   def func(*args, prof, cnt=5):
       print(prof, args, cnt)
   func('익주', '명준', prof='남호', cnt=7)
   # 남호 ('익주', '명준') 7
   ```

3. 전체 정수 범위에서 최소값, 최대값 구하기

   ```python
   num_max(-1, -2, -4, 5, 7, 8, 516, 159, -65, -99, -74)
   num_min(-1, -2, -4, 5, 7, 8, 516, 159, -65, -99, -74)
   ```

   ```python
   def num_max(*args):
       fst = args[0]
       for i in args:
           if fst < i:
               fst = i
       return fst
   
   def num_min(*args):
       fst = args[0]
       for i in args:
           if fst > i:
               fst = i
       return fst
   ```

4. 다음 함수을 재귀함수로 만드시오.

   ```python
   # 입력예시
   # '1234' => 10
   # '1002003004005' => 15
   def add_num(string):
       total = 0
       idx = 0
       while idx < len(string):
           total += int(string[idx])  # str를 정수로 변환 후 계산한다.
           idx += 1
       return total
   add_num('1002003004005') #=> 15
   ```

   ```python
   # step1 역으로 계산되는 함수를 만들어본다.
   def add_num(string):
       total = 0
       idx = len(string)-1
       while idx >= 0:
           total += int(string[idx])
           idx -= 1
       return total
   add_num('1002003004005') #=> 15
   ```

   ```python
   # step2 역으로 계산된 함수를 재귀함수로 만들어본다.
   def recur_total(string):
       idx = len(string)-1
       if idx == 0:
           return int(string[idx])
       else:
           return recur_total(str(int(string)//10)) + int(string[idx])
       
   recur_total('352546')
   ```

   



