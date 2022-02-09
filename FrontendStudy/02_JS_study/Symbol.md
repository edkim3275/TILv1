# 33. Symbol

## 33.1. 심벌이란?

- 97년 자바스크립트가 ESMAScript로 표준화된 이래로 자바스크립트에는 6개의 타입(문자열, 숫자, 불리언, `undefined`, `null`, 객체) 타입이 존재했었다.

- `Symbol`은 ES6에서 도입된 7번째 데이터 타입

- **변경 불가능한 원시 타입의 값**

- **다른 값과 중복되지 않는 유일무이한 값** => 주로 충돌 위험이 없는 유일한 프로퍼티 키를 만들기 위해 사용

  :grey_exclamation: 프로퍼티 키로 사용할 수 있는 값은 빈 문자열을 포함하는 모든 문자열 또는 심벌 값이다

## 33.2. 심벌값의 생성

### 33.2.1. Symbol함수

- 심벌 값은 Symbol 함수를 호출하여 생성

  ```javascript
  const mySymbol = Symbol();
  ```

- 심벌 값은 외부로 노출되지 않아 확인할 수 없다

  ```javascript
  console.log(mySymbol); // Symbol()
  ```

- 생성자 함수로 객체를 생성하는 방식과는 달리 `new` 연산자와 함께 호출하지 않는다.

  ```javascript
  new Symbol(); // TypeError: Symbol is not a constructor
  ```

  - `new`연산자와 함께 함수 또는 클래스를 호출하면 객체(인스턴스)가 생성되지만 심벌 값은 변경 불가능한 원시 값이다.

- Symbol 함수에는 선택적으로 문자열을 인수로 전달가능

  ```javascript
  const mySymbol = Symbol('mySymbol');
  ```

  - 문자열은 심벌 값에 대한 description(심벌 값 생성에 어떠한 영향도 주지 않는다.) => 문자열이 같더라도 생성된 심벌 값은 유일무이한 값이다.
  - 문자열이 아닌 타입이 오면 자동으로 toString 처리합니다.

  ```javascript
  const mySymbol1 = Symbol('mySymbol');
  const mySymbol2 = Symbol('mySymbol');
  
  console.log(mySymbol1 === mySymbol2); // false
  ```

- 심벌 값도 문자열, 숫자, 불리언과 같이 암묵적 래퍼 객체를 생성한다.

  :grey_exclamation: 암묵적 래퍼 객체 : 마침표 표기법으로 객체 접근시에 임시로 생성되는 객체

  ```javascript
  const mySymbol = Symbol('mySymbol');
  
  console.log(mySymbol.description); // mySymbol
  console.log(mySymbol.toString()); // Symbol(mySymbol)
  ```

- 숫자나 문자열 타입으로 변환되지 않고, 불리언 타입으로 변환된다.

  ```javascript
  const mySymbol = Symbol();
  // 암묵적으로 문자열이나 숫자 타입으로 변환되지 않는다.
  console.log(mySymbol + ''); // TypeError
  console.log(+mySymbol); // TypeError
  
  // 불리언 타입으로는 암묵적으로 타입 변환된다.
  console.log(!!mySymbol); // true
  // if 문 등에서 존재 확인이가능
  if (mySymbol) console.log('Symbol이 존재')
  ```

### 33.2.2. Symbol.for / Symbol.keyFor 메서드

- `Symbol.for()`

  인수로 전달 받은 문자열을 키로 사용하여 **키와 심벌값의 쌍들이 저장**되어 있는 *전역 심벌 레지스트리*에서 해당 키와 일치하는 심벌 값을 검색

  - 성공시 검색 된 심벌 값 반환
  - 실패시 새로운 심벌 값 생성하여 인수로 전달된 키로 레지스트리에 저장 후 생성된 심벌 값 반환

  ```javascript
  const mySymbol1 = Symbol.for();
  const mySymbol2 = Symbol.for();
  
  console.log(mySymbol1 === mySymbol2) // true
  ```

  :grey_exclamation: 전역 심벌 레지스트리 : JS 엔진이 관리하는 심벌값 저장소

- `Symbol()`과 `Symbol.for()`의 차이?

  - Symbol함수는 호출될 때마다 유일무이한 심벌 값을 생성하는데, `Symbol()`의 경우 전역 심벌 레지스트리에서 심벌 값을 검색할 수 있는 키를 지정할 수 없으므로 전역 심벌 레지스트리에 등록되어 관리되지 않는다.
  - `Symbol.for()`를 사용하게되면 애플리케이션 전역에서 중복되지 않는 유일무이한 상수인 심벌 값을 단 하나만 생성하여 전역 심벌 레지스트리를 통해 공유할 수 있다.

  ```javascript
  const mySymbol1 = Symbol('hello'); // 여기서 hello는 description
  const mySymbol2 = Symbol.for('hello'); // 여기서 hello는 레지스트리에서 검색할 키
  const mySymbol3 = Symbol.for('hello');
  
  console.log(mySymbol1 === mySymbol2); // false
  console.log(mySymbol2 == mySymbol3); // true
  ```

