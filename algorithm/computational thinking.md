# computational thinking:desktop_computer:

> 수많은 세월 동안 정리해 둔 것이 "증명"기법이다. 
>
> 어떤 전공도 상식선에서 이해되는 분야는 없다.

---

## 0. 서론

### 목차

![image-20210407090853486](computational thinking.assets/image-20210407090853486.png)

이 중에서 간단한 것만 살펴보겠습니다.

---

### 프로그래밍과 논리/수학

![image-20210407091022251](computational thinking.assets/image-20210407091022251.png)

- 예제1(카드 문제)

  ![image-20210407091521754](computational thinking.assets/image-20210407091521754.png)

  답 : D, 7

  ![image-20210407091551829](computational thinking.assets/image-20210407091551829.png)

- 예제2(맥주집 문제)

  ![image-20210407091633156](computational thinking.assets/image-20210407091633156.png)

  20세 이하인 사람, 맥주마시는 사람 확인을 하면 된다.

  ![image-20210407091723359](computational thinking.assets/image-20210407091723359.png)

  ![image-20210407091821086](computational thinking.assets/image-20210407091821086.png)

- 예제3

  ![image-20210407091846018](computational thinking.assets/image-20210407091846018.png)

  ![image-20210407091859025](computational thinking.assets/image-20210407091859025.png)

  inclusive or 둘중 하나가 반드시 필요한 것

  exclusive or 둘중 하나만 선택

  ![image-20210407125022984](computational thinking.assets/image-20210407125022984.png)

![image-20210407092008026](computational thinking.assets/image-20210407092008026.png)

![image-20210407092035562](computational thinking.assets/image-20210407092035562.png)

- 참고

  명제 : 참이나 거짓을 알 수 있는 식이나 선언적 문장

  ![image-20210407092158642](computational thinking.assets/image-20210407092158642.png)

  ![image-20210407092345067](computational thinking.assets/image-20210407092345067.png)

  논리곱(Conjunction)

  ![image-20210407092437240](computational thinking.assets/image-20210407092437240.png)

​	![image-20210407092642182](computational thinking.assets/image-20210407092642182.png)

![image-20210407092903945](computational thinking.assets/image-20210407092903945.png)

**조건은 True이지만 결론이 False인 경우에만 명제가 거짓이 된다.**

**결과가 True이면 조건은 상관없이 True가 된다.**

![image-20210407092936717](computational thinking.assets/image-20210407092936717.png)

![image-20210407093337912](computational thinking.assets/image-20210407093337912.png)

![image-20210407093621336](computational thinking.assets/image-20210407093621336.png)

![image-20210407094145694](computational thinking.assets/image-20210407094145694.png)

**원래 조건명제와 대우명제는 서로 진리값이 같다.**

![image-20210407094455574](computational thinking.assets/image-20210407094455574.png)

1. F -> ? : 알 수 없다
2. ? -> T : True

![image-20210407094747478](computational thinking.assets/image-20210407094747478.png)

조건p가 False면 진리값은 항상 True

사실 상식적으로는 관련이 없어 보이는데 명제식은 상식에 상관없이 이렇게 수학적으로만 고려하면 되는 것

![image-20210407100903135](computational thinking.assets/image-20210407100903135.png)

### 증명

![image-20210407101305125](computational thinking.assets/image-20210407101305125.png)

![image-20210407101907214](computational thinking.assets/image-20210407101907214.png)

![image-20210407101914100](computational thinking.assets/image-20210407101914100.png)

![image-20210407102345399](computational thinking.assets/image-20210407102345399.png)

- Trivial Proof : 모든 x에대해서 P(x) -> Q(x)를 증명하는데, Q(x)가 항상 참인 경우를 보이는 증명을 Trivial Proof라고 한다.

  ![image-20210407102529920](computational thinking.assets/image-20210407102529920.png)

  간접증명 : 대우를 이용한 증명

  1. x^2은 항상 0보다 크므로 True
  2. 2로 묶이므로(2의 배수이므로) 짝수

- Vacuous Proof(공허한 증명) : 모든 x에 대해서 P(x) -> Q(x)를 증명하는데, P(x)가 항상 거짓인 경우를 보이는 증명을 Vacuous Proof라고 한다.

  ![image-20210407103212952](computational thinking.assets/image-20210407103212952.png)

  1. 2x^2-4x+4= 2(x-1)^2+2는 항상 양수 이므로 명제가 거짓, 따라서 진리값은 True
  2. 2(2n^3+3n^2+5)+1은 홀수

---

## 1. 논리와 증명

![image-20210407103744853](computational thinking.assets/image-20210407103744853.png)

