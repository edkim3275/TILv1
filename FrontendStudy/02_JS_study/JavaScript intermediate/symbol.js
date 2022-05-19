// 다른 개발자가 만들어 놓은 객체
const user = {
    name: 'Kim',
    age: 56
}

// 내가 작업
// user.showName = function () {
//     console.log(this.name)
// }
const showName = Symbol('show name');
const showName2 = Symbol.for('show name');


user[showName] = function () {
    console.log(this.name)
}
user[showName]()

// 사용자가 접속하면 보는 메시지
for (let key in user) {
    console.log(`His ${key} is ${user[key]}.`)
}

console.log(showName === showName2) // false
console.log(showName.description) // show name
console.log(Symbol.keyFor(showName2)) // show name
