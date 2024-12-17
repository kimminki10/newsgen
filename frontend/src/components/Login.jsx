import React from "react";
import { useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();

  const handleRegisterClick = () => {
    navigate("/register");
  };

  const handleResetClick = () => {
    navigate("/reset-password");
  };

  return (
    <div className="login-container">
      <h1>로그인</h1>
      <TextBox label="이메일주소" type="email" placeholder="Enter email" />
      <TextBox label="비밀번호" type="password" placeholder="Enter password" />
      <button className="login-btn">로그인</button>
      <div className="button-container">
        <button onClick={handleRegisterClick}>가입하기</button>
        <button onClick={handleResetClick}>계정찾기</button>
      </div>
    </div>
  );
};

export default Login;
