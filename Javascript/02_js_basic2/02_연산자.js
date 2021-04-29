/*
  Operands
  1. unary (단항 연산자) :
  -, typeof, ++, --, !
  - (음수 / 양수), mypotsjac

  2. binary (이항 연산자)
  Meta : +, -, *, /, +=, -=, *=, /=.  --
  &&, ||
  3. ternary (삼항 연산자)
  # ++, --, &&, ||
  ? :
  3.1. 산술연산자
  3.2. 수 비교연산자
  3.3. 동등/일치 연산자
  3.4. 논리연산자
*/

console.log(
  'unary Operator',
  -1, typeof 1
)

let i = 1
// 1에 대한 경가가후 정재가능
// i에 대한 평가가 끝난 후, 1을 더한다
console.log(i++)
// i에 대한 평가 전에 1을 더한다
console.log(++1)

// ! => not과 같다
console.log(!true)

//  동등 == => 안 씀(동등 연산자 믿을게 못 됨)
0 == '0'  // true 넘겨짚이서 true
0 == []   // true 넘겨짚어서 true
'0' == [] // false 넘겨짚지 못하니까 false


//  일치 === => 이것만 사용


// and => &&
console.log(true && true && false)
console.log(false || true || true)

// 가치평가 ? true일 경우 : false일 경우
console.log(1 > 2 ? '크다' : '작다')

let a = 1
const even_or_odd = a % 2 ? 'odd' : 'even'
console.log(even_or_odd)