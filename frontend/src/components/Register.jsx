import React, { useRef } from "react";
import { useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import axios from "axios";
import "./Register.css";

const do_register = async (email, password, password_check) => {
  try {
    const response = await axios.post("http://localhost:8000/register/", {
      email,
      password,
      password_check,
    });
    if (response.status === 200) {
      alert("회원가입이 완료되었습니다. 로그인해주세요.");
      return true;
    } else {
      console.log(response.data);
      alert("회원가입에 실패했습니다. 다시 시도해주세요.");
    }
  } catch (error) {
    console.error("회원가입 요청 중 오류가 발생했습니다.", error);
    alert("회원가입 요청 중 오류가 발생했습니다.");
  }
  return false;
};

const Register = () => {
  const navigate = useNavigate();
  const emailRef = useRef(null);
  const passwordRef = useRef(null);
  const passwordCheckRef = useRef(null);

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleResetClick = () => {
    navigate("/reset-password");
  };

  const handleRegister = async () => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    const password_check = passwordCheckRef.current.value;

    if (!email || !password || !password_check) {
      alert("모든 필드를 입력해주세요.");
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

    if (password !== password_check) {
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }

    const registerSuccess = await do_register(email, password, password_check);
    if (!registerSuccess) {
      alert("회원가입에 실패했습니다. 다시 시도해주세요.");
      return;
    }

    navigate("/login");
  };

  return (
    <div className="register-container">
      <h1>회원가입</h1>
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
        </div>
        <div className="password-field">
          <TextBox
            ref={passwordCheckRef}
            label="비밀번호 확인"
            type="password"
            placeholder="********"
          />
          <span className="password-hint">
            비밀번호는 8자 이상이어야 합니다
          </span>
        </div>
        <button className="register-btn" onClick={handleRegister}>
          가입하기
        </button>
        <div className="button-container">
          <button onClick={handleLoginClick}>로그인</button>
          <button onClick={handleResetClick}>계정찾기</button>
        </div>
      </div>
    </div>
  );
};

export default Register;