항진명제 : 항상 참이되는 명제

![image-20210407104130428](computational thinking.assets/image-20210407104130428.png)

![image-20210407104411844](computational thinking.assets/image-20210407104411844.png)

모순명제 : 항상 거짓이되는 명제

![image-20210407104601978](computational thinking.assets/image-20210407104601978.png)

![image-20210407104701954](computational thinking.assets/image-20210407104701954.png)

두 명제가 동등하다? 진리값이 같다

![image-20210407104816308](computational thinking.assets/image-20210407104816308.png)

![image-20210407104905091](computational thinking.assets/image-20210407104905091.png)

1. 실수집합의 모든 원소에대해서(모든 실수에대해서), x^2은 x이상이다.

   만족하지 않는 반례를 하나 보이면 증명이 된다. 0<x<1인 경우 만족하지 못한다

![image-20210407110233618](computational thinking.assets/image-20210407110233618.png)

![image-20210407110435811](computational thinking.assets/image-20210407110435811.png)

![image-20210407110445977](computational thinking.assets/image-20210407110445977.png)

대우를 증명하는 것이 간접증명방식

![image-20210407110517287](computational thinking.assets/image-20210407110517287.png)

![image-20210407110654902](computational thinking.assets/image-20210407110654902.png)

---

## 2. 수와 표현

![image-20210407110742067](computational thinking.assets/image-20210407110742067.png)

![image-20210407111437451](computational thinking.assets/image-20210407111437451.png)

![image-20210407111704231](computational thinking.assets/image-20210407111704231.png)

![image-20210407112121287](computational thinking.assets/image-20210407112121287.png)

![image-20210407112501583](computational thinking.assets/image-20210407112501583.png)

![image-20210407112725392](computational thinking.assets/image-20210407112725392.png)

![image-20210407112730466](computational thinking.assets/image-20210407112730466.png)

![image-20210407112943140](computational thinking.assets/image-20210407112943140.png)

![image-20210407140450076](computational thinking.assets/image-20210407140450076.png)



![image-20210407140521226](computational thinking.assets/image-20210407140521226.png)



![image-20210407140533574](computational thinking.assets/image-20210407140533574.png)

![image-20210407140733307](computational thinking.assets/image-20210407140733307.png)

## 3. 집합과 조합론

![image-20210407140902610](computational thinking.assets/image-20210407140902610.png)

![image-20210407141031839](computational thinking.assets/image-20210407141031839.png)

![image-20210407160256514](computational thinking.assets/image-20210407160256514.png)

![image-20210407141330220](computational thinking.assets/image-20210407141330220.png)



![image-20210407141814881](computational thinking.assets/image-20210407141814881.png)

![image-20210407160552107](computational thinking.assets/image-20210407160552107.png)

![image-20210407160708333](computational thinking.assets/image-20210407160708333.png)

![image-20210407160734732](computational thinking.assets/image-20210407160734732.png)

![image-20210407143707980](computational thinking.assets/image-20210407143707980.png)

q가 공집합이 아닌경우를 생각해서 그때의 p가 존재하지 않는 것을 증명하면 된다.

![image-20210407160912818](computational thinking.assets/image-20210407160912818.png)

![image-20210407161218276](computational thinking.assets/image-20210407161218276.png)



![image-20210407161244328](computational thinking.assets/image-20210407161244328.png)

![image-20210407144233766](computational thinking.assets/image-20210407144233766.png)

## 4. 기초 수식

![image-20210407161304189](computational thinking.assets/image-20210407161304189.png)

![image-20210407161549833](computational thinking.assets/image-20210407161549833.png)

![image-20210407161705637](computational thinking.assets/image-20210407161705637.png)

![image-20210407161733734](computational thinking.assets/image-20210407161733734.png)

위 같은 경우 nlogn걸릴 수 있다 

![image-20210407161956675](computational thinking.assets/image-20210407161956675.png)

![image-20210407162025996](computational thinking.assets/image-20210407162025996.png)



![image-20210407162130653](computational thinking.assets/image-20210407162130653.png)

![image-20210407162352723](computational thinking.assets/image-20210407162352723.png)

![image-20210407162654296](computational thinking.assets/image-20210407162654296.png)



![image-20210407162717478](computational thinking.assets/image-20210407162717478.png)

---

## 5. 재귀

![image-20210407162756197](computational thinking.assets/image-20210407162756197.png)

![image-20210407162805379](computational thinking.assets/image-20210407162805379.png)

![image-20210407162823904](computational thinking.assets/image-20210407162823904.png)

![image-20210407162831785](computational thinking.assets/image-20210407162831785.png)

