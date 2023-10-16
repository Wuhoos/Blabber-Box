import React, { useEffect, useState } from "react";
import io from 'socket.io-client';
import { Switch, Route } from "react-router-dom";

let endPoint = 'http://localhost:5555';
let socket = io.connect(`${endPoint}`);

const App = () => {
  const [messages, setMessages] = useState(['Welcome User']);
  const [message, setMessage] = useState('');

  useEffect(() => {
    getMessages()
  }, [messages.length]);

  const getMessages = () => {
    socket.on('message', msg => {
      setMessages([...messages, msg]);
    });
  };

  // const onChange = e => {
  //   setMessage(e.target.value);
  // };

  // const onClick = () => {
  //   if (message !== '') {
  //     socket
  //   }
  // }
  return (
    <div>
      <p>Hello World!</p>
    </div>
  )
}

export default App;
