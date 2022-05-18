// 12. How does the forEach() method differ form a for statement?
// forEach는 비동기함수라서 eventloop에 저장이 되고 모두 실행이되는 반면1, 2, 3, 4 다 찍히는 반면
// for는 동기함수라서 eventloop에 저장되는것이 아니라서 도중에 나올 수 있다.
const array = [1, 2, 3, 4, 5, 6]

array.forEach(e => {
  if (e === 3) {
    return
  }
  console.log(e)
})
// console.log(returnedElement)
