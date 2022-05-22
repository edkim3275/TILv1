## 1. 변수

`var`, `let`, `const` 3가지가 존재. (ES6부터 `let`, `const`가 나왔고 이를 권장함)

- `var`

  ```js
  // 1. 선언 & 초기화 2. 할당
  // 함수 스코프
  var name; // undefined
  console.log(name); // undefined
  name = 'kim'
  ```

- `let`, `const`

  ```js
  // 1. 선언 2. 초기화 3. 할당
  // 블록 스코프
  let name;
  console.log(name); // ReferenceError
  name = 'kim'
  
  // 1. 선언 & 초기화 & 할당
  // 블록 스코프
  const name = 'kim'
  ```

  

## 2. 생성자 함수

```js
// 리터럴 객체
userX = {
    name: 'X',
    age: 32
}
```

객체를 선언하는 방법 중 하나로 리터럴 객체가 있다. 그런데 이 객체와 유사한 또 다른 객체를 많이 만들어야 하는 상황이 있다면?(예를들어 user1, user2, user3 ... 이 만들어질 경우) 리터럴 객체로 객체를 선언하는 것은 생각보다 번거로운 일이 될 것. 이러한 상황에서 객체를 보다 효율적으로 만들어주기 위해서 생성자 함수를 사용하게 된다.

```js
function User(name, age) {
    this.name = name;
    this.age = age;
}
user1 = new User('mj', 12); // user1 = { name: 'mj', age: 12}
user2 = new User('kim', 45); // user2 = { name: 'kim', age: 45}
```



## 3. 객체 메서드, Computed property

- ### computed property

  ```js
  let a = 'age';
  const user = {
      name: 'kim',
      [a]: 30,
      [1 + 4]: 5,
      ["안녕" + "하세요"]: "Hello"
  }
  ```

  - practice

    ```js
    // 1
    let n = "name";
    let a = "age";
    
    const user = {
        [n]: "Kim", // n 변수에 해당하는 값이 key에 적용 됨.
        [a]: 30
    }
    
    console.log(user); // {name: "Kim", age: 30}
    ```

    ```js
    // 2
    function makeObj(key, val) {
        return {
            [key]: val
        }
    }
    
    const obj = makeObj('나이', 30);
    console.log(obj); // {나이: 30}
    ```

    

- ### 객체 메서드

  - `Object.assign()` : 객체 복제

    assign(초기값, 초기값 객체에 병합 할 객체)

    ```js
    // 이런 경우 복제 불가
    // user에는 객체자체가 들어가있는 것이 아니라 객체가 저장되어있는 메모리의 주소 값(객체에 대한 참조 값)이 저장. 따라서 cloneUser의 경우에는 객체가 복사되는 것이 아니라 객체의 참조값이 저장되는 것.
    const user = {
        name: 'Kim',
        age: 15
    }
    const cloneUser = user;
    
    // 동일하게 복제하기 위해서는 Object.assign() 메서드를 활용
    const newUser = Object.assign({}, user);
    
    const anotherUser = Object.assing({ gender: 'male'}, user) // 새로운 key
    console.log(anotherUser) // { gender: 'male', name: 'Kim', age: 15}
    
    const otherUser = Object.assign({name: 'Park'}, user) //  key가 같은 경우
    console.log(otherUser) // { name: 'Kim', age: 15}
    
    // 2개 이상의 객체도 합치는 것이 가능
    const user = { name: 'Mike' }
    const info1 = { age: 30 }
    const info2 = { gender: 'male' }
    Object.assign(user, info1, unfo2) // info1, info2가 user에 합쳐진다.
    ```

    

  - `Object.keys()` : 키 배열 반환

    Object property의 키들을 배열로 반환

    ```js
    const user = {
        name: 'Kim',
        age: 30,
        gender: 'male',
    }
    Object.keys(user); // ["name", "age", "gender"]
    ```

    

  - `Object.values()` : 값 배열 반환

    ```js
    const user = {
        name: 'Kim',
        age: 30,
        gender: 'male',
    }
    Object.values(user); // ["Kim", 30, "male"]
    ```

    

  - `Object.entries()` : 키, 값 배열 반환

    키와 값을 쌍으로 묶어서 배열로 반환. 배열 안에 키와 값이 들어있는 배열이 존재.

    ```js
    const user = {
        name: 'Kim',
        age: 30,
        gender: 'male',
    }
    Object.entries(user); // [["name", "Kim"], ["age", 30], ["gender", "male"]]
    ```

    

  - `Object.fromEntries()` : 키, 값 배열을 객체로(entries 메서드의 반대)

    ```js
    const arr = [
        ["name", "Kim"], 
        ["age", 30], 
        ["gender", "male"]
    ]
    Object.fromentries(arr); // { name: 'Kim', age: 30, gender: 'male' }
    ```



