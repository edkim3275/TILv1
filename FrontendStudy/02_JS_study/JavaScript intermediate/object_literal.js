const user = {
    name: 'Kim',
    age: 28
}

const anotherUser = {
    name: 'Lee',
    age: 29
}

// Object.assign()
const user2 = Object.assign({ gender: 'male' }, user);
const user3 = Object.assign({}, user, anotherUser);

// 스프레드 문법을 적용한 객체 리터럴
// const user2 = { ...user }
// const user3 = { ...user, ...anotherUser }

user2.name = 'Park';
console.log(user);
console.log(user2);
console.log(user3);


// Object.keys()
const keyLst = Object.keys(user);
console.log(keyLst);

// Object.values()
const valueLst = Object.values(user);
console.log(valueLst);

// Object.entries()
const keyValueLst = Object.entries(user);
console.log(keyValueLst);

// Object.fromentries()
const arr = [['name', 'Kim'], ['age', 28]]
const obj = Object.fromEntries(arr);
console.log(obj)