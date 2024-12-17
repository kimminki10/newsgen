import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "./AuthContext";

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleSubmit = (e) => {
    e.preventDefault();
    const email = e.target.email.value;
    // 실제 백엔드 연동 대신 임시로 로그인 처리
    login(email);
    navigate("/"); // 홈으로 리다이렉트
  };

  return (
    <div>
      <h2>로그인</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>이메일주소</label>
          <input type="email" name="email" placeholder="Enter email" required />
        </div>
        <div>
          <label>비밀번호</label>
          <input
            type="password"
            name="password"
            placeholder="Enter password"
            required
          />
        </div>
        <button type="submit">로그인</button>
      </form>
    </div>
  );
};

export default Login;
