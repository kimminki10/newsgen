import React, { useRef } from "react";
import { useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import axios from "axios";
import "./TextBox.css";
import "./Register.css";

const do_register = async (email, password) => {
  try {
    const response = await axios.post("http://localhost:8000/user/", {
      email,
      password,
    });
    if (response.status === 201) {
      alert("가입이 완료되었습니다.");
      return true;
    } else {
      console.log(response.data);
      alert("가입에 실패했습니다. 다시 시도해주세요.");
    }
  } catch (error) {
    console.error("가입 요청 중 오류가 발생했습니다.", error);
    alert("가입 요청 중 오류가 발생했습니다.");
  }
  return false;
};

const Register = () => {
  const emailRef = useRef(null);
  const passwordRef = useRef(null);
  const passwordCheckRef = useRef(null);
  const navigate = useNavigate();

  const handleRegister = async () => {
    const email = emailRef.current.value;
    const password = passwordRef.current.value;
    const passwordCheck = passwordCheckRef.current.value;

    if (!email || !password || !passwordCheck) {
      alert("이메일과 비밀번호를 입력해주세요.");
      return;
    }

    // 이메일 형식 검증
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("올바른 이메일 형식을 입력해주세요.");
      return;
    }

    // 비밀번호 길이 검증
    if (password.length < 8) {
      alert("비밀번호는 8자 이상이어야 합니다.");
      return;
    }

    if (password !== passwordCheck) {
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }

    const registerSuccess = await do_register(email, password);
    if (!registerSuccess) {
      alert("가입에 실패했습니다. 다시 시도해주세요.");
      return;
    }

    alert("가입이 완료되었습니다. 로그인해주세요.");
    navigate("/login");
  };

  return (
    <div className="register-container">
      <h1>회원가입</h1>
      <div className="info-message">
        * 보안을 위해 비밀번호는 8자 이상으로 설정해주세요.
      </div>
      <strong className="email-info">
        가입 인증을 위한 이메일을 보내드리오니
        <br />
        수신 가능한 이메일 주소를 사용해주세요.
      </strong>
      <TextBox
        ref={emailRef}
        label="이메일"
        type="email"
        placeholder="Enter email"
      />
      <div className="password-field">
        <TextBox
          ref={passwordRef}
          label="비밀번호"
          type="password"
          placeholder="비밀번호 8자 이상 입력"
        />
        <span className="password-hint">비밀번호는 8자 이상이어야 합니다</span>
      </div>
      <TextBox
        ref={passwordCheckRef}
        label="비밀번호 확인"
        type="password"
        placeholder="비밀번호 재입력"
      />
      <button className="register-btn" onClick={handleRegister}>
        가입하기
      </button>
    </div>
  );
};

export default Register;
