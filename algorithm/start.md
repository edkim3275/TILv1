# start

- 일정 수준이 되지않으면 쓸모없는 프로그래밍이 될 수 있기 때문에 일정 수준까지 올라올 필요가 있다.
- ![image-20210412125208315](start.assets/image-20210412125208315.png)
- ![image-20210412125541139](start.assets/image-20210412125541139.png)

- 빅오, 빅오메가, 빅쎄타(빅오, 빅오메가 표기가 같은 경우)

- ![image-20210412115313669](start.assets/image-20210412115313669.png)

- ![image-20210412115627665](start.assets/image-20210412115627665.png)

  ```python
  import sys
  sys.stdin = open("input.txt", "r")
  sys.stdout = open("output.txt", "w")
  
  text = input()
  print(text)
  ```

- ![image-20210412140711231](start.assets/image-20210412140711231.png)

  - `&` : 특정 비트를 0으로 만들 때 사용
  - `|` : 특정 비트를 1로 만들 때 사용
  - `^` : 비트 반전, 검사에 사용

- ![image-20210412142005194](start.assets/image-20210412142005194.png)

- ![image-20210412144041149](start.assets/image-20210412144041149.png)

- ![image-20210412144205176](start.assets/image-20210412144205176.png)

- 메모리 주소는 한 바이트마다 저장이 된다.

- ![image-20210412144352978](start.assets/image-20210412144352978.png)

- 4개의 비트를 a가 사용하는 건데

- ![image-20210412144627068](start.assets/image-20210412144627068.png)

- ![image-20210412144718039](start.assets/image-20210412144718039.png)

  낮은 자리 검사했을때, 

  ![image-20210412144902157](start.assets/image-20210412144902157.png)

  ![image-20210412150805386](start.assets/image-20210412150805386.png)

  ![image-20210412151349305](start.assets/image-20210412151349305.png)

- ![image-20210412151606353](start.assets/image-20210412151606353.png)

- ![image-20210412152357113](start.assets/image-20210412152357113.png)

- ![image-20210412152824073](start.assets/image-20210412152824073.png)

  1111 의 경우 다 뒤집고 나서 1을 더하고 -를 붙이면 -1이 된다.

- ![image-20210412153659077](start.assets/image-20210412153659077.png)
- 















## 웹엑스 시간

- 문제 해결 과정

  ![image-20210412130731965](start.assets/image-20210412130731965.png)

  ​	처음 접근 할때 이해하고 잘 기획하는 것이 중요

![image-20210412130849712](start.assets/image-20210412130849712.png)

![image-20210412131045016](start.assets/image-20210412131045016.png)

```python
print(27&6)  # 2
```

![image-20210412131748199](start.assets/image-20210412131748199.png)

`<<`  : 배수

`>>` : 나누기

![image-20210412131958341](start.assets/image-20210412131958341.png)

`>>>` : 오른쪽으로 옮겨도 1이 유지되는

![image-20210412132456324](start.assets/image-20210412132456324.png)

- 2의 보수법

  컴퓨터 음수를 표현하는데 2의 보수법 방식을 사용

  맨 앞에있는 비트를 부호비트로 사용

- ![image-20210412163527994](start.assets/image-20210412163527994.png)

### 연습문제 1

![image-20210412163736180](start.assets/image-20210412163736180.png)



### 연습문제2

![image-20210412164119667](start.assets/image-20210412164119667.png)

0F97A3 => 2진법 => 7자리씩 묶어서 출력

A : 1010, B : 1011 이렇게 정의해도되고, 정의하지 않아도 되고. 여러가지 방법으로 시도해 보시길

### 연습문제3

![image-20210412164422791](start.assets/image-20210412164422791.png)

### Reviews

![image-20210412171216087](start.assets/image-20210412171216087.png)

일반적으로 32자리의 비트를 가지고 수를 표현을 합니다. 근데 우리는 8자리만 떼와서 보는 것

![image-20210412171401073](start.assets/image-20210412171401073.png)

이렇게 다 표현하면 더러우니까 16진수로 8자리로 표현하게 됩니다.

![image-20210412171613406](start.assets/image-20210412171613406.png)

- ![image-20210412172138720](start.assets/image-20210412172138720.png)

16진수로 2칸씩이니까 각각 8칸씩이다.

![image-20210412172355190](start.assets/image-20210412172355190.png)

![image-20210412172422125](start.assets/image-20210412172422125.png)

- 엔디안은 지금 중요한 것은 아니지만 한번 찾아보시길
  - 엔디안에대해서 공부를 해오고 내일 같이 공부해봅시다
- 음수표현방법

## 210413

### 오늘할꺼

- programming advanced

![image-20210413091722374](start.assets/image-20210413091722374.png)

- 과제(단순 2진 암호코드)



### 연습문제1

![image-20210413091107517](start.assets/image-20210413091107517.png)

### 연습문제2

![image-20210413101259917](start.assets/image-20210413101259917.png)