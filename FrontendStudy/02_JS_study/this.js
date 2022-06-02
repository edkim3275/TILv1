var a = 5;

function foo() {
  let a = 15
  return this.a
}

// 일반함수 호출에서 this는 무조건 전역객체
console.log(foo());

const obj = {
  a: 5,
  foo2() {
    console.log(this.a)
  }
}

// 메서드 호출은 해당 객체
obj.foo2()

