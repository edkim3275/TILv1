import React, { useState } from "react";

const IterationSample = () => {
  const [names, setNames] = useState([
    { id: 1, text: "눈사람" },
    { id: 2, text: "얼음" },
    { id: 3, text: "눈" },
    { id: 4, text: "바람" },
  ]);
  const [inputText, setInputText] = useState("");
  const [nextId, setNextId] = useState(5);

  // const arr = [1, 2, 3, 4, 5];

  // const newArr = () => {
  //   const newArray = [];
  //   arr.map((currentValue, index, array) => {
  //     console.log("현재 currentValue :", currentValue);
  //     console.log("현재 index :", index);
  //     console.log("현재 array :", array);
  //     newArray.push(currentValue ** 2);
  //   });
  //   return newArray;
  // };

  // const newArr = arr.map(function (num) {
  //   return num * num;
  // });

  const onChange = (e) => setInputText(e.target.value);
  const onClick = () => {
    // setNames(state => [{id: nextId, text: inputText }])
    const nextNames = names.concat({
      id: nextId,
      text: inputText,
    });
    setNextId(nextId + 1);
    setNames(nextNames);
    setInputText("");
  };
  const onKeyUp = (e) => {
    if (e.keyCode === 13) {
      onClick();
    }
  };
  const onRemove = (id) => {
    const nextNames = names.filter((name) => name.id !== id);
    setNames(nextNames);
  };
  // const names = ["눈사람", "얼음", "눈", "바람", "꽃송이"];
  const nameList = names.map((name, index) => (
    <li key={name.id} onDoubleClick={() => onRemove(name.id)}>
      {name.text}
    </li>
  ));
  return (
    <>
      <input
        type="text"
        value={inputText}
        onChange={onChange}
        onKeyUp={onKeyUp}
      />
      <button onClick={onClick}>추가</button>
      <ul>{nameList}</ul>
    </>
  );
};

export default IterationSample;
