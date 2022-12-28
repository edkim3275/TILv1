import React, { Component } from "react";

class Counter extends Component {
  state = {
    number: 0,
    fixedNumber: 0,
  };
  // constructor(props) {
  //   // 클래스형 컴포넌트에서 constructor 작성시엔 반드시 super(props)를 호출해 주어야 한다.
  //   // 이 함수가 호출되면 현재 클래스형 컴포넌트가 상속받고 있는 리액트의 Component 클래스가 지닌 생성자 함수를 호출해준다.
  //   super(props);
  //   // state의 초기값 설정
  //   // this.state = {...}
  // }
  render() {
    // state를 조회할 때는 this.state로 조회한다.
    const { number, fixedNumber } = this.state;
    const { name } = this.props;
    return (
      <div>
        <h1>{number}</h1>
        <h2>fixedNumber : {fixedNumber}</h2>
        <h2>name : {name}</h2>
        <button
          // 이벤트 발생 시 호출할 함수를 지정한다.
          onClick={() => {
            // this.setState를 사용하여 state에 새로운 값을 넣을 수 있다.
            // this.setState함수는 인자로 전달된 객체 안에 들어 있는 값만 바꾸어 준다.
            this.setState({ number: number + 1 });
            // this.setState({ number: number + 1 });

            // 비동기문제 해결 : 함수를 인자로 넣어주자
            // prevState : 기존 상태
            // props : 현재 지니고 있는 props(불필요시 생략가능)
            this.setState(
              (prevState, props) => {
                return {
                  number: prevState.number + 1,
                };
              },
              () => {
                console.log("방금 setState 호출된 참이에용");
              }
            );
          }}>
          +1
        </button>
        <button onClick={() => console.log(number)}>check</button>
      </div>
    );
  }
}

export default Counter;
