let i = 0
while (i < 5) {
  console.log('hi')
  // i += 1
  i++
}


// 세상의 모든 for문은 이렇게 생김
// 전통적인 for
for (let j=0; j<5; j++) {
  console.log('hi', j)
}
// 인덱스 활용
for (let j=0; j<arr.length; j++) {
  console.log(arr[j])
}
// Array => 요소를 꺼내는 for - of 리스트 돌릴 때
const arr = [1, 2, 3, 4, 5]
for (let number of arr) {
  console.log(number)
}

// Object(key-value값을 가지고 있는 객체) => Key를 꺼내는 for - in
const person = {'name': 'neo', 'address': 'seoul'}
for (const key in person) {
  console.log(key, person[key])
}
// 1. 따옴표 생략 가능
// 2. person.name, person.address