# favicon

> 브라우저 탭의 `<title>` 태그 옆에 들어가는 요소를 파비콘이라고 부릅니다.

## 개요

CSS 연습도중 title부분에 지구본모양이 보기 싫어서 바꾸고 싶어서 찾아보게됨

## 방법

- HTML title 이미지 삽입 방법은 `<link>`태그에 이미지 주소를 링크시키면 됩니다.

  ```html
  <link href="이미지주소.ico" rel="shortcut icon" type="image/x-icon">
  ```

  예를 들어 사과 모양 로고의 주소를 브라우저 파비콘으로 삽입하고 싶다면 아래와 같이 작성합니다.

  ```html
  <link rel="shortcut icon" type="image/x-icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/800px-Apple_logo_black.svg.png">
  ```

- 용량을 줄이기 위해서 이미지 형식을 .ico로 변경하고 크기를 최대한 작게 16px정도로 만들어서 사용합니다.

- 뒤에