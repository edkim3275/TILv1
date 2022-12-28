import React, { useState } from "react";

const Say = () => {
  const [msg, setMsg] = useState("default message");
  const sayHello = () => setMsg("hello");
  const sayGoodBye = () => setMsg("good bye!");

  return (
    <>
      <p>{msg}</p>
      <button onClick={sayHello}>hello?</button>
      <button onClick={sayGoodBye}>good bye~</button>
    </>
  );
};

export default Say;
