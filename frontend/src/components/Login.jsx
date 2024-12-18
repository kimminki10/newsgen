import React, { useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";
import TextBox from "./TextBox";
import "./Login.css";

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const emailRef = useRef(null);
  const passwordRef = useRef(null);

  const handleRegisterClick = () => {
    navigate("/register");
  };

  const handleResetClick = () => {
    navigate("/reset-password");
  };

  const handleLogin = () => {
    const email = emailRef.current.value;
    // 실제 백엔드 연동 대신 임시로 로그인 처리
    login(email);
    navigate("/"); // 홈으로 리다이렉트
  };

  return (
    <div className="login-container">
      <h1>로그인</h1>
      <TextBox ref={emailRef} label="이메일주소" type="email" placeholder="Enter email" />
      <TextBox ref={passwordRef} label="비밀번호" type="password" placeholder="Enter password" />
      <button className="login-btn" onClick={handleLogin}>로그인</button>
      <div className="button-container">
        <button onClick={handleRegisterClick}>가입하기</button>
        <button onClick={handleResetClick}>계정찾기</button>
      </div>
    </div>
  );
};

export default Login;