- `Symbol.keyFor()`

  - 전역 심벌 레지스트리에 저장된 심벌 값의 키를 추출

  ```javascript
  const s1 = Symbol.for('mySymbol')
  console.log(Symbol.keyFor(s1)) // mySymbol
  
  const s2 = Symbol('foo');
  console.log(Symbol.keyFor(s2)) // undefined
  console.log(s2, typeof(s2))
  ```

## 33.3. 심벌과 상수

- 값에는 의미가 없고 상수 이름 자체에 의미가 있는 경우가 존재

  ```javascript
  // 1, 2, 3, 4엔 특별한 의미가 없고 상수 이름에 의미가 있다
  const Direction = {
    UP: 1,
    DOWN: 2,
    LEFT: 3,
    RIGHT: 4,
  }
  
  const myDirection = Direction.UP;
  
  if (myDirection === Direction.UP) {
    console.log('Going Up')
  }
  
  // 중복될 가능성이 없는 심벌 값으로 상수 값을 생성한다
  const Direction = {
      UP: Symbol('up'),
      DOWN: Symbol('down'),
    	LEFT: Symbol('left'),
    	RIGHT: Symbol('right'),
  }
  ```

## 33.4. 심벌과 프로퍼티 키

- 객체의 프로퍼티 키는 문자열 또는 심벌 값으로 만들 수 있고, 동적으로 생성할 수 있다.

- 동적 생성하는 경우

  ```javascript
  const obj = {
      [Symbol.for('mySymbol')]: 1
  }
  obj[Symbol.for('mySymbol')] // 1
  ```

  - 심벌 값을 프로퍼티 키로 사용하거나, 접근할 때 대괄호를 사용해야한다.

- **심벌 값은 유일무이한 값이으로 심벌 값으로 프로퍼티 키를 만들면 다른 프로퍼티 키와 절대 충돌하지 않는다.**

## 33.5. 심벌과 프로퍼티 은닉

- 심벌 값으로 프로퍼티 키를 생성한 경우 해당 프로퍼티는 `for ... in`, `Object keys`, `Object.getOwnPropertyNames` 메서드로 찾을 수 없다.(은닉이 가능)

  ```javascript
  const obj = {
    [Symbol('mySymbol')]: 1,
  };
  
  for (const key in obj) {
    console.log(key) // 아무것도 출력 x
  }
  
  console.log(Object.keys(obj)) // []
  console.log(Object.getOwnPropertyNames(obj)) // []
  ```

- `Object.getOwnPropertySymbols` 메서드를 사용하면 심벌 값을 프로퍼티 키로 사용하여 생성한 프로퍼티를 찾을 수 있다.

  ```javascript
  // getOwnPropertySymbols 메서드는 인수로 전달한 객체의 심벌 프로퍼티 키를 배열로 반환
  console.log(Object.getOwnPropertySymbols(obj)) // [ Symbol(mySymbol) ]
  const symbolKey1 = Object.getOwnPropertySymbols(obj)[0]
  console.log(obj[symbolKey1]) // 1
  ```

## 33.6. 심벌과 표준 빌트인 객체 확장

- 일반적으로 표준 빌트인 객체에 사용자 정의 메서드를 직접 추가하여확장하는 것은 권장하지 않는다.(읽기 전용으로 사용하는 것이 좋다)

  ```javascript
  Array.prototype.sum = function () {
      return this.reduce((acc, cur) => acc + cur, 0);
  };
  [1, 2].sum(); // 3
  ```

  - 추가된 사용자 정의 메서드와 미래 표준 사양으로 추가될 메서드의 이름이 중복될 수 있기 때문
  - 이렇게 된다면 표준 사양으로 추가하고자 했던 메서드를 사용자 정의 메서드가 덮어쓰게 된다.

- 중복될 가능성이 없는 심벌 값으로 프로퍼티 키를 생성하여 확장 시 다른 키와 절대 충돌하지 않아서 안전

  ```javascript
  Array.prototype[Symbol.for('sum')] = function () {
      return this.reduce((acc, cur) => acc + cur, 0);
  };
  [1, 2][Symbol.for('sum')](); // 3
  ```

## 33.7. Well-known Symbol

- 자바스크립트가 기본 제공하는 빌트인 심벌 값을 ECMAScript 사양에서는 Well-known Symbol이라 부른다.
- Symbol 함수의 프로퍼티에 할당되어 있다.
- 자바스크립트 엔진의 내부 알고리즘에 사용된다.
- 예를들어, `Array, String, Map, Set, TypedArray, arguments, NodeList, HTMLCollection`과 같이 `for ... of`문으로 순회 가능한 빌트인 이터러블은 `Symbol.iterator`를 키로 갖는 메서드를 가진다
- `Symbol.iterator` 메서드를 호출하면 이터레이터를 반환
- 빌트인 이터러블은 `Symbol.iterator`를 갖는 이터레이션 프로토콜을 준수한다.
- `Symbol.iterator`를 키로 갖는 메서드를 객체에 추가하고 이터레이터를 반환하도록 구현하면 그 객체는 이터러블이 된다.

**심벌은 중복되지 않는 상수 값을 생성하는 것은 물론 기존에 작성된 코드에 영향을 주지 않고 새로운 프로퍼티를 추가하기 위해, 즉 하위 호환성을 보장하기 위해 도입되었다.**

