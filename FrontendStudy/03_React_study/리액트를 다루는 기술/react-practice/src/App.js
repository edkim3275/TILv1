import { Component } from "react";
// import MyComponent from "./MyComponent";
import Counter from "./Counter";
import IterationSample from "./IterationSample";
import LifeCycleSample from "./LifeCycleSample";
import Say from "./Say";
import ScrollBox from "./ScrollBox";
import ValidationSample from "./ValidationSample";

function getRandomColor() {
  return "#" + Math.floor(Math.random() * 16777215).toString(16);
}

class App extends Component {
  state = {
    color: "#000000",
  };

  handleClick = () => {
    this.setState({
      color: getRandomColor(),
    });
  };

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
        {/* <ScrollBox ref={(ref) => (this.scrollBox = ref)} />
        <button onClick={() => this.scrollBox.scrollToBottom()}>
          맨 밑으로
        </button> */}
        {/* <IterationSample /> */}
        <button onClick={this.handleClick}>랜덤 색상</button>
        <LifeCycleSample color={this.state.color} />
      </>
    );
  }
}
export default App;
