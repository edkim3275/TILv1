function makeObj(key, val) {
    return {
        [key]: val
    }
}

const obj1 = makeObj('나이', 30);
console.log(obj1)

const user = {
    name: 'Kim',
    age: 28,
}

const user2 = Object.assign({}, user)
console.log("user2: ", user2)