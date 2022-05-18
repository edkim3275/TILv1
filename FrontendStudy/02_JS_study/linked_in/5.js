// Which line could you add to this 
// code to print "jaguar" to the console?
let animals = ["jaguar", "eagle"];

// Missing Line
// const otherAnimals = animals.reverse();
// console.log(otherAnimals === animals) // true

console.log(animals.filter(e => e === "jaguar"))


console.log(animals.pop()); // Prints jaguar

// animals.shift(); // 원본을 바꿈
// animals.reverse(); // jaguar 원본을 바꾸고 반환을 함.
// animals.pop(); // jaguar 원본을 바꿈.
// animals.filter(e => e === "jaguar"); // eagle 조건에 맞는 요소를 배열에 담아서 반환