![image-20210407162852842](computational thinking.assets/image-20210407162852842.png)

![image-20210407162902441](computational thinking.assets/image-20210407162902441.png)

![image-20210407162920989](computational thinking.assets/image-20210407162920989.png)

![image-20210407162932498](computational thinking.assets/image-20210407162932498.png)

![image-20210407163015978](computational thinking.assets/image-20210407163015978.png)











## 웹엑스

### 문제1 ∨

![image-20210407130040303](computational thinking.assets/image-20210407130040303.png)

| p    | q    | ~p   | (~p∧q) | ~(~p∧q) | ~(~p∧q)∨q |
| ---- | ---- | ---- | ------ | ------- | --------- |
| T    | T    | F    | F      | T       | T         |
| T    | F    | F    | F      | T       | T         |
| F    | T    | T    | T      | F       | T         |
| F    | F    | T    | F      | T       | T         |

항진명제

| p    | q    | ~p   | (~p∨q) | ~q   | (p∧~q) | (~p∨q)∨(p∧~q) |
| ---- | ---- | ---- | ------ | ---- | ------ | ------------- |
| T    | T    | F    | T      | F    | F      | T             |
| T    | F    | F    | F      | T    | T      | T             |
| F    | T    | T    | T      | F    | F      | T             |
| F    | F    | T    | T      | T    | F      | T             |

항진명제

### 문제2

![image-20210407130844640](computational thinking.assets/image-20210407130844640.png)

| p    | q    | (p∧q) | ~q   | (p∧~q) | (p∧q)∧(p∧~q) |
| ---- | ---- | ----- | ---- | ------ | ------------ |
| T    | T    | T     | F    | F      | F            |
| T    | F    | F     | T    | T      | F            |
| F    | T    | F     | F    | F      | F            |
| F    | F    | F     | T    | F      | F            |

∨ ∧

### 문제3

![image-20210407131352882](computational thinking.assets/image-20210407131352882.png)

| p    | q    | ~p   | ~q   | ~p∨~q | ~(p∨q) |
| ---- | ---- | ---- | ---- | ----- | ------ |
| T    | T    | F    | F    | F     | F      |
| T    | F    | F    | T    | T     | F      |
| F    | T    | T    | F    | T     | F      |
| F    | F    | T    | T    | T     | T      |

동등하지 않다

### 문제4

![image-20210407132012599](computational thinking.assets/image-20210407132012599.png)

![image-20210407132617606](computational thinking.assets/image-20210407132617606.png)

∨ ∧

(~q)

### 문제5 ∈ ∀ ∃

![image-20210407132724791](computational thinking.assets/image-20210407132724791.png)

1. ∀x ∈ R, x^2 >= x : 거짓
2. ∀x ∈ Z, x^2 >= x : 참
3. ∃x ∈ R, x^2 < x : 참
4. ∃x ∈ Z, x^2 < x : 거짓, 모든경우에 x^2 > x

### 문제7

![image-20210407133758652](computational thinking.assets/image-20210407133758652.png)

n = 2k + 1

n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 1 + 2k + 1 = 4k² + 6k + 2 = 2(2k²+3k+1)

따라서 n이 홀수이면 n² + n은 짝수

![image-20210407134226543](computational thinking.assets/image-20210407134226543.png)

### 문제9

![image-20210407134506338](computational thinking.assets/image-20210407134506338.png)





### 💎머지소트

- 교재 분할정복, 백트래킹 부분

![image-20210407163423349](computational thinking.assets/image-20210407163423349.png)

![image-20210407163441712](computational thinking.assets/image-20210407163441712.png)

#### 문제1

![image-20210407163515886](computational thinking.assets/image-20210407163515886.png)

![image-20210407163635329](computational thinking.assets/image-20210407163635329.png)

![image-20210407163743204](computational thinking.assets/image-20210407163743204.png)

쪼갰다가 다시 합치는 과정

버블 선택정렬, 카운팅정렬 최악의 경우은 n^2이지만 병합정렬은 nlogn시간복잡도를 가진다.

![image-20210407163908200](computational thinking.assets/image-20210407163908200.png)

![image-20210407164155427](computational thinking.assets/image-20210407164155427.png)

퀵정렬은 분할하면서 내려가면서 정렬

병합정렬은 일단 모두 분할하고나서 합하면서 올라오면서 정렬

#### 예제

![image-20210407171528711](computational thinking.assets/image-20210407171528711.png)



![image-20210407172901038](computational thinking.assets/image-20210407172901038.png)

![image-20210407173414193](computational thinking.assets/image-20210407173414193.png)