## 4. 심볼

특정 객체의 원본 데이터는 건드리지 않고 속성을 추가할 수 있다. 유일한 식별자 역할을 한다.

- `Symbol()`

```js
const id = Symbol('id')
const id2 = Symbol('id2')
id === id2 // false
```

- 전역심볼 `Symbol.for()`
  - 하나의 심볼만 보장받을 수 있다. 없으면 만들고 있으면 가져오기 때문
  - 하나를 생성한 뒤 키를 통해 같은 Symbol을 공유

```js
const id = Symbol.for('id')
const id2 = Symbol.for('id')
id === id2 // true
```

Symbol을 완전히 숨길 수 있는 방법은 없다.

`Object.getOwnPropertySymbols(user)`, `Reflect.ownKeys(user)` 등을 사용하여 확인은 가능하다.

`Object.getOwnPropertySymbols(user)` : user 객체의 심볼들만 확인 가능

`Reflect.ownKeys(user)` : 심볼형 키를 포함한 객체의 모든 키 확인 가능

하지만 대부분의 라이브러리 내장 함수들은 위와 같은 함수를 사용하지 않기 때문에, 유일한 프로퍼티를 추가하고 싶다면 심볼을 사용하면 된다.

## 5. Number, Math

- `toString()` : 10진수 => 2진수/16진수

  ```js
  let num = 10;
  
  num.toString(); // "10"
  num.toString(2); // "1010"
  
  let num2 = 255;
  num2.toString(16) // "ff"
  ```

- `Math`

  JS에는 수학과 관련된 프로퍼티와 메서드를 갖고 있는 내장객체 `Math`가 있다. 대표적으로 `Math.PI`가 있다.

  - `Math.ceil()` : 올림

    ```js
    let num1 = 5.1;
    let num2 = 5.7;
    
    Math.ceil(num1); // 6
    Math.ceil(num2); // 6
    ```

  - `Math.floor()` : 내림

    ```js
    let num1 = 5.1;
    let num2 = 5.7;
    
    Math.floor(num1); // 5
    Math.floor(num2); // 5
    ```

  - `Math.round()` : 반올림(5보다 작으면 내림, 이상이면 올림)

    ```js
    let num1 = 5.1;
    let num2 = 5.7;
    
    Math.round(num1); // 5
    Math.round(num2); // 6
    ```

    - 소수점 자릿수

    ```js
    let userRate = 30.1234;
    // 소수점 둘째자리까지 표현(소수점 셋째자리에서 반올림)
    // 1. 10^2을 곱하고 반올림한 뒤에 다시 10^2를 나누는 방식
    Math.round(userRate * 100)/100 // 30.12 number
    
    // 2. toFixed() 문자열을 반환한다.
    userRate.toFixed(2); // "30.12" string
    userRate.toFixed(0); // "30" string
    userRate.toFixed(6); // "30.123400" string
    // 반환받은 이후에 숫자로 변환시켜 준다.
    Number(userRate.toFixed(2)); // 30.12 number
    ```

  - `Math.random()` : 0 ~ 1사이의 무작위 숫자 생성

    ```js
    Math.random() // 0.26027823967117425
    
    // 1 ~ 100사이 임의의 숫자를 뽑고 싶다면?
    Math.floor(Math.random()*100)+1
    ```

  - `Math.max()` / `Math.min()` : 최대, 최소

    ```js
    Math.max(1, 4, -1, 5, 10, 9, 5.54); // 10
    Math.min(1, 4, -1, 5, 10, 9, 5.54); // -1
    ```

  - `Math.abs()` : 절대값

    ```js
    Math.abs(-1); // 1
    ```

  - `Math.pow(n, m)` : 제곱

    ```js
    Math.pow(2, 10); // 1024
    ```

  - `Math.sqrt()` : 제곱근

    ```js
    Math.sqrt(16); // 4
    ```

