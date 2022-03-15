# Object

- primitive type은 변수 하나당 하나의 값. 

- object는 key와 value의 집합체.

- 생성 방법

  ```js
  const obj1 = {}; // 'object literal' syntax
  const obj2 = new Object(); // 'object constructor' syntax
  ```

  - `new` 키워드 사용시 object에서 정의된  constructor가 호출되면서 object생성
  - JS는 dynamically typed language. 동적으로 타입이 런타임 때 결정되는 언어

## Computed properties

```js
console.log(ellie.name);
console.log(ellie['name']);
```

- object 내의 data에 접근하는 방법이 존재.
  - `.`으로 접근하거나
  - 배열에서 데이터를 받아오는 것처럼 접근이 가능. 여기서 **key는 `string` 타입**이어야만 한다.

```js
ellie.hasJob = true
ellie['hasJob'] = true
```

- 데이터를 추가하는 방법 또한 2가지.

- 그렇다면 어떤 경우에 어떤 방법이 사용되는 걸까?

  - `.` : 코딩을 하는 순간 key에 해당하는 값을 받아오고 싶은 경우(일반적으로 이 방식이 맞음)

  - computed properties : 정확하게 어떤 key가 필요한지 모를때. 실시간으로 원하는 property값을 받아오고 싶은 경우.

  - e.g.

    ```js
    function printValue(obj, key) {
        console.log(obj.key) // undefined
        console.log(obj[key])
    }
    printValue(ellie, 'name') // key는 string 타입으로 전달
    ```

    - **동적으로 key에 관련된 value를 받아와야할 때 유용하게 사용될 수 있다.**

## Property value shorthand

```js
const person1 = { name: 'bob', age: 9 };
const person2 = { name: 'steve', age: 30};
const person3 = makePerson('ellie', 20);

// shorthand
function makePerson(name, age) {
    return {
        name,
        age,
    };
}

// Constructor function
const person4 = new Person('kim', 38)
function Person(name, age) {
    // this = {};
    this.name = name;
    this.age = age;
    // return this;
}
```

- object를 생성할 경우 key와 value값이 동일하다면 콜론과 value를 생략가능

- 다른 계산없이 순수 object를 생성하는 함수는 보통 Pascal case로 이름을 작성

## in operator

- 해당 object 내에 key가 있는지 없는지를 확인하는 방법.

```js
console.log('name' in ellie); // true
console.log('age' in ellie); // true
console.log('random' in ellie); // false
console.log(ellie.random); // undefined
```

## for ..in vs. for ..of

```js
console.clear();
for (key in ellie) { // obj 모든 key들 받아와서 사용
	console.log(key); 
}

// for (value of iterable)
const arary = [1, 2, 3, 4];
for(let i = 0; i < array.length; i++) {
    console.log(array[i])
}
for(value of array) {
    console.log(value);
}
```

## cloning

```js
// Object.assign(dest, [obj1, obj2, obj3...])
const user = { name: 'ellie', age: '20' };
const user2 = user;
```

![image-20220313105022121](Object.assets/image-20220313105022121.png)

```js
user2.name = 'coder'; // user2가 가리키고있는 ref의 name을 변경하는 것.
console.log(user); // { name: 'coder', age: '20' }
```

- 그렇다면 obj를 실제로 복사하는 방법을 무엇일까?

```js
// old way
const user3 = {};
for (key in user) {
	user3.key = user[key];
}
console.log(user3); // { name: 'coder', age: '20'}

// Object.assign(target, source)
const user4 = {};
Object.assign(user4, user);
console.log(user4) // { name: 'coder', age: '20'}

const user5 = Object.assign({}, user)
console.log(user5) // { name: 'coder', age: '20'}
```

- `Object` 는 js내 기본적으로 탑재되어있는 object중하나. js의 모든 object는 `Object`를 상속한다.

```js
// another example
const fruit1 = { color: 'red'};
const fruit2 = { color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2);
console.log(mixed.color); // blue
console.log(mixed.size); // big
```

