# list

## 1. 배열

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

### 1.1 배열의 필요성

- 예를 들어

  Num0 = 0; Num1 = 1; Num2 = 2; Num3 =3; 과 같은 자료를

  Num = [0, 1, 2, 3]과 같이 표현을 할 수 있다.

  변수가 무수히 많아질 경우 첫번째와 같은 표현은 어려울 수 있다.

- 프로그램 내에서 여러 개의 변수가 필요할 때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 매우 비효율적일 수 있다.
- 배열을 사용하면 하나의 선언을 통해서 둘 이상의 변수를 선언할 수 있다.
- 단순히 다수의 변수 선언을 의미하는 것이 아니라, 다수의 변수로는 하기 힘든 작업을 배열을 활용해 쉽게 할 수 있다.

### 1.2 1차원 배열

- 1차원 배열의 선언

  - 별도의 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성

  - 이름 : 프로그램에서 사용할 배열의 이름

    `Arr = list()` `Arr=[]`

- 1차원 배열의 접근
  - Arr[0] = 10; '배열 Arr의 0번째 원소에 10을 저장하라'
  - Arr[idx] = 10; '배열 Arr의 idx번째 원소에 10을 저장하라'
  - Arr[-1] = 10; '배열 Arr의 끝에서 1번째 원소에 10을 저장하라'

#### 1.2.1 연습문제 : Gravity

- 낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램 작성

- 중력은 회전이 완료된 후 적용

- 상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.

- 방의 가로 길이는 항상 100이며, 세로길이도 항상 100이다.(제한조건은 중요한 포인트!) 즉, 상자는 최소 0, 최대 100높이로 쌓을 수 있다.

  ![image-20210212164850205](list.assets/image-20210212164850205.png)

### 1.3 정렬

- 2개 이상의 자료를 특정 기준에 의해 작은 값부터 큰 값(오름차순 : ascending), 혹은 그 반대의 순서대로(내림차순 : descending) 재배열하는 것
- 키 : 자료를 정렬하는 기준이 되는 특정 값

#### 1.3.1 대표적인 정렬 방식의 종류

- 버블 정렬(Bubble Sort)
- 카운팅 정렬(Counting Sort)
- 선택 정렬(Selection Sort)
- 퀵 정렬(Quick Sort)
- 삽입 정렬(Insertion Sort) - 응용 part
- 병합 정렬(Merge Sort) - 응용 part

| 알고리즘 | 평균수행시간 | 최악수행시간 | 알고리즘기법 | 비고                                               |
| -------- | ------------ | ------------ | ------------ | -------------------------------------------------- |
| 버블     | O(n^2)       | O(n^2)       | 비교와 교환  | 코딩이 가장 손쉽다                                 |
| 카운팅   | O(n+k)       | O(n+k)       | 비교환 방식  | n이 비교적 작을 때만 가능                          |
| 선택     | O(n^2)       | O(n^2)       | 비교와 교환  | 교환의 회수가 버블, 삽입정렬보다 작다              |
| 퀵       | O(nlogn)     | O(n^2)       | 분할 정복    | 최악의 경우 O(n^2)이지만, 평균적으로는 가장 빠르다 |
| 삽입     | O(n^2)       | O(n^2)       | 비교와 교환  | n의 개수가 작을 때 효과적이다                      |
| 병합     | O(nlogn)     | O(nlogn)     | 분할 정복    | 연결리스트의 경우 가장 효율적인 방식               |

### 1.4 * 완전검색(Exhaustive Search) *

> 문제의 해법으로 생각할 수 있는 **모든 경우의 수를 나열해보고 확인**하는 기법.

- Brute-force 혹은 Generate-and-Test 기법이라고도 불리운다.
- 모든 경우의 수를 테스트한 후, 최종 해법을 도출한다.
- 일반적으로 경우의 수가 상대적으로 작을 때 유용하다.
- 모든 경우의 수를 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률이 작다.
  - 기본을 배우는 지금은 느리지만 정확도가높은 완전검색방법을 연습해야한다.
- 자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다.
- 동작 과정
  1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해집합(Solution Set)에 추가한다.
  2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지를 확인한다. 곧, 문제의 제약 조건을 위반하지 않는지를 검사한다.
  3. 해 검사 :새로운 부분해 집합이 문제의 해가 되는지를 확인한다. 아직 전체  문제의 해가 완성되지 않았다면 1의 해 선택부터 다시 시작한다.

### 1.5 탐욕(Greedy) 알고리즘

- 최적해를 구하는 데 사용되는 근시안적인 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달한다.
- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들엇다고 하여, 그것이 최적이라는 보장은 없다.
- 일반적으로, 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 된다.

## 2. 정렬

### 2.1 버블정렬(Bubble Sort)

> 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

- 정렬과정

  1. 우선 오름차순, 내림차순 중 어떤방식으로 정렬할지 정한다

  2. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동한다.

  3. 한 단게가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다.

  4. 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 모양과 같다고 하여 버블정렬이라고 한다.

- **시간복잡도 : O(n^2)**

