# Reference Vs. Value in JavaScript

```javascript
let a = 10
let b = "Hi"
let c = a // 10
c = c + 1 // 11
let d = [1, 2]
```

| Variable | Value  | Reference | Value  |
| -------- | ------ | --------- | ------ |
| a        | 10     | 0x01      | [1, 2] |
| b        | "Hi"   |           |        |
| c        | 10     |           |        |
| d        | <0x01> |           |        |
| e        | <0x01> |           |        |

arrays and objects and essentially anything that's not the primitive type of string number boolean etc those are going to be passed by reference

when you call `d` you're not actually getting this value here returns this `0x01`. you're actually being returned the value of the memory at that location

both `d` and `e` point to the exact same memory address which means `d` and `e` are referenced in the exact same piece of memory inside of your code



step further you can see if we want to add a new variable

```javascript
let c = [1, 2]
let d = c
d.push(3)
```

| Variable | Value  | Reference | Value     |
| -------- | ------ | --------- | --------- |
| c        | <0x01> | 0x01      | [1, 2, 3] |
| d        | <0x01> |           |           |



now let's go one step further and actually set `d` to a brand new variable

```javascript
let c = [1, 2]
let d = c
d = [3, 4, 5]
```

| Variable | Value  | Reference | Value     |
| -------- | ------ | --------- | --------- |
| c        | <0x01> | 0x01      | [1, 2]    |
| d        | <0x02> | 0x02      | [3, 4, 5] |

in JavaScript, you take the value of whatever is on the right and our case `[3, 4, 5]` has the memory address of `02` so we take that `02` value and we set it to `d`



```javascript
let c = [1, 2]
let d = c

console.log(`c === d ${c === d}`) // true
console.log(`c == d ${c == d}`) // true

let c = [1, 2] // 0x01
let d = [1, 2] // 0x02

console.log(`c === d ${c === d}`) // false
console.log(`c == d ${c == d}`) // false
```

the reason for this is because when we're using the equal sign to compare two different objects for example these two arrays it's actually checking the value that variable value section where we had the memory address being stored.



conclusion. what you need to know is that primitive values such as numbers, boolean, strings, undefined, null those are all passed by value and other things such as arrays, objects, classes those are all passed by reference and can thus be modified. this is why when you set an array to a constant variable

```javascript
const c = [1, 2] // 0x01
c.push(3)
console.log(c) // [1, 2, 3]
```

you still able to do see that push for example of three because the value that is being constant is that memory reference of `0x01`that's what can't change but what we actually store at that memory address can change