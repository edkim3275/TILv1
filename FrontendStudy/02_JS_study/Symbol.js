// 1. Symbol.for()
// const mySymbol1 = Symbol.for(); // Symbol(undefined)
// const mySymbol2 = Symbol.for();

// console.log(mySymbol1 === mySymbol2) // true
// console.log(Symbol.for(undefined) == mySymbol2)

// 2. Symbol()과 Symbol.for()의 차이
// const mySymbol1 = Symbol('hello');
// const mySymbol2 = Symbol.for('hello');
// const mySymbol3 = Symbol.for('hello');

// console.log(mySymbol1 === mySymbol2); // false
// console.log(mySymbol2 == mySymbol3); // true

// 3. Symbol.keyFor()
// 전역 심벌 레지스트리에 저장된 심벌 값의 키를 추출
// const s1 = Symbol.for('symbol\'s key')
// console.log(Symbol.keyFor(s1)) // symbol's key

// const s2 = Symbol('foo');
// console.log(Symbol.keyFor(s2)) // undefined
// console.log(s2, typeof(s2))

// 4. 심벌과 상수
const Direction = {
  UP: Symbol('up'),
  DOWN: Symbol('down'),
  LEFT: Symbol('left'),
  RIGHT: Symbol('right'),
}

const myDirection = Direction.UP;

if (myDirection === Direction.UP) {
  console.log('Going Up')
}


// 5. 심벌과 프로퍼티 은닉
// const obj = {
//   [Symbol('mySymbol')]: 1,
// };

// for (const key in obj) {
//   console.log(key) // 아무것도 출력 x
// }

// console.log(Object.keys(obj)) // []
// console.log(Object.getOwnPropertyNames(obj)) // []

// // getOwnPropertySymbols 메서드는 인수로 전달한 객체의 심벌 프로퍼티 키를 배열로 반환
// console.log(Object.getOwnPropertySymbols(obj)) // [ Symbol(mySymbol) ]
// const symbolKey1 = Object.getOwnPropertySymbols(obj)[0]
// console.log(obj[symbolKey1])

// 6. Symbol.iterator
// const iterable = {
//   [Symbol.iterator]() {
//     let cur = 1;
//     const max = 5;
//     return {
//       next() {
//         return { value: cur++, done: cur > max + 1};
//       }
//     }
//   }
// }
// for (const item of iterable) {
//   console.log(item)
// }

// 

// const mySymbol1 = Symbol('mySymbol');
// const mySymbol2 = Symbol('mySymbol');
// console.log(mySymbol1 === mySymbol2) // false

// const mySymbol = Symbol('mySymbol');


const isIterable = v => v !== null && typeof v[Symbol.iterator] === 'function';

// 유사 배열 객체
// const arrayLike = {
//   0: 1,
//   1: 2,
//   2: 3,
//   length: 3
// }
// // 유사 배열 객체는 length 프로퍼티를 갖기 때문에 for 문으로 순회할 수 있다.
// for (let i=0; i < arrayLike.length; i++) {
//   // 유사 배열 객체는 마치 배열처럼 인덱스로 프로퍼티 값에 접근할 수 있다.
//   console.log(arrayLike[i])
// }

// 무한 이터러블을 생성하는 함수
// const fibonacciFunc = function() {
//   let [pre, cur] = [0, 1]
//   return {
//     [Symbol.iterator]() {return this},
//     next() {
//       [pre, cur] = [cur, cur+pre]
//       // 무한을 구현해야 하므로 done프로퍼티를 생략
//       return {value: cur}
//     }
//   }
// }
// for (const num of fibonacciFunc()) {
//   if (num > 1000) break;
//   console.log(num)
// }
// const [f1, f2, f3] = fibonacciFunc();
// console.log(f1, f2, f3)

// const a = 1
// const b = a+'12'
// const c = a-'12'
// console.log(b, typeof b) // 112 string
// console.log(c, typeof c) // -11 number


// 실패시 새로운 심벌 값 생성하여 인수로 전달된 키로 레지스트리에 저장 후 생성된 심벌 값 반환
// const mySymbol1 = Symbol.for();
// // 성공시 검색 된 심벌 값 반환
// const mySymbol2 = Symbol.for();
// console.log(mySymbol1 === mySymbol2) // true
// console.log(Symbol.for(undefined) === mySymbol1) // true
// console.log(Symbol.for('undefined') === mySymbol1) // true

// 프로퍼티 키 동적 생성
// let i = 0
// const obj = {
//     [Symbol.for(`mySymbol${i++}`)]: i, // [Symbol.for('mySymbol0)]: 1
//     [Symbol.for(`mySymbol${i++}`)]: i, // [Symbol.for('mySymbol1)]: 2
//   }
// console.log(obj[Symbol.for('mySymbol0')]) // 1

// 프로퍼티 키 은닉이 안되는 경우
// let id = Symbol('id');
// let user = {
//   [id]: 123
// };
// let clone = Object.assign({}, user)
// console.log(clone) // { [Symbol(id)]: 123 }

// for in과 for of의 차이
// let iterable = [3, 5, 'a'];
// // iterable.foo = "hello";

// for (let key in iterable) {
//   console.log(key, typeof key); // 0, 1, 2 string
// }

// for (let value of iterable) {
//   console.log(value); // 3, 5, 7
// }

// console.log(iterable, iterable.length ,typeof iterable)

// Object.prototype.objCustom = {};
// Array.prototype.arrCustom = [];

// let iterable = [3, 5, 7];
// iterable.foo = "hello";

// iterable.propertyIsEnumerable('foo') // true
// Object.prototype.propertyIsEnumerable('objCustom') // true
// Array.prototype.propertyIsEnumerable('arrCustom') // true

// 객체의 모든 열거 가능한 속성에 대해 반복
// for (let i in iterable) {
//   console.log(i); // logs 0, 1, 2, "foo", "arrCustom", "objCustom"
// }
// //  [Symbol.iterator] 속성을 가지는 컬렉션 전용
// for (let i of iterable) {
//   console.log(i); // logs 3, 5, 7
// }

// // 이터러블
// const iterable = [1, 2, 3];
// // 이터러블의 Symbol.iterator 메서드를 호출하여 이터레이터를 생성
// const iterator = iterable[Symbol.iterator]();
// for (;;) {
//   // 이터레이터의 next 메서드를 호출하여 이터러블을 순회한다
//   // 이때 next 메서드는 이터레이터 리절트 객체를 반환한다.
//   const res = iterator.next() 
//   // next 메서드가 반환한 객체의 done 프로퍼티의 값이 true이면 순회를 중단
//   if (res.done) break;
//   // 이터레이터 리절트 객체의 value 프로퍼티 값을 item 변수에 할당
//   const item = res.value;
//   console.log(item)
// }
const mySymbol1 = Symbol('mySymbol');
const mySymbol2 = Symbol('mySymbol');
console.log(mySymbol1 === mySymbol2) // false
const sym = Symbol();
console.log(sym.description, typeof sym.description) // undefined undefined

const mySymbol3 = Symbol.for();
console.log(mySymbol3.description, typeof mySymbol3.description)


const obj = {
    [Symbol('mySymbol')]: 1,
  };
  for (const key in obj) {
    console.log(key) // 아무것도 출력 x
  }

console.log(Object.getOwnPropertySymbols(obj)) // [ Symbol(mySymbol) ]
const symbolKey1 = Object.getOwnPropertySymbols(obj)[0]
obj[symbolKey1] = 5
console.log(obj[symbolKey1]) // 1

  