- `isNaN()`

  `isNaN()`만이 NaN인지 아닌지 판단하는 유일한 방법이다.

  ```js
  let x = Number('x'); // NaN
  x == NaN // false
  x === NaN // false
  NaN == NaN // false
  isNaN(x); // true. NaN인지 판단하기 위한 유일한 방법
  isNaN(3); // false
  ```

- `parseInt()` : 문자를 숫자로 바꿔 줌

  `Number`와의 차이점은 문자가 혼용되어 있어도 동작을 한다. `Number`의 경우에는 NaN을 반환하지만 `ParseInt()`의 경우 읽을 수 있는 데까지 읽고, 문자가 나올경우 그 때까지의 숫자를 반환.

  ```js
  let margin = '10px';
  
  parseInt(margin); // 10
  Number(margin); // NaN
  
  let redColor = 'f3';
  parseInt(redColor); // 숫자로 시작하지않으면 NaN을 반환
  ```

  다만 2번째 인수를 받아서 진수를 지정할 수 있다.

  ```js
  let redColor = 'f3';
  parseInt(redColor); // 숫자로 시작하지않으면 NaN을 반환
  parseInt(redColor, 16); // 243, 2번째 인수에 16을 전달하여 16진수를 10진수로 변경함
  parseInt('11', 2); // 3, '11'을 숫자 11로 바꾸고 2진수를 10진수로 변경함
  ```

- `parseFloat()` : `parseInt()`와 동일하게 작동하지만 부동소수점을 반환.

  ```js
  let padding = '18.5%';
  parseInt(padding); // 18 소수점 이하는 무시하고 정수만 반환
  parseFloat(padding); // 18.5 부동소수점을 반환
  ```

## 6. string

- `length` : 문자열 길이

  ```js
  let desc = '안녕하세요.';
  desc.length; // 6
  ```

- 특정 위치에 접근

  ```js
  let desc = '안녕하세요.';
  desc[2]; // '하'
  // 바꿀수는 없다.
  desc[4] = '용'
  console.log(desc); // 안녕하세요.
  ```

- `toUpperCase()` / `toLowerCase()` : 대소문자 변경

- `indexOf(text)` : 문자를 인수로 받아 몇번째 인덱스인지 확인

  ```js
  let desc = "Hi guys. Nice to meet you.";
  desc.indexOf("to") // 14
  desc.indexOf("man") // -1
  ```

  포함된 문자가 여러개라도 앞에 있는 문자의 인덱스가 나온다.

  if문에서 사용될때 주의해야한다.

  ```js
  if (desc.indexOf("Hi") > -1) { // 0 => false
      console.log("Hi가 포한된 문장입니다.")
  }
  ```

- `slice(n, m)` : 특정 범위의 문자열 뽑기

  n : 시작점, m : 없으면 문자열 끝까지, 양수면 그 숫자까지(포함x), 음수면 끝에서부터

  ```js
  let desc = "abcdefg";
  desc.slice(2); // "cdefg"
  desc.slice(0, 5) // "abcde"
  desc.slice(2, -2) // "cde"
  ```

- `substring(n, m)` : n과 m 사이 문자열 반환

  단, n과 m을 바꿔도 동작함. 음수는 0으로 인식

  ```js
  let desc = "abcdefg"
  desc.substring(1, 5); // "bcde"
  desc.substring(5, 1); // "bcde"
  ```

- `substr(n, m)` : n 부터 시작, m개를 가져옴

  ```js
  let desc = "abcdefg";
  desc.substr(2, 4); // "cdef"
  desc.substr(-4, 2); // "de"
  ```

- `trim()` : 앞 뒤 공백 제거

  ```js
  let desc = " coding      ";
  desc.trim(); // "coding"
  ```

- `repeat(n)` : n번 반복

  ```js
  let desc = "hello!"
  hello.repeat(3); // "hello!hello!hello!"
  ```

- 문자열 비교

  | 십진법 | 십육진법 | 모양 | 85진법(아스키85) |
  | ------ | -------- | ---- | ---------------- |
  | 64     | 40       | @    | 31               |
  | 65     | 41       | A    | 32               |
  | ...    |          |      |                  |
  | 97     | 61       | a    | 64               |
  | 98     | 62       | b    | 65               |

  ```js
  "a" < "c" // true
  ```

  



