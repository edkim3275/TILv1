const arr = [1, 2, 3]
/*
array helper methods의 생김새
.forEach, .map, .find, .filter 

arr.helperMethod(callbackFunction)
arr.helperMethod(function (arg) {})

*/
// .forEach() => 유일하게 return되는 값 없음 => 해당 메서드의 리턴또한 없다. 콜백 함수에 return 필요 없음
arr.forEach(function () {
  console.log(num)
})

// .forEach()는 for - of의 대체제 느낌
for (const num of arr) {
  console.log(num)
}





// .map() => 콜백함수의 리턴값으로 만든 배열을 리턴
arr.map(function (num) {
  return num * 2
})
// arr.map(num => num * 2)

// 1
const contents = ['hello', 'world']
const tags = contents.map(function (content) {
  return `<h2>${content}</h2>`
})
tags.forEach(tag => document.write(tag))

// 2
contents.map(function (num) {
  return `<h2>${content}</h2>`
})
contents.map(content=> `<h2>${content}</h2>`).forEach(tag => document.write(tag))



// .find(cb) => 콜백 함수의 리턴값이 true(혹은 true로 평가되는)
// 첫번째 요소만 리턴
arr.find(function (num) {
  return num === 2
})

arr.find(num => num === 2)

const articles = [
  {pk: 1, title: 'hi'},
  {pk: 2, title: 'hello'},
  {pk: 3, title: 'great'},
]
articles.find(article => article.pk === 3)

// .filter(cb) => 콜백함수의 리턴값이 true(혹은 true로 평가되는)인 요소만 모아서 배열로 리턴
arr.filter(num => num % 2)

// 사용 예시
const movies = [
  {title: 'matrix', isAdult: false},
  {title: 'kingsman', isAdult: true},
]
const adultMovies = movies.filter(movie => movie.isAdult)
// 같은 말
const adultMovies = movies.filter(function (movie) {
  return movie.isAdult
})



// .some(cb), .every(cb) => 배열 안의 하나라도 / 전부 콜백에서 return 하는
arr.every(num => num > 0) // arr요소가 모두 true라면 true
arr.some(num => !num % 2) // arr요소중에 하나라도 true라면 true



// .reduce(cb, initValue) => .reduce도 인자가 2개 필요, cb도 인자가 2개필요
// 이전 함수의 return 값이 function의 acc로 들어가게됨
// initValue
arr.reduce(function (acc, num) {
  console.log(num, acc)
}, 0)

// 총 합 구하기
arr.reduce(function (acc, num) {
  return acc + num
})

// 2씩 곱하기
arr.reduce(function (acc, unm) {
  acc.push(num * 2)
  return acc
})