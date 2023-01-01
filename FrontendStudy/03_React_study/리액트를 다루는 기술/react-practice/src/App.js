import { Component } from "react";
// import MyComponent from "./MyComponent";
import Counter from "./Counter";
import Say from "./Say";
import ScrollBox from "./ScrollBox";
import ValidationSample from "./ValidationSample";

class App extends Component {
  render() {
    // const name = "edgar";
    return (
      <>
        {/* <h1>{name}</h1>
        <MyComponent name={name} favoriteNumber={3}>
          리액트 연습중
        </MyComponent> */}

        {/* <Counter name="edgar" /> */}
        {/* <Say /> */}
        {/* <ValidationSample /> */}
        <ScrollBox ref={(ref) => (this.scrollBox = ref)} />
        <button onClick={() => this.scrollBox.scrollToBottom()}>
          맨 밑으로
        </button>
      </>
    );
  }
}
export default App;
