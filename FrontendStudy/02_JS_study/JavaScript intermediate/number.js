let userRate = 30.1234;
// 소수점 둘째자리까지 표현(소수점 셋째자리에서 반올림)
// 1. 10^2을 곱하고 반올림한 뒤에 다시 10^2를 나누는 방식
userRate = Math.round(userRate * 100) / 100 // 30.12

// 2. toFixed()
// userRate = userRate.toFixed(2); // "30.12"
console.log(userRate, typeof userRate)

console.log(parseInt('11', 2))