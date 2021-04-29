/*
  JS의 배열
  1. 리스트(크기 제한 없음)
  2. 음수인덱싱, 슬라이싱 불가능
*/


let numbers = [1, 2, 3, 4]
numbers[0]  // 가능
numbers[-1] // 음수 인덱스 불가능
// numbers[:]  // 슬라이싱 불가능
numbers.length // 길이

// .reverse() => 원본 파괴
numbers.reverse() // [4, 3, 2, 1] 리턴값이 존재
numbers // [4, 3, 2, 1] 원본값이 변경

// .push => return 0, 원본파괴 0
numbers = [1, 2, 3, 4]
numbers.push(5) // 5 : length를 return 
numbers // [1, 2, 3, 4, 5]

// .pop => return 0, 원본파괴
numbers.pop() // 'a' : pop한 겨과
numbers(27) // .shift)

// .unshift()
numbers.unshift('a') // 5 5; numbers.length를 return'
// numbers.unshift()  앞에 추가하
// numbers.unshift('a')
numbers

// .shift
numbers.shift()  // 'a' : stift
numbers.includes(4)

// includes()
numbers.includes(4) // true
numers // 변화없음

// # 12. indexOf()
numbers.indexOf(2)
numbersindexOf(1234)
numbrtd

// 13. .join()
numbers.joint('-') // 1-2-3-4
numbers             // 변화없음 



