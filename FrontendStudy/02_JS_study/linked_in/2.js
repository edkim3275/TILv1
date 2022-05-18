// 2. Which snippet could you add to this code to print "food" to the console?
class Animal {
  static belly = [];
  eat() { Animal.belly.push("food");}
}

let a = new Animal();
a.eat();

let b = new Animal();
b.eat();

console.log(a.belly); // Prints food
console.log(b.belly); // undefined

// Object.getPrototypeOf(a).belly[0] // 1 Cannot read property '0' of undefined
// a.belly[0] // 2 Cannot read property '0' of undefined
// a.prototypeOf.belly[0] // 3 Cannot read property 'belly' of undefined
// Animal.belly[0] // 4 food