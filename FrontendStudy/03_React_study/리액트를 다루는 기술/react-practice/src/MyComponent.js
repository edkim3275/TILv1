import { Component } from "react";
import PropTypes from "prop-types";

// const MyComponent = ({ name, favoriteNumber, children }) => {
//   return (
//     <>
//       <div>my name is {name}</div>
//       <br />
//       <div>children : {children}</div>
//     </>
//   );
// };

class MyComponent extends Component {
  render() {
    const { name, favoriteNumber, children } = this.props;
    return (
      <>
        <div>my name is {name}</div>
        <br />
        <div>children : {children}</div>
      </>
    );
  }
}
MyComponent.defaultProps = {
  name: "default name",
  favoriteNumber: 0,
};
MyComponent.propTypes = {
  name: PropTypes.string,
  favoriteNumber: PropTypes.number.isRequired,
};
export default MyComponent;
