// JSON === JavaScript Object Notation
/* Python
  import json
  json.loads
  json.dumps
*/

const obj = {
  coffee: 'Americano',
  iceCream: 'Cookie&Cream',
}

const jsonData = JSON.stringify(obj)
const backToObj = JSON.parse(jsonData)