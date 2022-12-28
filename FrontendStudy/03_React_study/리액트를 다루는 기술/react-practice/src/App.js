import { Component } from "react";
// import MyComponent from "./MyComponent";
import Counter from "./Counter";
import Say from "./Say";

class App extends Component {
  render() {
    // const name = "edgar";
    return (
      <>
        {/* <h1>{name}</h1>
        <MyComponent name={name} favoriteNumber={3}>
          리액트 연습중
        </MyComponent> */}
        <Counter name="edgar" />
        <Say />
      </>
    );
  }
}
export default App;
