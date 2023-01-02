# Should I use one or many state variables?

- 복잡한 중첩구조를 가진 객체를 사용할 때는, 복사비용에 주의하라.
  - flatten object(중첩객체 펼치기) - 같이 변경되는 값들 기준으로 상태분리하기
  - 1번이 불가능하다면, 불변객체를 사용할 수 있게 도와주는 라이브러리(immutable.js, immer) 사용

이름, 이메일, 휴대폰번호 ...

참고링크 : [useState in Reat: A complete guide - Multiple state variables or one state object](https://blog.logrocket.com/a-guide-to-usestate-in-react-ecb9952e406c/#multiplestatevariablesoronestateobject)