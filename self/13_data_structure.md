## 1. 문자열
### 1.1 조회/탐색

`.find(x)` : x의 첫번째 위치를 반환. 없으면 `-1`을 반환

`.index(x)` : x의 첫번째 위치를 반환. **없으면 오류**발생

### 1.2 값 변경

`.replace(old, new[, count])` : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환. count지정시 해당 갯수만큼 시행

`.stirp([chars])` : 특정 문자들을 지정하면 그 문자들로 만들 수있는 모든 조합들을 양쪽에서 제거해 가면서 그 외의 문자가 나오면 멈춤.
                    지정하지 않으면 공백을 제거
                    
`.lstrip()`, `.rstrip()`
                    
`'seperator'.join(iterable)` : 특정한 문자열로 만들어 반환

### 1.3 문자 변형

`.capitalize()` : 앞글자를 대문자로 만들어 반환

`.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환

`.upper()` : 모두 대문자로 만들어 반환

`.lower()` : 모두 소문자로 만들어 반환

`.swapcase()` : 대<->소문자로 변경하여 반환

`.isalpha()`, `.isdecimal()`, `.isnumeric()`, `.isdigit()`, `.isspace()`, `.isupper()`, `.istitle()`, `.islower()`

## 2. 리스트
### 2.1 값 추가 및 삭제

`.append(x)`: 리스트에 값을 추가

`.extend(iterable)` : 리스트에 iterable(list, range, tuple, string(**[주의]**) 값을 붙일 수 있음

`.insert(i, x)` : 정해진 위치 `i`번지에 값을 추가 **[주의]** 맨 뒤 추가시 `len()`사용

`.remove(x)` : 리스트에서 값이 x인 것 한개를 삭제합니다. **[주의]** 여러개 한번에 삭제 불가, **값이 없으면 오류**

`.pop(i)` : 정해진 위치 `i`번지에 있는 값을 삭제. 그 항목을 반환. 지정 되지 않으면 마지막 항목을 삭제하고 삭제한 값을 반환

`.clear()` : 원본 리스트의 모든 항목을 삭제

### 2.2 탐색 및 정렬

`.index(x)` : x값을 찾아 해당 index값을 반환. **찾는 값이 없을시 오류**

`.count(x)` : 원하는 값의 개수를 확인. 원하는 값이 없다면 0

`.sort()` : 정렬. `sorted()`와는 다르게 원본 list를 변형시키고, `None`을 반환

`.reverse()` : 반대로 뒤집습니다. (정렬아님) 인덱스를 반대로 한다는 말이지 오름차순, 내림차순은 아니다.

## 3. 세트
### 3.1 추가 및 삭제

`.add(elem)` : elem을 세트에 추가 **[주의]** 추가하는 위치가 순서가 없다

`.update(*others)` : 여러가지 값을 추가. 인자로는 반드시 iterable 데이터 구조를 전달 **[주의]** 문자열 추가지 char단위로 추가됨

`.remove(elem)` : elem을 세트에서 삭제하고, **없으면 KeyError 발생** 특정값 삭제

`.discard(elem)` : elem을 세트에서 삭제하고, 없어도 에러가 발생하지 않는다.

`.pop()`: 임의의 원소를 제거해 반환합니다.

## 4. 딕셔너리
### 4.1 조회

`.get(key[, default])` : key를 통해 value를 가져옵니다. **절대로 KeyError가 발생하지 않는다.** **default는 None**

### 4.2 추가 및 삭제

`.pop(key[, default])` : key가 딕셔너리에 있으면 제거하고 그 값을 반환. 그렇지 않으면 default를 반환. default가 없는 상태에서 딕셔너리
                         에 없으면 KeyError가 발생
                         
`.update()` : 값을 제공하는 key, value로 덮어씁니다.

## 5. 데이터 구조에 적용가능한 Built-in-Function

### 3.1 map(function, iterable)

- 파이썬 3대 `or`

  - generator, iterator, decorator

  - 이 중에서 map은 generator(a.k.a 젤리키트)

    ```python
    m = map(str, [1, 2, 3])  #=> '1', '2', '3'
    list(m)  # list맛 젤리를 만드는 것
    tuple(m)  # tuple맛 젤리를 만드는 것
    ```

    

### 3.2 filter(function, iterable)

- iterable에서 function의 반환된 결과가 `True`인 것들만 구성하여 반환

- `filter object`를 반환

  ```python
  def odd(n):
      return n % 2
  numbers = [1, 2, 3, 4, 5]
  # odd함수를 numbers에 적용하여 필터
  new_numbers = filter(odd, numbers)  #=> <filter at 0x1c4d67bc280> 반환
  list(filter(odd, numbers))  #=> list로 형변환하여 [1, 3, 5]로 변환
  ```

  

### 3.3 zip(*iterables)