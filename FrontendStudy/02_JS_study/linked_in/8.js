// Which code would you use to access the Irish flag?
// JSON.parse() 메서드는 JSON 문자열의 구문을 분석하고, 
// 그 결과에서 JavaScript 값이나 객체를 생성합니다. 
// 선택적으로, reviver 함수를 인수로 전달할 경우, 
// 결과를 반환하기 전에 변형할 수 있습니다.

// JSON.stringify() 메서드는 JavaScript 값이나 
// 객체를 JSON 문자열로 변환합니다.
var flagsJSON = '{ "countries": [' +
 '{ "country":"Ireland", "flag": "IE"},' +
 '{"country":"Serbia", "flag": "RS"},' +
 '{"country":"Peru", "flag": "PE"} ]}';

var flagDatabase = JSON.parse(flagsJSON);
console.log(flagDatabase[1].flag)

// flagsJSON.countries[0].flag // Cannot read property '0' of undefined
// flagDatabase.countries[1].flag
// flagDatabase.countries[0].flag
// flagDatabase[1].flag // Cannot read property 'flag' of undefined