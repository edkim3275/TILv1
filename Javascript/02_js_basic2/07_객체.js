// js핵심이자 정수
/*
  {key: value} => Object === 객체
  1. key 문자열의 따옴표 삭제 가능(띄어쓰기 업슬 때)
  2. 접근할 때, ['key']와 .key 모두 가능
  ---

  3. 함수 정의 시...?
*/
const me = {
  name = '홍길동',
  // 'phone number': 010123456789 => 가능하지만 key도 변수명처럼 자를 것
  greeting: '어서오고',
  phoneNumber: '01012345678',
  friends: [
    '도우너', '마이콜', '또치'
  ],
  home: {
    address: '서울',
    owner: '고길동',
  }
}

/* ES6+ 축약 문법 */
// 1. Old(ES5 까지)
var books = ['Learning JS', 'EloquentJS']
var magazines = ['GQ', 'esquire']
var bookshop = {
  books: books,
  magazines: magazines,
}

// New(ES6+ 이후)
// key value가 같으면 한번만 쓸 수 있다.
const books = ['Learning JS', 'EloquentJS']
const magazines = ['GQ', 'esquire']
const bookshop = {
  books,
  magazines,
}


// object내부의 함수(메서드) 정의 == 메서드(객체 내에 정의되어 있는 함수)
// 2. Old
var dooly = {
  name: 'dooly',
  greeting: function () {
    console.log('어서 오고')
  }
}

// New
const dooly = {
  name: 'dooly',
  // Arrow
  greeting1: () => console.log('어서오고'),
  // Function 키워드 대체용
  greering2 () {
    console.log('어서오고')
  },
}


// 3. (minor) computed property name
const key = 'regions'
const value = ['서울', '대전', '광주', '구미', '부산']
const ssafy = {
  [key]: value
}
ssafy.regions


// 4. Object Destruturing (비구조화)
// Old(key값을 뽑아서 다시 value로 넣는 과정)
var userInfo = {
  name: '김싸피',
  email: 'kim@ssafy.com',
  phone: '0101234567',
}

var name = userInfo.name
var email = userInfo.email
var phone = userInfo.phone

// New(변수명과 key값이 같다면, 아래와 같이 작성 가능)
// 이처럼 옛날에 하는 것보다 더 쉽게 해주는 것을 syntatic sugar라고 합니다.
const userInfo = {
  name: '김싸피',
  email: 'kim@ssafy.com',
  phone: '0101234567',
}

// const { name } = userInfo
// const { email } = userInfo
// const { phone } = userInfo
const { name, email, phone } = userInfo

function printInfo(name, email, phone) {
  console.log(`안녕 나는 ${name} ${email} ${phone}`)
}

printInfo(userInfoo)
