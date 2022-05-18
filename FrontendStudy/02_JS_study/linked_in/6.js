// Which statement prints "roar" to the console?
var sound = "grunt";
var bear = { sound: "roar" };

function roar() {
  console.log(this.sound); // this가 apply 첫번째 인자로 들어가는 obj가 된다.
}

roar.apply(bear); // roar
// roar.bind(bear); // nothing
// bear.bind(roar); // bear.bind is not a function
// bear[roar](); // bear[roar] is not a function