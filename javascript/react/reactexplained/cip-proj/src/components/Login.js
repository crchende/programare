import React, { useState, useContext } from "react";
import { Navigate } from "react-router-dom";

import UserContext from "../context/UserContext";

const Login = ( props ) => {
  const { user, onLogin } = useContext(UserContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (event) => {
    event.preventDefault();
    //console.log(email, password);
    onLogin(email, password);
  };


  if ( user.isAuthenticated === true) {
    console.log("Login Successful - navigating to the posts page");
    return <Navigate to="/" />
  }

  return (
    <form className="container" name="login" onSubmit={handleLogin}>
      <p>
        <label htmlFor="email">Email:</label>
        <input type="email"
          onChange={(event) => setEmail(event.target.value)}
        />
      </p>
      <p>
        <label htmlFor="password">Password:</label>
        <input type=""
          onChange={(event) => setPassword(event.target.value)}
        />
      </p>
      <p>
        <button type="submit" disabled={email === "" || password === ""}>
          Login
        </button>
      </p>
    </form>
  )
};

export default Login;
