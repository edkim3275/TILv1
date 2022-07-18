// top level await
(async function() {
  await setServer();
})

await setServer();


// Error 
const err = new Error('error message', {cause: 'hello'});
console.log(err.cause);


// .at()
const arr = ['a', 'b', 'c', 'd'];
arr.at(1); // b
arr.at(-1); // d