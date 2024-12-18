import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import TextBox from "./TextBox";
import resetPasswordMailService from "../services/mail/resetPasswordMailService";
import "./TextBox.css";
import "./ResetPasswordPage.css";

const ResetPasswordPage = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

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
      // 비밀번호 재설정 이메일 전송
      await resetPasswordMailService.sendResetPasswordEmail(email);
      // 성공시 확인 페이지로 이동
      navigate("/check-email");
    } catch (err) {
      setError("이메일 전송에 실패했습니다. 다시 시도해주세요.");
      console.error("Reset password email error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="reset-container">
      <h1>비밀번호 재설정</h1>
      <strong>
        회원 등록시 사용한 이메일 주소를 입력하십시오.
        <br />
        비밀번호를 재설정할 수 있는 링크가 포함된 이메일을 보내드립니다.
      </strong>
      <TextBox
        label="이메일"
        type="email"
        placeholder="Enter email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        disabled={loading}
        required
      />
      {error && <p className="error-message">{error}</p>}
      <button type="submit" className="reset-btn" disabled={loading}>
        {loading ? "이메일 전송중..." : "비밀번호 복구"}
      </button>
    </form>
  );
};

export default ResetPasswordPage;
