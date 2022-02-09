let range = {
  from: 1,
  to: 5,
  [Symbol.iterator]() {
    let cur = this.from
    let max = this.to
    return {
      next() {
        if (cur <= max) {
          return {value: cur++, done: false}
        } else {
          return {done: true}
        }
      }
    }
  }
}

for (let num of range) {
  console.log(num)
}


// const mySymbol = Symbol();
// console.log(mySymbol, typeof mySymbol); // Symbol() symbol

const mySymbol = Symbol('mySymbol');
mySymbol.description = 'hello';
console.log(mySymbol.description); // mySymbol
console.log(mySymbol.toString()); // Symbol(mySymbol)


const s1 = Symbol.for('mySymbol')
console.log(Symbol.keyFor(s1)) // mySymbol
const s2 = Symbol('foo');
// console.log(Symbol.keyFor(s2)) // undefined
console.log(s2, typeof s2) // Symbol(foo) symbol


const obj = {
    [Symbol('mySymbol')]: 1,
    name: 'kim'
  };
  for (const key in obj) {
    console.log(key) // 아무것도 출력 x
  }
  console.log(Object.keys(obj)) // []
  console.log(Object.getOwnPropertyNames(obj)) // []
  

Object.prototype.objCustom = {};
Array.prototype.arrCustom = [];
let iterable = [3, 5, 7];
iterable.foo = "hello";
iterable.propertyIsEnumerable('foo') // true
Object.prototype.propertyIsEnumerable('objCustom') // true
Array.prototype.propertyIsEnumerable('arrCustom') // true
// 객체의 모든 열거 가능한 속성에 대해 반복
for (let i in iterable) {
  console.log(i); // logs 0, 1, 2, "foo", "arrCustom", "objCustom"
}
//  [Symbol.iterator] 속성을 가지는 컬렉션 전용
for (let i of iterable) {
  console.log(i); // logs 3, 5, 7
}
