/*
camelCase === lowerCamelCase
변수, 상수, 함수명

PascalCase === UpperCamelCase
class명

UPPER_SNAKE_CASE
절대 변하면 안되는 상수 값
*/

// let => 변수 재할당 가능
let x = 1
x = 2

// const => const는 상수. *재할당* 불가능
const y = 1
y = 2 // ERROR. 재할당 불가능

const arr = []
arr.push(1) // 값을 아예 바꾸는 것이아니라 배열에 할당하는 것은 가능


// scope
// 블록({ block }) 스코프

if (true) {
  let y = 1
}
console.log(y) // y is not defined ERROR