![image-20210407173644200](computational thinking.assets/image-20210407173644200.png)



![image-20210407173842310](computational thinking.assets/image-20210407173842310.png)

왼쪽 사이드를 먼저 분할을 하고나서 합하면서 올라오고, 오른쪽 사이드를 분할 합하면서 올라오고의 느낌으로 분할하게 됩니다 



















---

![image-20210407164845613](computational thinking.assets/image-20210407164845613.png)

![image-20210407164930989](computational thinking.assets/image-20210407164930989.png)

리스트 큐가아닌 인덱스 활용하는 것을 추천(아니면 시간초과 날수도)

**merge sort를 시간을 할애해가면서 설명을 하는 이유가 있을겁니다.**

### 재귀  문제2

![image-20210407165535323](computational thinking.assets/image-20210407165535323.png)

위로 부터 식을 하나 뽑아내고 그것을 증명하여 시간복잡도를 계산한다.

O(nlogn)이 나오는지 확인해볼 것

## 과제

논리와 증명 12 수와 표현 4 집합과 조합론 16

### 논리와 증명12

![image-20210407134416887](computational thinking.assets/image-20210407134416887.png)

n은 정수범위라고 생각하고 푸세요

대우 : n이 3의 배수가 아니라면 n²은 3의 배수가 아니다

if n = 3k+1

n² = (3k+1)² = 9k² + 6k + 1 = 3(3k² + 2k) + 1

if n = 3k + 2

n² = (3k+2)² = 9k² + 12k + 4 = 3(3k² + 4k + 1) + 1

대우가 참이므로 명제도 참

### 수와 표현4

![image-20210407170216781](computational thinking.assets/image-20210407170216781.png)

(logy + logz) / loga

### 집합과 조합론16

![image-20210407170227128](computational thinking.assets/image-20210407170227128.png)



## 퀵정렬

```python
def quicksort(array):
  if len(array) < 2:
    # 배열의 길이가 0 이나 1이면 더이상 정렬하지 않아도 된다.
    return array
  else:
    # 계속 재귀 돌릴 곳
    pivot = array[0]
    # pivot 보다 작은 원소들의 모음집
    less = [i for i in array[1:] if i <= pivot]
    # pivot 보다 큰 원소들의 모음집
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
```

---

## 210408 

논리 9 11

수와표현 2 3-2 3-4 5-2

집합과 조합론 3 10 13

기초수식 2 4 6 

재귀 2

동적프로그래밍 1



과제 : 기초수식8 / 동적프로그래밍 2 / 심심하면 재귀 6

## 210409

<img src="computational thinking.assets/image-20210409090449117.png" alt="image-20210409090449117" style="zoom:100%;" />

![image-20210409090758780](computational thinking.assets/image-20210409090758780.png)

- 문제3

  드모르강 법칙이라는게 있다.

  ![image-20210409090933399](computational thinking.assets/image-20210409090933399.png)

  ![image-20210409091114313](computational thinking.assets/image-20210409091114313.png)

- 문제4

  분배법칙이 성립한다.

  ![image-20210409091352371](computational thinking.assets/image-20210409091352371.png)

- 문제5

![image-20210409091719445](computational thinking.assets/image-20210409091719445.png)

- 문제7

  ![image-20210409092348345](computational thinking.assets/image-20210409092348345.png)

- 문제9

  ![image-20210409092912409](computational thinking.assets/image-20210409092912409.png)

- 문제11

  ![image-20210409093304849](computational thinking.assets/image-20210409093304849.png)

### 수와표현

![image-20210409093730699](computational thinking.assets/image-20210409093730699.png)

![image-20210409094127293](computational thinking.assets/image-20210409094127293.png)

![image-20210409095020806](computational thinking.assets/image-20210409095020806.png)

## 과목평가(월)

2시간 => 4문제

1, 2, 3 코드직접 짜는문제 : 2문제 이상 풀어야만 패스

4 : 서술형(Comtational Thinking)

공부 : 배열, 탐색(그래프, bfs, bfs, 2차원배열), 이진순회

주석은 엄청 세세하게 달 필요는 없습니다.

연습문제 : 2차원배열, 델타를 이용해서 순회하는 방법, 2진순회하는 법

문제를 자세히 읽어보고 풀어보자

## 다음주

본격적인 응용과정의 시작

월을 시작으로 완전탐색, 그리디(자세히 할지 안할지 아직모르겠음), 분할정복, 백트래킹, 그래프에 대한 이론(인접행렬, 인접리스트, dfs, bfs), 최소가중치(MST, 크루스칼, 프림, 다익스트라)