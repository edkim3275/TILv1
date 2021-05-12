// ... (Spread Operator)
const numbers = [1, 2, 3, 4, 5]
const newNumbers = [...numbers]  
// console.log(newNumbers) // [1, 2, 3, 4, 5]


const obj = {
  a: 1,
  b: 2,
}
const newObj = {
  ...obj
}
console.log(newObj) // { a: 1, b: 2 }