```python
def BubbleSort(arr):  # 정렬할 list
    for i in range(len(arr)-1, 0, -1):  # 범위의 끝 위치지정
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

```python
def BubbleSort(arr):  # 정렬할 list
    for i in range(len(arr)-1, 0, -1):  # 범위의 끝 위치지정
        for j in range(1, i+1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
```

### 2.2 카운팅정렬(Counting Sort)

> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

- 선형시간? n번만에 정렬을 할 수 있다는 느낌

- 제한사항

  - 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능 : 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
  - 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야 한다.
  - 최대값이 적당히 큰 경우에 사용을 해야만 한다.

- **시간복잡도 : O(n+k)**

  - n은 리스트 길이, k는 정수의 최대값

- 과정

  1. 기존의 리스트 내의 가장 큰 정수를 확인한다.

  2. count 배열을 생성

     `count = [0] * (가장 큰 정수 + 1)`

  3. 기존 리스트 내의 정수의 개수 만큼 count배열을 갱신

  4. 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 count의 원소를 조정한다.

     ![image-20210212173041313](list.assets/image-20210212173041313.png)

  5. counts[1]을 감소시키고 Temp에 1을 삽입한다.

     ![image-20210212173357428](list.assets/image-20210212173357428.png)

- 안정정렬(stable sort)

  기존의 데이터를 훼손 시키지 않고, 요소들의 순서를 유지하면서 정렬이 가능해진다.

```python
def Counting_Sort(A, B, k)
# A [] -- 입력 배열(1 to k)
# B [] -- 정렬된 배열
# C [] -- 카운트 배열

C = [0] * (k+1)

for i in range(0, len(A)):  # counts배열
    C[A[i]] += 1
for i in range(1, len(C)):  # 누적합
    C[i] += C[i-1]
for i in range(len(A)-1, -1, -1):  # 정렬
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]
```

#### 2.2.1 연습문제 : Baby-gin Game

- 0 ~ 9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때, 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고, 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
- 그리고, 6장의 카드가 run과 triplet로만 구성된 경우를 baby-gin으로 부른다.
- 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라. 

- 입력 예
  - 667767은 두 개의 triplet이므로 baby-gin이다. (666, 777)
  - 054060은 한 개의 run과 한 개의 triplet이므로 baby-gin이다. (456, 000)
  - 101123은 한 개의 triplet이 존재하나, 023은 run이 아니므로 baby-gin이 아니다.

- 완전검색을 활용한 접근

  1. 고려할 수 있는 모든 경우의 수 생성하기

     6개의 숫자로 만들 수 있는 모든 숫자를 나열(중복포함)

     6!의 경우가 있는 순열을 생성

  2. 해답 테스트 하기

     앞의 3자리와 뒤의 3자리를 잘라서 run과 triplet여부를 테스트하고 최종적으로 baby-gin을 판단한다.

  - 순열(Permutation)

    서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것

    `nPr`과 같이 표현한다

    nPr = n * (n-1) * (n-2) * ... * (n-r+1)

    nPn = n!(n Factorial) = n * (n-1) * (n-2) * ... * 2 * 1

    - 예시 : {1, 2, 3}을 포함하는 모든 순열을 생성하는 함수

    - 원소의 개수만큼 for문이 만들어진다.

      ```python
      for i1 in range(1, 4):
          for i2 in range(1, 4):
              if i2 != i1:
                  for i3 in range(1, 4):
                      if i3 != i1 and i3 != i2:
                          print(i1, i2, i3)
      ```

      ```python
      N = 3
      card = [4, 5, 6]
      for i in range(N):
          for j in range(N):
          if i != j:
              for k in range(N):
                  if k != i and k != j:
                      print(card[i], card[j], card[k])
      ```

  - 순열을 통한 계산

    ```python
    N = 3
    card = [4, 5, 6]
    run = False
    tri = False
    for i in range(N):
        for j in range(N):
        if i != j:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])
                    # run 검사
                    if card[i]+1 == card[j] and card[i]+2 == card[k]:
                        run = True
                    # triplet 검사
                    if card[i] == card[j] and card[j] == card[k]:
                        tri = True
                    if run:
                        print("run")
                    if tri:
                        print("triplet")
    ```

- 완전검색이 아닌 접근

  - 6개의 숫자는 6자리의 정수 값으로 입력된다.
  - Counts 배열의 각 원소를 체크하여 run과 triplet 및 baby-gin여부를 판단한다.

  ```python
  num = 456789
  c = [0] * 12
  
  for i in range(6):
      c[num%10] += 1
      num //= 10
  ```

- 입력 받은 숫자를 정렬한 후, 앞뒤 3자리씩 끊어서 run 및 triplet을 확읺나느 방법을 고려할 수도 있다.
  - [6, 4, 4, 5, 4, 4] -> [4, 4, 4, 4, 5, 6] 확인 가능
  - [1, 2, 3, 1, 2, 3] -> [1, 1, 2, 2, 3, 3] 확인 불가능 한 경우도 존재
  - 이처럼 탐욕 알고리즘적인 접근은 해답을 찾아내지 못하는 경우도 있으니 유의해야만 한다.