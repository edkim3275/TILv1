const id = 'admin'

if (id === 'admin') {
  console.log('관리자님, 환영합니다.')
} else if (id === 'manager') {
  console.log('매니저님, 환영합니다.')
} else {
  console.log(`${id} 님, 환영합니다.`)
}


// 하나가지고 비교할 때
switch (id) {
  case 'admin': {
    console.log('관리자님, 환영합니다.')
    break // 무조건 들어가야함
  }
  case 'manager': {
    console.log('매니저님 환영합니다.')
    break // 무조건 들어가야함
  }
  default: {
    console.log(`${id} 님, 환영합니다.`)
  }
}

if (a === 1) {}
else if (a !== 1 && b === 1) {}