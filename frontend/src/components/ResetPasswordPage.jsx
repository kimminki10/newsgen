import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import resetPasswordMailService from "../services/mail/resetPasswordMailService";
import "./ResetPasswordPage.css";

const ResetPasswordPage = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLoginClick = () => {
    navigate("/login");
  };

  const handleRegisterClick = () => {
    navigate("/register");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // 이메일 유효성 검사
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
      setError("이메일을 입력해주세요.");
      return;
    }
    if (!emailRegex.test(email)) {
      setError("유효한 이메일 주소를 입력해주세요.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      await resetPasswordMailService.sendResetPasswordEmail(email);
      navigate("/check-email");
    } catch (err) {
      setError("이메일 전송에 실패했습니다. 다시 시도해주세요.");
      console.error("Reset password email error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="reset-container">
      <h1>비밀번호 재설정</h1>
      <div className="input-wrapper">
        <div className="description">
          <p>회원 등록시 사용한 이메일 주소를 입력하십시오.</p>
          <p>
            비밀번호를 재설정할 수 있는 링크가 포함된 이메일을 보내드립니다.
          </p>
        </div>
        <div className="input-field">
          <TextBox
            label="이메일"
            type="email"
            placeholder="example@gmail.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            disabled={loading}
            required
          />
          {error && <span className="error-message">{error}</span>}
        </div>
        <button
          type="submit"
          className="reset-btn"
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? "이메일 전송중..." : "비밀번호 복구"}
        </button>
        <div className="button-container">
          <button onClick={handleLoginClick}>로그인</button>
          <button onClick={handleRegisterClick}>가입하기</button>
        </div>
      </div>
    </div>
  );
};

export default ResetPasswordPage;
