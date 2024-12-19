import React, { useRef } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";
import TextBox from "./TextBox";
import axios from "axios";
import "./Login.css";

const do_login = async (email, password) => {
  try {
    const response = await axios.post("/api/token/", {
      email,
      password,
    });
    if (response.status === 200) {
      alert("로그인에 성공했습니다.");
      localStorage.setItem("fintrend_access_token", response.data.access);
      localStorage.setItem("fintrend_refresh_token", response.data.refresh);
      localStorage.setItem("userEmail", email);
      return true;
    } else {
      console.log(response.data);
      alert("로그인에 실패했습니다. 다시 시도해주세요.");
    }
  } catch (error) {
    console.error("로그인 요청 중 오류가 발생했습니다.", error);
    alert("로그인 요청 중 오류가 발생했습니다.");
  }
  return false;
};

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

  const handleLogin = async () => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;

    if (!email || !password) {
      alert("이메일과 비밀번호를 입력해주세요.");
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("올바른 이메일 형식을 입력해주세요.");
      return;
    }

    if (password.length < 8) {
      alert("비밀번호는 8자 이상이어야 합니다.");
      return;
    }

    const loginSuccess = await do_login(email, password);
    if (!loginSuccess) {
      alert("로그인에 실패했습니다. 다시 시도해주세요.");
      return;
    }

    login(email);
    navigate("/");
  };

  return (
    <div className="login-container">
      <h1>로그인</h1>
      <div className="input-wrapper">
        <div className="input-field">
          <TextBox
            ref={emailRef}
            label="이메일주소"
            type="email"
            placeholder="example@gmail.com"
          />
        </div>
        <div className="password-field">
          <TextBox
            ref={passwordRef}
            label="비밀번호"
            type="password"
            placeholder="********"
          />
          <span className="password-hint">
            비밀번호는 8자 이상이어야 합니다
          </span>
        </div>
        <button className="login-btn" onClick={handleLogin}>
          로그인
        </button>
        <div className="button-container">
          <button onClick={handleRegisterClick}>가입하기</button>
          <button onClick={handleResetClick}>계정찾기</button>
        </div>
      </div>
    </div>
  );
};

export default Login;
