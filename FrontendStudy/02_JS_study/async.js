// const check = async function() {
//   let list = [];
//   for (let i=0; i < 20; i++) {
//     var k = await fetch('https://infuser.odcloud.kr/oas/docs?namespace=15069309/v1')
//     list.push(k)
//   };
//   console.log(list);
// }

// check();

// 2
async function getResult() {
  let list = [];
  for (let i=0; i < 20; i++) {
    var k = await fetch('https://infuser.odcloud.kr/oas/docs?namespace=15069309/v1')
    k = await k.json()
    list.push(k)
  };
  return list
}
getResult();

// 3
async function test() {
  let list = [];
  let arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const result = await Promise.all([
      arr.map((i) => {
          console.log(i)
          fetch('https://infuser.odcloud.kr/oas/docs?namespace=15069309/v1')
              .then(res => res.json())
              .then(data => list.push(data))
      })
      ])
  return result
}
test()
.then(res => console.log(res))

async function fetchData() {
  let result = await fetch('https://infuser.odcloud.kr/oas/docs?namespace=15069309/v1')
  result = await result.json()
return result
}

const result = await Promise.all([
fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
  fetchData(),
])
console.log(result)


// 5.
console.time('소요시간 : ')
const fetchData = async () => {
    let result = await fetch('https://infuser.odcloud.kr/oas/docs?namespace=15069309/v1')
    result = await result.json()
  return result
}
const getResult = async () => {
    const result = await Promise.all([
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
    fetchData(),
])
console.log(result)
}
getResult()
console.timeEnd('소요시간 : ') // 108  10102.656005859375 ms

// 12323.141845703125 ms

// 198 19676.88671875 ms  21120.72314453125 ms